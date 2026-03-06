"""
oracle_rag.retriever
~~~~~~~~~~~~~~~~~~~~
Retrieval library for Oracle documentation RAG.

Searches one or both SQLite/FTS5 databases produced by the scraper and
returns structured results that can be fed directly into an LLM prompt.

Basic usage::

    from oracle_rag.retriever import OracleRetriever, RetrievalConfig

    cfg = RetrievalConfig(
        dict_db='/path/to/data-dictionary/oracle_docs.db',
        plsql_db='/path/to/pl-sql/oracle_docs.db',
    )
    ret = OracleRetriever(cfg)

    # Separate results from each source
    result = ret.search('segment storage bytes blocks', limit=5)
    print(result.dict_chunks)   # data dictionary hits
    print(result.plsql_chunks)  # PL/SQL package hits

    # Exact name lookup
    chunk = ret.lookup('DBA_SEGMENTS')
    chunk = ret.lookup('DBMS_STATS.GATHER_TABLE_STATS')

    # All subprograms in a package
    chunks = ret.package_subprograms('DBMS_STATS')
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass
class RetrievalConfig:
    """
    Paths to the Oracle RAG SQLite databases.

    Can be set explicitly, or loaded from environment variables:
        ORACLE_RAG_DICT_DB   — path to data dictionary oracle_docs.db
        ORACLE_RAG_PLSQL_DB  — path to PL/SQL packages oracle_docs.db

    Or from a config file at ~/.oracle_rag.conf (INI format):
        [databases]
        dict_db  = /path/to/data-dictionary/oracle_docs.db
        plsql_db = /path/to/pl-sql/oracle_docs.db
    """
    dict_db:  Optional[str] = None   # data dictionary database path
    plsql_db: Optional[str] = None   # PL/SQL packages database path

    def __post_init__(self):
        # Environment variables take precedence over constructor args
        if os.environ.get("ORACLE_RAG_DICT_DB"):
            self.dict_db = os.environ["ORACLE_RAG_DICT_DB"]
        if os.environ.get("ORACLE_RAG_PLSQL_DB"):
            self.plsql_db = os.environ["ORACLE_RAG_PLSQL_DB"]

        # Fall back to config file
        if not self.dict_db or not self.plsql_db:
            self._load_config_file()

    def _load_config_file(self):
        import configparser
        cfg_path = Path.home() / ".oracle_rag.conf"
        if not cfg_path.exists():
            return
        cfg = configparser.ConfigParser()
        cfg.read(cfg_path)
        if "databases" in cfg:
            if not self.dict_db and cfg["databases"].get("dict_db"):
                self.dict_db = cfg["databases"]["dict_db"]
            if not self.plsql_db and cfg["databases"].get("plsql_db"):
                self.plsql_db = cfg["databases"]["plsql_db"]

    @classmethod
    def from_directory(cls, base_dir: str | Path, version: str = "19c") -> "RetrievalConfig":
        """
        Convenience constructor for the standard output directory layout:
            base_dir/
              <version>/
                data-dictionary/oracle_docs.db
                pl-sql/oracle_docs.db
        """
        base = Path(base_dir) / version
        return cls(
            dict_db=str(base / "data-dictionary" / "oracle_docs.db"),
            plsql_db=str(base / "pl-sql" / "oracle_docs.db"),
        )


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    """A single retrieved documentation chunk."""
    id:             str
    name:           str
    object_type:    str
    oracle_version: str
    doc_type:       str
    parent:         Optional[str]
    category:       Optional[str]
    description:    str
    columns:        list[dict]
    parameters:     list[dict]
    return_type:    Optional[str]
    syntax:         Optional[str]
    usage_notes:    str
    source_file:    str
    tags:           list[str]
    score:          float = 0.0     # FTS5 rank (lower = better in SQLite)

    @property
    def is_view(self) -> bool:
        return self.object_type == "data_dictionary_view"

    @property
    def is_package(self) -> bool:
        return self.object_type == "plsql_package"

    @property
    def is_subprogram(self) -> bool:
        return self.object_type in ("plsql_procedure", "plsql_function", "plsql_subprogram")

    def to_markdown(self, compact: bool = False) -> str:
        """
        Render chunk as Markdown for LLM context injection.
        compact=True: name + description only (minimal tokens)
        compact=False: full detail including columns, syntax, notes
        """
        lines = [f"## {self.name}"]
        if self.parent:
            lines.append(f"*Package: {self.parent}*")
        if self.category:
            lines.append(f"*Category: {self.category}*")
        lines += ["", self.description or "*(no description)*"]

        if compact:
            return "\n".join(lines)

        if self.syntax:
            lines += ["", "### Syntax", "", "```sql", self.syntax.strip(), "```"]

        if self.columns:
            lines += ["", "### Columns", "",
                      "| Column | Type | Null | Description |",
                      "|--------|------|------|-------------|"]
            for col in self.columns:
                n    = col.get("name", "")
                t    = col.get("type", "")
                null = col.get("nullable", "")
                d    = col.get("description", "").replace("\n", " ")
                lines.append(f"| {n} | {t} | {null} | {d} |")

        if self.parameters:
            lines += ["", "### Parameters", "",
                      "| Parameter | Type | Mode | Description |",
                      "|-----------|------|------|-------------|"]
            for p in self.parameters:
                pn   = p.get("name", "")
                pt   = p.get("type", "")
                pm   = p.get("mode", "")
                pd   = p.get("description", "").replace("\n", " ")
                lines.append(f"| {pn} | {pt} | {pm} | {pd} |")

        if self.return_type:
            lines += ["", f"**Returns:** `{self.return_type}`"]

        if self.usage_notes:
            lines += ["", "### Notes", "", self.usage_notes]

        return "\n".join(lines)

    def to_dict(self) -> dict:
        """Return chunk as a plain dict (JSON-serialisable)."""
        return {
            "id":             self.id,
            "name":           self.name,
            "object_type":    self.object_type,
            "oracle_version": self.oracle_version,
            "doc_type":       self.doc_type,
            "parent":         self.parent,
            "category":       self.category,
            "description":    self.description,
            "columns":        self.columns,
            "parameters":     self.parameters,
            "return_type":    self.return_type,
            "syntax":         self.syntax,
            "usage_notes":    self.usage_notes,
            "source_file":    self.source_file,
            "tags":           self.tags,
            "score":          self.score,
        }


@dataclass
class RetrievalResult:
    """
    Combined result from a retrieval operation.
    dict_chunks and plsql_chunks are kept separate so the caller
    can decide how to combine or present them.
    """
    query:        str
    dict_chunks:  list[Chunk] = field(default_factory=list)
    plsql_chunks: list[Chunk] = field(default_factory=list)

    @property
    def all_chunks(self) -> list[Chunk]:
        """All chunks combined, dict first then PL/SQL."""
        return self.dict_chunks + self.plsql_chunks

    @property
    def total(self) -> int:
        return len(self.dict_chunks) + len(self.plsql_chunks)

    def to_markdown(self, compact: bool = False) -> str:
        """Render full result as Markdown, suitable for LLM context."""
        sections = [f"# Oracle Documentation: {self.query}", ""]

        if self.dict_chunks:
            sections += ["## Data Dictionary Views", ""]
            for chunk in self.dict_chunks:
                sections.append(chunk.to_markdown(compact=compact))
                sections.append("")

        if self.plsql_chunks:
            sections += ["## PL/SQL Package Subprograms", ""]
            for chunk in self.plsql_chunks:
                sections.append(chunk.to_markdown(compact=compact))
                sections.append("")

        return "\n".join(sections)

    def to_dict(self) -> dict:
        return {
            "query":        self.query,
            "dict_chunks":  [c.to_dict() for c in self.dict_chunks],
            "plsql_chunks": [c.to_dict() for c in self.plsql_chunks],
            "total":        self.total,
        }


# ---------------------------------------------------------------------------
# Database connection helper
# ---------------------------------------------------------------------------

def _row_to_chunk(row: sqlite3.Row, score: float = 0.0) -> Chunk:
    return Chunk(
        id=row["id"],
        name=row["name"],
        object_type=row["object_type"],
        oracle_version=row["oracle_version"],
        doc_type=row["doc_type"],
        parent=row["parent"],
        category=row["category"],
        description=row["description"] or "",
        columns=json.loads(row["columns_json"] or "[]"),
        parameters=json.loads(row["parameters_json"] or "[]"),
        return_type=row["return_type"],
        syntax=row["syntax"],
        usage_notes=row["usage_notes"] or "",
        source_file=row["source_file"],
        tags=json.loads(row["tags_json"] or "[]"),
        score=score,
    )


def _open_db(path: str) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    return con


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------

def _build_fts_query(query: str) -> str:
    """
    Convert a natural language query string to an FTS5 OR query.
    Strips punctuation, splits on whitespace, joins with OR.
    Single-word queries are passed through unchanged.
    """
    # Strip characters that would confuse FTS5 parser
    cleaned = re.sub(r'["\'\(\)\*\:\.]', ' ', query)
    tokens = [t for t in cleaned.split() if len(t) > 1]
    if not tokens:
        return query
    if len(tokens) == 1:
        return tokens[0]
    return " OR ".join(tokens)


# ---------------------------------------------------------------------------
# Core retriever
# ---------------------------------------------------------------------------

class OracleRetriever:
    """
    Retrieves Oracle documentation chunks from SQLite/FTS5 databases.

    Example::

        ret = OracleRetriever(RetrievalConfig(
            dict_db='output/19c/data-dictionary/oracle_docs.db',
            plsql_db='output/19c/pl-sql/oracle_docs.db',
        ))

        # Keyword search
        result = ret.search('session wait events', limit=5)

        # Exact name lookup (single chunk or None)
        chunk = ret.lookup('V$SESSION')
        chunk = ret.lookup('DBMS_STATS.GATHER_TABLE_STATS')

        # All subprograms for a package
        chunks = ret.package_subprograms('DBMS_STATS')

        # All views matching a name prefix
        chunks = ret.views_like('DBA_HIST_%', limit=20)
    """

    def __init__(self, config: RetrievalConfig):
        self.config = config
        self._dict_con:  Optional[sqlite3.Connection] = None
        self._plsql_con: Optional[sqlite3.Connection] = None

        if config.dict_db and Path(config.dict_db).exists():
            self._dict_con = _open_db(config.dict_db)
        if config.plsql_db and Path(config.plsql_db).exists():
            self._plsql_con = _open_db(config.plsql_db)

        if not self._dict_con and not self._plsql_con:
            raise ValueError(
                "No databases found. Set dict_db and/or plsql_db in RetrievalConfig, "
                "environment variables ORACLE_RAG_DICT_DB / ORACLE_RAG_PLSQL_DB, "
                "or ~/.oracle_rag.conf"
            )

    def close(self):
        if self._dict_con:
            self._dict_con.close()
        if self._plsql_con:
            self._plsql_con.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    # ------------------------------------------------------------------
    # Internal search against a single connection
    # ------------------------------------------------------------------

    def _fts_search(
        self,
        con: sqlite3.Connection,
        fts_query: str,
        limit: int,
        object_types: Optional[list[str]] = None,
        version: Optional[str] = None,
    ) -> list[Chunk]:
        """Run an FTS5 search against one database."""
        sql = """
            SELECT c.*, f.rank AS fts_rank
            FROM chunks_fts f
            JOIN chunks c ON c.rowid = f.rowid
            WHERE chunks_fts MATCH ?
        """
        params: list = [fts_query]

        if object_types:
            placeholders = ",".join("?" * len(object_types))
            sql += f" AND c.object_type IN ({placeholders})"
            params.extend(object_types)

        if version:
            sql += " AND c.oracle_version = ?"
            params.append(version)

        sql += " ORDER BY f.rank LIMIT ?"
        params.append(limit)

        try:
            rows = con.execute(sql, params).fetchall()
            return [_row_to_chunk(r, score=r["fts_rank"]) for r in rows]
        except sqlite3.OperationalError as e:
            # FTS5 query syntax error — fall back to name LIKE search
            if "fts5" in str(e).lower() or "syntax" in str(e).lower():
                return self._name_search(con, fts_query.split()[0], limit)
            raise

    def _name_search(
        self,
        con: sqlite3.Connection,
        name: str,
        limit: int,
    ) -> list[Chunk]:
        """Fallback: search by name prefix."""
        rows = con.execute(
            "SELECT * FROM chunks WHERE name LIKE ? ORDER BY name LIMIT ?",
            (f"%{name.upper()}%", limit),
        ).fetchall()
        return [_row_to_chunk(r) for r in rows]

    def _exact_lookup(
        self,
        con: sqlite3.Connection,
        name: str,
    ) -> Optional[Chunk]:
        """Look up a single chunk by exact name (case-insensitive)."""
        row = con.execute(
            "SELECT * FROM chunks WHERE UPPER(name) = UPPER(?)",
            (name,),
        ).fetchone()
        return _row_to_chunk(row) if row else None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search(
        self,
        query: str,
        limit: int = 5,
        version: Optional[str] = None,
        dict_only: bool = False,
        plsql_only: bool = False,
    ) -> RetrievalResult:
        """
        Full-text search across both databases.

        Args:
            query:      Natural language or keyword query string.
            limit:      Max results per database (default 5).
            version:    Filter by Oracle version, e.g. '19c'.
            dict_only:  Only search data dictionary database.
            plsql_only: Only search PL/SQL packages database.

        Returns:
            RetrievalResult with dict_chunks and plsql_chunks populated.
        """
        fts_query = _build_fts_query(query)
        result = RetrievalResult(query=query)

        if not plsql_only and self._dict_con:
            result.dict_chunks = self._fts_search(
                self._dict_con, fts_query, limit, version=version
            )

        if not dict_only and self._plsql_con:
            result.plsql_chunks = self._fts_search(
                self._plsql_con, fts_query, limit, version=version
            )

        return result

    def lookup(self, name: str) -> Optional[Chunk]:
        """
        Exact name lookup across both databases.
        Checks data dictionary first, then PL/SQL packages.
        Supports dotted names like 'DBMS_STATS.GATHER_TABLE_STATS'.

        Returns the first match found, or None.
        """
        if self._dict_con:
            chunk = self._exact_lookup(self._dict_con, name)
            if chunk:
                return chunk
        if self._plsql_con:
            chunk = self._exact_lookup(self._plsql_con, name)
            if chunk:
                return chunk
        return None

    def lookup_many(self, names: list[str]) -> list[Chunk]:
        """
        Look up multiple names, returning all found chunks.
        Useful when you have a list of identifiers from code analysis.
        """
        chunks = []
        for name in names:
            chunk = self.lookup(name)
            if chunk:
                chunks.append(chunk)
        return chunks

    def package_subprograms(
        self,
        package_name: str,
        version: Optional[str] = None,
    ) -> list[Chunk]:
        """
        Return all subprograms for a given package, sorted by name.
        Excludes the package-level chunk itself.
        """
        if not self._plsql_con:
            return []
        sql = """
            SELECT * FROM chunks
            WHERE UPPER(parent) = UPPER(?)
              AND object_type IN ('plsql_procedure','plsql_function','plsql_subprogram')
        """
        params: list = [package_name]
        if version:
            sql += " AND oracle_version = ?"
            params.append(version)
        sql += " ORDER BY name"
        rows = self._plsql_con.execute(sql, params).fetchall()
        return [_row_to_chunk(r) for r in rows]

    def views_like(
        self,
        pattern: str,
        version: Optional[str] = None,
        limit: int = 50,
    ) -> list[Chunk]:
        """
        Return data dictionary views matching a SQL LIKE pattern.
        E.g. 'DBA_HIST_%', 'V$%SESSION%'
        """
        if not self._dict_con:
            return []
        sql = "SELECT * FROM chunks WHERE name LIKE ? AND object_type = 'data_dictionary_view'"
        params: list = [pattern]
        if version:
            sql += " AND oracle_version = ?"
            params.append(version)
        sql += " ORDER BY name LIMIT ?"
        params.append(limit)
        rows = self._dict_con.execute(sql, params).fetchall()
        return [_row_to_chunk(r) for r in rows]

    def related_views(self, view_name: str) -> list[Chunk]:
        """
        Given a view name like 'DBA_SEGMENTS', return the related
        ALL_ and USER_ variants (and vice versa).
        """
        if not self._dict_con:
            return []
        # Strip prefix to get base name
        base = re.sub(r'^(DBA_|ALL_|USER_|CDB_|V\$|GV\$)', '', view_name.upper())
        rows = self._dict_con.execute(
            """SELECT * FROM chunks
               WHERE (name LIKE ? OR name LIKE ? OR name LIKE ? OR name LIKE ?)
                 AND UPPER(name) != UPPER(?)
                 AND object_type = 'data_dictionary_view'
               ORDER BY name""",
            (f"DBA_{base}", f"ALL_{base}", f"USER_{base}", f"CDB_{base}", view_name.upper()),
        ).fetchall()
        return [_row_to_chunk(r) for r in rows]

    def stats(self) -> dict:
        """Return a summary of what's in each database."""
        out = {}
        for label, con in [("dict", self._dict_con), ("plsql", self._plsql_con)]:
            if con is None:
                out[label] = None
                continue
            rows = con.execute(
                "SELECT object_type, COUNT(*) as n FROM chunks GROUP BY object_type ORDER BY n DESC"
            ).fetchall()
            versions = con.execute(
                "SELECT DISTINCT oracle_version FROM chunks ORDER BY oracle_version"
            ).fetchall()
            out[label] = {
                "types": {r["object_type"]: r["n"] for r in rows},
                "versions": [r["oracle_version"] for r in versions],
                "total": sum(r["n"] for r in rows),
            }
        return out
