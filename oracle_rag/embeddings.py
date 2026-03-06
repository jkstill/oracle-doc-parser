"""
oracle_rag.embeddings
~~~~~~~~~~~~~~~~~~~~~
Generates embeddings for Oracle documentation chunks using Ollama,
stores them in SQLite, and provides hybrid vector+FTS5 search.

The embedding text for each chunk is:
    "{name}\n{description}\n{column_or_param_names}"

This gives the semantic search enough signal to match natural language
questions like "which sessions are waiting" to V$SESSION_WAIT without
requiring exact keyword overlap.
"""

from __future__ import annotations

import json
import math
import sqlite3
import struct
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

from oracle_rag.retriever import Chunk, _open_db, _row_to_chunk


# ---------------------------------------------------------------------------
# Vector serialisation — store as raw float32 BLOBs (compact, fast)
# ---------------------------------------------------------------------------

def vec_to_blob(vector: list[float]) -> bytes:
    return struct.pack(f"{len(vector)}f", *vector)


def blob_to_vec(blob: bytes) -> list[float]:
    n = len(blob) // 4
    return list(struct.unpack(f"{n}f", blob))


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(x * x for x in b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


# ---------------------------------------------------------------------------
# Embedding text builder
# ---------------------------------------------------------------------------

def chunk_to_embed_text(chunk: Chunk) -> str:
    """
    Build the text to embed for a chunk.
    Combines name + description + column/param names for maximum signal.
    """
    parts = [chunk.name]

    if chunk.description:
        parts.append(chunk.description)

    # Column names (views)
    if chunk.columns:
        col_names = " ".join(c["name"] for c in chunk.columns if c.get("name"))
        if col_names:
            parts.append(col_names)

    # Parameter names (subprograms)
    if chunk.parameters:
        param_names = " ".join(p["name"] for p in chunk.parameters if p.get("name"))
        if param_names:
            parts.append(param_names)

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Ollama embedding client
# ---------------------------------------------------------------------------

class EmbeddingClient:
    """
    Calls the Ollama /api/embed endpoint to generate embeddings.

    Args:
        base_url:   Ollama server URL, e.g. 'http://lestrade:11434'
        model:      Embedding model name, e.g. 'mxbai-embed-large:latest'
        batch_size: Number of texts to embed per API call (default 32)
        timeout:    Request timeout in seconds (default 60)
        retry:      Number of retries on transient failures (default 3)
    """

    def __init__(
        self,
        base_url: str,
        model: str = "mxbai-embed-large:latest",
        batch_size: int = 32,
        timeout: int = 60,
        retry: int = 3,
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.batch_size = batch_size
        self.timeout = timeout
        self.retry = retry

    def embed_one(self, text: str) -> list[float]:
        """Embed a single text string."""
        return self.embed_batch([text])[0]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed a list of texts, returns list of vectors."""
        url = f"{self.base_url}/api/embed"
        payload = json.dumps({
            "model": self.model,
            "input": texts,
        }).encode("utf-8")

        for attempt in range(self.retry):
            try:
                req = urllib.request.Request(
                    url,
                    data=payload,
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = json.loads(resp.read())
                    return data["embeddings"]
            except urllib.error.URLError as e:
                if attempt < self.retry - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise ConnectionError(
                    f"Embedding request failed at {self.base_url}: {e}"
                ) from e

    def check_connection(self) -> int:
        """
        Test connection and return embedding dimension.
        Raises ConnectionError if unreachable.
        """
        vec = self.embed_one("test")
        return len(vec)


# ---------------------------------------------------------------------------
# Schema management
# ---------------------------------------------------------------------------

EMBED_SCHEMA = """
    -- Embedding vectors stored as float32 BLOBs
    CREATE TABLE IF NOT EXISTS embeddings (
        chunk_id    TEXT PRIMARY KEY,
        model       TEXT NOT NULL,
        vector      BLOB NOT NULL,
        dimensions  INTEGER NOT NULL,
        embed_text  TEXT,           -- the text that was embedded (for inspection)
        created_at  TEXT DEFAULT (datetime('now'))
    );
    CREATE INDEX IF NOT EXISTS idx_embed_model ON embeddings(model);
"""


def ensure_embed_schema(con: sqlite3.Connection):
    con.executescript(EMBED_SCHEMA)
    con.commit()


def get_embedded_ids(con: sqlite3.Connection, model: str) -> set[str]:
    """Return set of chunk IDs already embedded with this model."""
    rows = con.execute(
        "SELECT chunk_id FROM embeddings WHERE model = ?", (model,)
    ).fetchall()
    return {r[0] for r in rows}


# ---------------------------------------------------------------------------
# Indexer — embeds all chunks and stores vectors
# ---------------------------------------------------------------------------

def index_database(
    db_path: str,
    client: EmbeddingClient,
    force: bool = False,
    progress_cb=None,
) -> dict:
    """
    Embed all chunks in a database and store vectors.

    Args:
        db_path:     Path to oracle_docs.db
        client:      EmbeddingClient instance
        force:       Re-embed even if already embedded
        progress_cb: Optional callback(current, total, chunk_name)

    Returns:
        dict with 'embedded', 'skipped', 'failed' counts
    """
    con = _open_db(db_path)
    ensure_embed_schema(con)

    already_embedded = set() if force else get_embedded_ids(con, client.model)

    # Load all chunks
    rows = con.execute("SELECT * FROM chunks ORDER BY name").fetchall()
    chunks = [_row_to_chunk(r) for r in rows]

    to_embed = [c for c in chunks if c.id not in already_embedded]
    total = len(to_embed)
    stats = {"embedded": 0, "skipped": len(already_embedded), "failed": 0}

    if total == 0:
        con.close()
        return stats

    # Process in batches
    for batch_start in range(0, total, client.batch_size):
        batch = to_embed[batch_start:batch_start + client.batch_size]
        texts = [chunk_to_embed_text(c) for c in batch]

        try:
            vectors = client.embed_batch(texts)
        except ConnectionError as e:
            print(f"  Batch failed: {e}")
            stats["failed"] += len(batch)
            continue

        for chunk, text, vector in zip(batch, texts, vectors):
            con.execute(
                """INSERT OR REPLACE INTO embeddings
                   (chunk_id, model, vector, dimensions, embed_text)
                   VALUES (?, ?, ?, ?, ?)""",
                (chunk.id, client.model, vec_to_blob(vector), len(vector), text),
            )
            stats["embedded"] += 1

            if progress_cb:
                progress_cb(batch_start + stats["embedded"], total, chunk.name)

        con.commit()

    con.close()
    return stats


# ---------------------------------------------------------------------------
# Hybrid search
# ---------------------------------------------------------------------------

class HybridSearcher:
    """
    Combines vector similarity search with FTS5 keyword search.

    Scoring:
        hybrid_score = (alpha * vector_score) + ((1 - alpha) * fts_score)

    alpha=1.0 → pure vector
    alpha=0.0 → pure FTS5
    alpha=0.6 → default: vector-weighted hybrid
    """

    def __init__(
        self,
        db_path: str,
        client: EmbeddingClient,
        alpha: float = 0.6,
        embed_model: Optional[str] = None,
    ):
        self.db_path = db_path
        self.client = client
        self.alpha = alpha
        self.embed_model = embed_model or client.model
        self._con = _open_db(db_path)

    def close(self):
        self._con.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def _vector_search(self, query_vec: list[float], limit: int) -> list[tuple[str, float]]:
        """
        Brute-force cosine similarity over all stored vectors.
        Returns list of (chunk_id, similarity_score) sorted descending.
        Fast enough for 6400 chunks — ~50ms typically.
        """
        rows = self._con.execute(
            "SELECT chunk_id, vector FROM embeddings WHERE model = ?",
            (self.embed_model,),
        ).fetchall()

        scores = []
        for chunk_id, blob in rows:
            vec = blob_to_vec(blob)
            sim = cosine_similarity(query_vec, vec)
            scores.append((chunk_id, sim))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:limit * 3]  # fetch extra for merging

    def _fts_search(self, query: str, limit: int) -> list[tuple[str, float]]:
        """
        FTS5 search. Returns list of (chunk_id, normalised_score).
        FTS5 rank is negative (lower = better), normalise to [0,1].
        """
        from oracle_rag.retriever import _build_fts_query
        fts_query = _build_fts_query(query)

        try:
            rows = self._con.execute(
                """SELECT c.id, f.rank
                   FROM chunks_fts f
                   JOIN chunks c ON c.rowid = f.rowid
                   WHERE chunks_fts MATCH ?
                   ORDER BY f.rank
                   LIMIT ?""",
                (fts_query, limit * 3),
            ).fetchall()
        except sqlite3.OperationalError:
            return []

        if not rows:
            return []

        # Normalise FTS5 rank to [0, 1] — rank is negative, so min is worst
        ranks = [r[1] for r in rows]
        min_rank = min(ranks)
        max_rank = max(ranks)
        span = max_rank - min_rank if max_rank != min_rank else 1.0

        return [
            (chunk_id, (rank - min_rank) / span)
            for chunk_id, rank in rows
        ]

    def search(
        self,
        query: str,
        limit: int = 5,
        version: Optional[str] = None,
        object_types: Optional[list[str]] = None,
    ) -> list[Chunk]:
        """
        Hybrid search: embed query, merge vector + FTS5 scores, return chunks.
        """
        # Embed the query
        query_vec = self.client.embed_one(query)

        # Get scores from both sources
        vec_scores  = dict(self._vector_search(query_vec, limit))
        fts_scores  = dict(self._fts_search(query, limit))

        # Union of all candidate chunk IDs
        all_ids = set(vec_scores) | set(fts_scores)

        # Compute hybrid score
        hybrid = {}
        for cid in all_ids:
            vs = vec_scores.get(cid, 0.0)
            fs = fts_scores.get(cid, 0.0)
            hybrid[cid] = (self.alpha * vs) + ((1 - self.alpha) * fs)

        # Sort by hybrid score descending
        ranked = sorted(hybrid.items(), key=lambda x: x[1], reverse=True)

        # Fetch the top chunks from DB
        top_ids = [cid for cid, _ in ranked[:limit * 2]]
        if not top_ids:
            return []

        placeholders = ",".join("?" * len(top_ids))
        sql = f"SELECT * FROM chunks WHERE id IN ({placeholders})"
        params = list(top_ids)

        if version:
            sql += " AND oracle_version = ?"
            params.append(version)
        if object_types:
            ph2 = ",".join("?" * len(object_types))
            sql += f" AND object_type IN ({ph2})"
            params.extend(object_types)

        rows = self._con.execute(sql, params).fetchall()
        row_map = {r["id"]: r for r in rows}

        # Return in ranked order, up to limit
        result = []
        for cid, score in ranked:
            if cid in row_map:
                chunk = _row_to_chunk(row_map[cid], score=score)
                result.append(chunk)
            if len(result) >= limit:
                break

        return result

    def coverage(self) -> dict:
        """Return embedding coverage stats."""
        total = self._con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        embedded = self._con.execute(
            "SELECT COUNT(*) FROM embeddings WHERE model = ?",
            (self.embed_model,),
        ).fetchone()[0]
        return {
            "total_chunks": total,
            "embedded": embedded,
            "coverage_pct": round(100 * embedded / total, 1) if total else 0,
            "model": self.embed_model,
        }
