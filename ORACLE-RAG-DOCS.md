# Oracle RAG Documentation

A pipeline for converting local Oracle HTML documentation into a retrieval-augmented generation (RAG) corpus, and querying it with natural language to produce accurate SQL and PL/SQL.

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [Project Layout](#project-layout)
5. [Step 1 — Parse the Documentation](#step-1--parse-the-documentation)
6. [Step 2 — Install the oracle-rag Package](#step-2--install-the-oracle-rag-package)
7. [Step 3 — Configure Database Paths](#step-3--configure-database-paths)
8. [Step 4 — Index Embeddings](#step-4--index-embeddings)
9. [CLI Reference](#cli-reference)
10. [Python Library Reference](#python-library-reference)
11. [LLM Backends](#llm-backends)
12. [How Hybrid Search Works](#how-hybrid-search-works)
13. [Output Formats](#output-formats)
14. [Troubleshooting](#troubleshooting)

---

## Overview

Oracle-specific SQL and PL/SQL are undertrained in most LLMs. Models frequently hallucinate column names, invent non-existent views, or produce subtly wrong syntax for built-in packages. This pipeline addresses that by:

1. Parsing local Oracle HTML documentation into structured chunks (one chunk per view or subprogram)
2. Storing chunks in SQLite with full-text search (FTS5)
3. Generating semantic embeddings for each chunk using `mxbai-embed-large` via Ollama
4. At query time, performing hybrid vector + keyword search to retrieve the most relevant documentation
5. Injecting that documentation as context into an LLM prompt, instructing the model to use only the exact names it finds there

The result is a system that reliably produces syntactically and semantically correct Oracle SQL using real column names and view names from the official documentation.

---

## Architecture

```
Oracle HTML docs (local)
        │
        ▼
   scraper.py
        │
        ├── JSONL output          (one record per chunk)
        ├── Markdown output       (one .md file per chunk, with YAML front-matter)
        └── SQLite output         oracle_docs.db
                │
                ├── chunks table  (structured data)
                ├── chunks_fts    (FTS5 virtual table for keyword search)
                └── embeddings    (float32 vectors, added by oracle-rag embed)
                        │
                        ▼
                oracle-rag CLI / Python library
                        │
                        ├── search    (hybrid vector + FTS5)
                        ├── lookup    (exact name)
                        ├── ask       (retrieves context → sends to LLM)
                        └── ...
```

Two separate databases are maintained:

| Database | Content | Doc path |
|----------|---------|----------|
| `data-dictionary/oracle_docs.db` | DBA_*, ALL_*, USER_*, V$*, GV$* views | `refrn/` |
| `pl-sql/oracle_docs.db` | DBMS_*, UTL_*, HTP, HTF packages | `arpls/` |

---

## Prerequisites

**On the parsing/query host:**

- Python 3.10+
- `beautifulsoup4` and `lxml` (for the scraper)
- Local copy of Oracle HTML documentation

**On the Ollama host (can be a separate server):**

- [Ollama](https://ollama.com) with `mxbai-embed-large:latest` pulled for embeddings
- A generation model such as `qwen2.5:14b`, `llama3`, or `gemma3:12b`
- Ollama must be reachable from the query host on port 11434

**Install scraper dependencies:**

```bash
pip install beautifulsoup4 lxml --break-system-packages
```

**Verify Ollama connectivity and embedding dimensions:**

```bash
curl -s http://<ollama-host>:11434/api/embed \
  -d '{"model":"mxbai-embed-large:latest","input":"test"}' \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d['embeddings'][0]))"
# Expected: 1024
```

---

## Project Layout

```
doc-parser/
├── scraper.py                   # HTML documentation parser
├── data_dictionary_scraper.py   # Alias / renamed scraper for data dictionary
├── oracle-rag                   # CLI tool (renamed from oracle_rag/cli.py)
├── setup.py                     # Package installation
├── requirements.txt             # scraper dependencies
├── oracle_rag.conf.example      # Example config file
├── test_scraper.py              # Scraper tests
├── test_retriever.py            # Retriever library tests
└── oracle_rag/
    ├── __init__.py
    ├── retriever.py             # Core retrieval library
    ├── embeddings.py            # Embedding generation and hybrid search
    ├── backends.py              # LLM backends (Ollama, Gemini CLI)
    └── cli.py                   # CLI entry point (source for oracle-rag)

output/
└── 19c/
    ├── data-dictionary/
    │   ├── oracle_docs.db       # SQLite: chunks + FTS5 + embeddings
    │   ├── chunks.jsonl         # JSONL export
    │   └── md/                  # Per-chunk Markdown files
    └── pl-sql/
        ├── oracle_docs.db
        ├── chunks.jsonl
        └── md/
```

---

## Step 1 — Parse the Documentation

The scraper walks a directory of Oracle HTML files and extracts structured chunks. Run it separately for each doc type.

### Data Dictionary Views

```bash
python data_dictionary_scraper.py \
    --path /path/to/oracle/docs/19c/refrn \
    --version 19c \
    --doctype database_reference \
    --output ./output/19c/data-dictionary/
```

This parses views like `DBA_SEGMENTS`, `V$SESSION`, `ALL_TABLES`, extracting:
- View name and description
- Column table (name, datatype, NULL constraint, description)
- Usage notes

### PL/SQL Package Reference

```bash
python data_dictionary_scraper.py \
    --path /path/to/oracle/docs/19c/arpls \
    --version 19c \
    --doctype plsql_packages \
    --output ./output/19c/pl-sql/
```

This parses packages like `DBMS_STATS`, `DBMS_METADATA`, `UTL_FILE`, extracting:
- Package overview chunk
- One chunk per subprogram (procedure or function)
- Syntax block, parameter table, return type

### Scraper Options

| Option | Default | Description |
|--------|---------|-------------|
| `--path` | *(required)* | Root directory of local Oracle HTML docs |
| `--version` | *(required)* | Oracle version tag, e.g. `19c`, `21c`, `23ai` |
| `--doctype` | `all` | `database_reference`, `plsql_packages`, or `all` |
| `--output` | `./output` | Output directory |
| `--max-files` | none | Limit file count (useful for testing) |
| `--no-jsonl` | off | Skip JSONL output |
| `--no-markdown` | off | Skip Markdown output |
| `--no-sqlite` | off | Skip SQLite output |
| `--verbose` / `-v` | off | Enable debug logging |

### Expected Results (Oracle 19c)

| Database | Chunks | Notes |
|----------|--------|-------|
| data-dictionary | ~2,571 | 84% yield from ~3,059 HTML files |
| pl-sql | ~3,537 | Includes package + per-subprogram chunks |

Pages that yield no chunk (synonym redirects, intro pages, TOC pages) are silently skipped — this is expected behaviour.

### Notes on Specific Views

Some `DBA_` views (e.g. `DBA_TABLES`) contain no column table in their HTML — instead the description reads "its columns are the same as those in `ALL_TABLES`". The scraper captures the description correctly. At query time, searches for `DBA_TABLES` column information will naturally retrieve `ALL_TABLES` via FTS5 or vector similarity since they share column names in their embeddings.

---

## Step 2 — Install the oracle-rag Package

From the project directory:

```bash
pip install -e . --break-system-packages
```

This installs the `oracle-rag` entry point. Alternatively, copy `oracle_rag/cli.py` to a file named `oracle-rag` and make it executable:

```bash
cp oracle_rag/cli.py oracle-rag
chmod +x oracle-rag
```

---

## Step 3 — Configure Database Paths

The tool needs to know where the two `oracle_docs.db` files live. Configuration is resolved in this order:

### Option A — Config file (recommended)

Copy the example and edit it:

```bash
cp oracle_rag.conf.example ~/.oracle_rag.conf
```

```ini
[databases]
dict_db  = /home/jkstill/ai/doc-parser/output/19c/data-dictionary/oracle_docs.db
plsql_db = /home/jkstill/ai/doc-parser/output/19c/pl-sql/oracle_docs.db
```

### Option B — Environment variables

```bash
export ORACLE_RAG_DICT_DB=/path/to/data-dictionary/oracle_docs.db
export ORACLE_RAG_PLSQL_DB=/path/to/pl-sql/oracle_docs.db
```

### Option C — CLI flags

```bash
./oracle-rag --dict-db /path/to/dict/oracle_docs.db \
             --plsql-db /path/to/plsql/oracle_docs.db \
             stats
```

### Option D — Directory layout convention

```bash
./oracle-rag --base-dir ./output --db-version 19c stats
```

This assumes the standard layout: `<base-dir>/<version>/data-dictionary/oracle_docs.db` and `<base-dir>/<version>/pl-sql/oracle_docs.db`.

---

## Step 4 — Index Embeddings

Embeddings must be generated once before hybrid search is available. The indexer calls the Ollama embedding API and stores 1024-dimensional float32 vectors in the `embeddings` table of each SQLite database.

```bash
./oracle-rag embed --ollama-url http://<ollama-host>:11434
```

This indexes both databases. To index only one:

```bash
./oracle-rag embed --ollama-url http://<ollama-host>:11434 --db dict
./oracle-rag embed --ollama-url http://<ollama-host>:11434 --db plsql
```

### Embed Options

| Option | Default | Description |
|--------|---------|-------------|
| `--ollama-url` | `http://localhost:11434` | Ollama server URL |
| `--embed-model` | `mxbai-embed-large:latest` | Embedding model |
| `--db` | `both` | `dict`, `plsql`, or `both` |
| `--batch-size` | `32` | Chunks per API call |
| `--force` | off | Re-embed already-indexed chunks |

Progress is reported every 5%. The command is safe to re-run — already-embedded chunks are skipped unless `--force` is given. Interrupted runs can be resumed by running the same command again.

**Approximate timing:** 6,000 chunks at batch size 32 takes 5–10 minutes depending on GPU speed and network latency.

**Verify coverage after indexing:**

```bash
./oracle-rag stats
```

```
=== dict (2571 chunks) ===
Versions: 19c
   2571  data_dictionary_view

  dict embeddings: 2571 vectors (mxbai-embed-large:latest)

=== plsql (3537 chunks) ===
Versions: 19c
   1779  plsql_procedure
   ...
  plsql embeddings: 3537 vectors (mxbai-embed-large:latest)
```

---

## CLI Reference

### Shared Options

These options are available on every subcommand except `models` and `claude-models`:

| Option | Default | Description |
|--------|---------|-------------|
| `--dict-db PATH` | from config | Path to data dictionary `oracle_docs.db` |
| `--plsql-db PATH` | from config | Path to PL/SQL packages `oracle_docs.db` |
| `--base-dir PATH` | — | Base output directory — alternative to `--dict-db`/`--plsql-db` |
| `--db-version VER` | `auto` | Filter results by Oracle version, e.g. `19c` |
| `--format` | `markdown` | Output format: `markdown` or `json` |
| `--compact` | off | Return name + description only (no columns/parameters/syntax) |
| `--limit N` | `5` | Maximum results returned per database |

---

### ask

The primary command. Retrieves relevant documentation via hybrid or FTS5 search and sends it as context to an LLM for SQL or PL/SQL generation.

```bash
# Ollama backend — hybrid search + local generation
./oracle-rag ask \
    --ollama-url http://lestrade:11434 \
    --model qwen2.5:14b \
    "write a query to show which sessions are waiting and on what events"

# Claude CLI backend — free, uses Claude.ai subscription
./oracle-rag ask \
    --backend claude \
    "write a query to show which sessions are waiting and on what events"

# Claude CLI backend — hybrid search (Ollama for embeddings, Claude CLI for generation)
./oracle-rag ask \
    --backend claude \
    --ollama-url http://lestrade:11434 \
    "write a query to show which sessions are waiting and on what events"

# Claude API backend — paid, per-token billing, requires ANTHROPIC_API_KEY
./oracle-rag ask \
    --backend claude-api \
    --model claude-haiku-4-5-20251001 \
    "write a query to show which sessions are waiting and on what events"

# Gemini CLI backend — hybrid search
./oracle-rag ask \
    --backend gemini \
    --ollama-url http://lestrade:11434 \
    "write a query to show which sessions are waiting and on what events"
```

**Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `--backend` | `ollama` | LLM backend: `ollama`, `gemini`, `claude`, or `claude-api` |
| `--ollama-url URL` | `None` | Ollama server URL. Required for `ollama` backend; optional for others (enables hybrid search when provided) |
| `--model MODEL` | varies | Generation model name. Required for `ollama`; optional for `gemini`, `claude`, and `claude-api` (each has a default) |
| `--embed-model MODEL` | `mxbai-embed-large:latest` | Embedding model used for hybrid search query vectorisation |
| `--gemini-cli PATH` | `gemini` | Path to the Gemini CLI binary if not on `PATH` |
| `--claude-cli PATH` | `claude` | Path to the Claude CLI binary if not on `PATH` |
| `--task` | `sql` | Prompt style: `sql`, `plsql`, `explain`, or `general` |
| `--timeout SECS` | `120` | LLM request timeout in seconds |
| `--dict-only` | off | Search only the data dictionary database |
| `--plsql-only` | off | Search only the PL/SQL packages database |
| `--include NAME[,NAME...]` | — | Force-include specific views or subprograms by exact name, comma-separated. Useful when search misses a known-relevant view |
| `--show-prompt` | off | Print the full prompt (instruction + context) to stderr before sending to the LLM |
| `--no-stats` | off | Suppress the token count and timing line printed after each response |
| `--alpha F` | `0.6` | Weight of vector score in hybrid scoring. `1.0` = pure vector, `0.0` = pure FTS5 |

Also accepts all shared options (`--limit`, `--compact`, `--format`, etc.).

**Backend comparison:**

| Backend | Cost | Token counts | Requirements |
|---------|------|-------------|--------------|
| `ollama` | Free | Exact | Ollama server, `--ollama-url`, `--model` |
| `gemini` | Free | Estimated | Gemini CLI installed and authenticated |
| `claude` | Free | Estimated | Claude CLI installed and authenticated |
| `claude-api` | Paid (per token) | Exact | `ANTHROPIC_API_KEY` env var |

**Task types:**

| Task | Prompt behaviour |
|------|-----------------|
| `sql` | Instructs the model to write SQL using only exact view and column names from the documentation |
| `plsql` | Instructs the model to write PL/SQL using only exact package, procedure, and parameter names |
| `explain` | Asks for a plain-language explanation referencing Oracle object names |
| `general` | No specific output format constraint |

**Search behaviour:**

| `--ollama-url` provided | Retrieval method |
|------------------------|-----------------|
| Yes | Hybrid vector + FTS5 (question is embedded via Ollama, cosine similarity + keyword scoring merged) |
| No | FTS5 keyword search only |

**Token and timing stats** are printed to stderr after every response:

```
--- tokens: 1842 in / 47 out / 1889 total  |  time: 4.3s ---
```

Token counts are exact for `ollama` and `claude-api` (returned by their APIs). For `gemini` and `claude` CLI backends they are estimated (`est` suffix) since the CLIs do not report token usage.

**Force-including specific views:**

```bash
./oracle-rag ask \
    --ollama-url http://lestrade:11434 \
    --model qwen2.5:14b \
    --include 'V$SESSION,V$SESSION_WAIT' \
    "show sessions waiting on I/O events"
```

**Inspecting the full prompt:**

```bash
./oracle-rag ask \
    --backend claude \
    --show-prompt \
    "show segments larger than 1GB" 2>&1 | less
```

### search

Full-text and/or vector search, returning matching documentation chunks without calling an LLM. Useful for inspecting what context would be sent to `ask`.

```bash
# FTS5 keyword search
./oracle-rag search "session wait events"
./oracle-rag search "segment storage bytes" --dict-only --limit 10

# Hybrid vector+FTS5 search (requires --ollama-url and indexed embeddings)
./oracle-rag search "session wait events" \
    --ollama-url http://lestrade:11434 \
    --limit 5

# JSON output
./oracle-rag search "redo log archiving" --format json
```

**Options (in addition to shared options):**

| Option | Default | Description |
|--------|---------|-------------|
| `--dict-only` | off | Search only the data dictionary database |
| `--plsql-only` | off | Search only the PL/SQL packages database |
| `--ollama-url URL` | — | Enable hybrid search using this Ollama server |
| `--embed-model MODEL` | `mxbai-embed-large:latest` | Embedding model for hybrid search |

---

### lookup

Exact name lookup across both databases. Returns full documentation including column or parameter tables.

```bash
./oracle-rag lookup DBA_SEGMENTS
./oracle-rag lookup DBMS_STATS.GATHER_TABLE_STATS
./oracle-rag lookup 'V$SESSION' 'V$SESSION_WAIT' DBA_WAITERS

# Compact output (name + description only)
./oracle-rag lookup DBA_SEGMENTS --compact

# JSON output
./oracle-rag lookup DBA_SEGMENTS --format json
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `NAME [NAME ...]` | One or more exact object names. Dotted names like `DBMS_STATS.GATHER_TABLE_STATS` are supported. Names not found are reported to stderr. |

---

### package

List all subprograms (procedures and functions) in a PL/SQL package.

```bash
./oracle-rag package DBMS_STATS
./oracle-rag package DBMS_STATS --compact     # names + descriptions only
./oracle-rag package UTL_FILE --format json
./oracle-rag package DBMS_METADATA --limit 20
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `PACKAGE` | Package name, e.g. `DBMS_STATS`, `UTL_FILE`, `DBMS_METADATA` |

---

### views

List data dictionary views matching a SQL LIKE pattern.

```bash
./oracle-rag views 'DBA_HIST_%'
./oracle-rag views 'V$%SESSION%' --limit 20
./oracle-rag views 'DBA_%PRIV%'
./oracle-rag views 'ALL_%' --compact --limit 50
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `PATTERN` | SQL LIKE pattern. `%` matches any sequence of characters. Quote the pattern in the shell to prevent glob expansion. |

---

### related

Show the DBA / ALL / USER / CDB view family for a given view name. Useful for understanding which privilege level a view requires.

```bash
./oracle-rag related DBA_SEGMENTS
# Returns: DBA_SEGMENTS, ALL_SEGMENTS

./oracle-rag related ALL_TABLES
# Returns: DBA_TABLES, ALL_TABLES, USER_TABLES, CDB_TABLES
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `VIEW` | Any member of the family, e.g. `DBA_SEGMENTS`, `ALL_TABLES`, `USER_INDEXES` |

---

### embed

Generate and store embedding vectors for all chunks in one or both databases. Must be run once before hybrid search is available. Safe to re-run — already-embedded chunks are skipped.

```bash
# Index both databases
./oracle-rag embed --ollama-url http://lestrade:11434

# Index only one database
./oracle-rag embed --ollama-url http://lestrade:11434 --db dict
./oracle-rag embed --ollama-url http://lestrade:11434 --db plsql

# Re-index everything from scratch
./oracle-rag embed --ollama-url http://lestrade:11434 --force
```

**Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `--ollama-url URL` | `http://localhost:11434` | Ollama server URL |
| `--embed-model MODEL` | `mxbai-embed-large:latest` | Embedding model |
| `--db` | `both` | Which database(s) to index: `dict`, `plsql`, or `both` |
| `--batch-size N` | `32` | Number of chunks per embedding API call |
| `--force` | off | Re-embed chunks even if already indexed |

Does not require database configuration from `~/.oracle_rag.conf` — paths are resolved from the shared options (`--dict-db`, `--plsql-db`, or `--base-dir`).

---

### stats

Show chunk counts, object type breakdown, and embedding coverage for both databases.

```bash
./oracle-rag stats
./oracle-rag stats --format json
```

No additional options beyond the shared options.

---

### models

List available models on an Ollama server. Does not require database configuration.

```bash
./oracle-rag models
./oracle-rag models --ollama-url http://lestrade:11434
```

**Options:**

| Option | Default | Description |
|--------|---------|-------------|
| `--ollama-url URL` | `http://localhost:11434` | Ollama server URL |

---

### claude-models

List available Claude model IDs from the Anthropic API. Does not require database configuration. Requires `ANTHROPIC_API_KEY` to be set.

```bash
export ANTHROPIC_API_KEY=sk-ant-...
./oracle-rag claude-models
```

No additional options.

## Python Library Reference

The `oracle_rag` package can be imported directly for scripting and integration.

### OracleRetriever

```python
from oracle_rag.retriever import OracleRetriever, RetrievalConfig

cfg = RetrievalConfig(
    dict_db='/path/to/data-dictionary/oracle_docs.db',
    plsql_db='/path/to/pl-sql/oracle_docs.db',
)

with OracleRetriever(cfg) as ret:

    # Keyword search — returns RetrievalResult
    result = ret.search('session wait events', limit=5)
    print(result.dict_chunks)   # data dictionary hits
    print(result.plsql_chunks)  # PL/SQL package hits

    # Exact name lookup — returns Chunk or None
    chunk = ret.lookup('V$SESSION')
    chunk = ret.lookup('DBMS_STATS.GATHER_TABLE_STATS')

    # Look up multiple names at once
    chunks = ret.lookup_many(['DBA_SEGMENTS', 'V$SESSION', 'DBA_WAITERS'])

    # All subprograms in a package
    subs = ret.package_subprograms('DBMS_STATS')

    # Views matching a pattern
    views = ret.views_like('DBA_HIST_%', limit=20)

    # DBA/ALL/USER family for a view
    family = ret.related_views('DBA_SEGMENTS')

    # Database statistics
    stats = ret.stats()
```

### RetrievalConfig

```python
# From explicit paths
cfg = RetrievalConfig(dict_db='/path/dict.db', plsql_db='/path/plsql.db')

# From environment variables ORACLE_RAG_DICT_DB / ORACLE_RAG_PLSQL_DB
cfg = RetrievalConfig()

# From standard directory layout
cfg = RetrievalConfig.from_directory('/path/to/output', version='19c')
```

### Chunk

Each retrieved chunk exposes:

```python
chunk.name           # 'V$SESSION' or 'DBMS_STATS.GATHER_TABLE_STATS'
chunk.object_type    # 'data_dictionary_view' | 'plsql_procedure' | ...
chunk.description    # Plain text description
chunk.columns        # list of {name, type, nullable, description}
chunk.parameters     # list of {name, type, mode, description}
chunk.return_type    # e.g. 'BOOLEAN' for functions
chunk.syntax         # Raw syntax block
chunk.usage_notes    # Additional notes
chunk.parent         # Package name for subprograms
chunk.category       # 'storage', 'performance', 'security', etc.
chunk.tags           # list of strings
chunk.score          # Relevance score from search

chunk.is_view        # True for data dictionary views
chunk.is_package     # True for package-level chunks
chunk.is_subprogram  # True for procedures/functions

# Render as Markdown
md = chunk.to_markdown()           # Full detail
md = chunk.to_markdown(compact=True)  # Name + description only

# Serialise
d = chunk.to_dict()   # JSON-serialisable dict
```

### HybridSearcher

```python
from oracle_rag.embeddings import EmbeddingClient, HybridSearcher

client = EmbeddingClient(
    base_url='http://lestrade:11434',
    model='mxbai-embed-large:latest',
)

with HybridSearcher('/path/to/oracle_docs.db', client, alpha=0.6) as hs:
    chunks = hs.search('sessions waiting on I/O events', limit=5)
    cov = hs.coverage()
    # {'total_chunks': 2571, 'embedded': 2571, 'coverage_pct': 100.0, ...}
```

`alpha` controls the vector/FTS5 balance:
- `1.0` — pure vector similarity
- `0.0` — pure FTS5 keyword
- `0.6` — default: vector-weighted hybrid

### EmbeddingClient

```python
from oracle_rag.embeddings import EmbeddingClient

client = EmbeddingClient(
    base_url='http://lestrade:11434',
    model='mxbai-embed-large:latest',
    batch_size=32,
    timeout=60,
)

dims = client.check_connection()   # Returns 1024, raises ConnectionError if unreachable
vec  = client.embed_one("some text")
vecs = client.embed_batch(["text1", "text2", "text3"])
```

---

## LLM Backends

### Ollama (local or remote)

```bash
./oracle-rag ask \
    --backend ollama \
    --ollama-url http://lestrade:11434 \
    --model qwen2.5:14b \
    "your question"
```

Calls `POST /api/generate` with `stream: false`. Works for any host reachable on the Ollama port. Token counts are exact (returned by the API).

### Gemini CLI

```bash
./oracle-rag ask \
    --backend gemini \
    --model gemini-1.5-pro \
    "your question"
```

Calls the `gemini` binary via subprocess with the prompt on stdin. Must be on `PATH` and authenticated. Use `--gemini-cli /path/to/gemini` if not on PATH. Token counts are estimated.

### Claude CLI (free)

```bash
./oracle-rag ask \
    --backend claude \
    "your question"
```

Calls the `claude` binary via subprocess using the `-p` flag for non-interactive single-prompt mode. Uses your Claude.ai subscription — no API costs. Install from https://claude.ai/download. Use `--claude-cli /path/to/claude` if not on PATH. Token counts are estimated.

### Claude API (paid)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
./oracle-rag ask \
    --backend claude-api \
    --model claude-haiku-4-5-20251001 \
    "your question"
```

Calls `https://api.anthropic.com/v1/messages` directly. Requires `ANTHROPIC_API_KEY`. Charges per token — Haiku is the most economical option. Token counts are exact (returned by the API). Use `./oracle-rag claude-models` to list available model IDs.

---

## How Hybrid Search Works

When `ask` or `search` is called with `--ollama-url` and embeddings are present, the following happens:

1. **Query embedding** — the question text is embedded using `mxbai-embed-large` via Ollama (the same model used during indexing)

2. **Vector search** — cosine similarity is computed between the query vector and all stored chunk vectors. The top candidates are selected.

3. **FTS5 search** — the question is tokenised and an OR query is run against the FTS5 index (name, description, column names, param names, usage notes). Results are normalised to [0, 1].

4. **Score merging** — hybrid score = `(alpha × vector_score) + ((1 - alpha) × fts_score)` with default `alpha = 0.6`. This weights semantic meaning higher than keyword overlap, while still rewarding exact name matches.

5. **Ranked results** — the top N chunks by hybrid score are returned and rendered as Markdown context for the LLM prompt.

**Why this works for Oracle documentation:** Natural language questions like "which sessions are waiting" do not share keywords with `V$SESSION_WAIT`, but the semantic embedding of the chunk text (which includes the description "displays one row for each active session that is currently waiting") is close to the query in vector space. FTS5 alone would miss this; vector search alone might miss exact view name matches. The hybrid combines both strengths.

**Brute-force cosine similarity** is used rather than an approximate nearest-neighbour index. At 6,000 vectors of 1024 dimensions, a full scan completes in under 100ms, so a dedicated vector database is unnecessary.

---

## Output Formats

### SQLite (`oracle_docs.db`)

The primary output. Schema:

```sql
CREATE TABLE chunks (
    id              TEXT PRIMARY KEY,   -- version__type__name
    name            TEXT,               -- DBA_SEGMENTS, DBMS_STATS.GATHER_TABLE_STATS
    object_type     TEXT,               -- data_dictionary_view | plsql_procedure | ...
    oracle_version  TEXT,               -- 19c, 21c, 23ai
    doc_type        TEXT,               -- database_reference | plsql_packages
    parent          TEXT,               -- Package name for subprograms
    category        TEXT,               -- storage | performance | security | ...
    description     TEXT,
    columns_json    TEXT,               -- JSON array of column dicts
    parameters_json TEXT,               -- JSON array of parameter dicts
    return_type     TEXT,
    syntax          TEXT,
    usage_notes     TEXT,
    source_file     TEXT,
    source_url      TEXT,
    tags_json       TEXT,
    column_names    TEXT,               -- Space-separated column names (for FTS5)
    param_names     TEXT                -- Space-separated param names (for FTS5)
);

CREATE VIRTUAL TABLE chunks_fts USING fts5(
    name, description, column_names, param_names, usage_notes,
    content='chunks', content_rowid='rowid'
);

CREATE TABLE embeddings (
    chunk_id    TEXT PRIMARY KEY,
    model       TEXT,
    vector      BLOB,                   -- float32 packed, 1024 dimensions
    dimensions  INTEGER,
    embed_text  TEXT,
    created_at  TEXT
);
```

### JSONL (`chunks.jsonl`)

One JSON object per line. Each object contains all fields from the `chunks` table with `columns` and `parameters` as arrays rather than JSON strings.

### Markdown (`md/`)

One `.md` file per chunk with YAML front-matter containing all metadata fields, followed by a rendered description, columns table, syntax block, and notes section.

---

## Troubleshooting

**`No module named 'oracle_rag'`**

The package is not installed or not on the Python path. Run `pip install -e . --break-system-packages` from the project root, or ensure `oracle_rag/` is in the same directory as the `oracle-rag` script.

**`No such table: chunks_fts`**

An old database exists at the output path that predates the FTS5 schema. Delete it and re-run the scraper:

```bash
rm output/19c/data-dictionary/oracle_docs.db
python data_dictionary_scraper.py ...
```

**`No results found`**

Check that the databases are configured correctly:

```bash
./oracle-rag stats
```

If stats shows 0 chunks, the database path is wrong. If stats shows chunks but search returns nothing, try a simpler query or use `--show-prompt` to inspect what context is being retrieved.

**Hybrid search not activating**

The `[hybrid vector+FTS5 search]` message appears on stderr when hybrid is active. If you see `[FTS5 keyword search]` instead, either:
- Embeddings have not been generated yet — run `oracle-rag embed`
- `--ollama-url` was not provided to `ask` or `search`
- The embeddings table exists but is empty

**LLM uses wrong column names despite correct context**

Use `--show-prompt` to verify the correct view and columns appear in the context. If they do, the model is ignoring them — try `--limit 3` to reduce noise (fewer irrelevant chunks can improve adherence), or rephrase the question more specifically.

**Slow embedding indexing**

Reduce `--batch-size` if the Ollama server is returning timeout errors. Increase it (up to 64) if the server is lightly loaded and you want faster throughput.

**`Connection refused` on Ollama host**

Ollama listens on `127.0.0.1:11434` by default. To allow remote access, set:

```bash
OLLAMA_HOST=0.0.0.0 ollama serve
```

or add it to the Ollama systemd service environment.
