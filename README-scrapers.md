# Oracle Docs RAG Scraper

Parses local Oracle HTML documentation and produces structured chunks
suitable for RAG (Retrieval-Augmented Generation) pipelines.

## Supported Doc Types

| Doc Type | Oracle Manual | Extracts |
|---|---|---|
| `database_reference` | Database Reference (refrn) | Data dictionary views: DBA_*, ALL_*, USER_*, V$*, GV$*, CDB_* |
| `plsql_packages` | PL/SQL Packages and Types Reference (arpls) | Package subprograms with parameters, syntax, return types |

## Setup

```bash
pip install -r requirements.txt
```


## Parse 19c Data Dictionary Reference

```bash
python data_dictionary_test_scraper.py \
    --path /mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn \
    --version 19c \
    --doctype database_reference \
    --output ./output/19c/data-dictionary/

python data_dictionary_scraper.py \
    --path /mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/refrn \
    --version 19c \
    --doctype database_reference \
    --output ./output/19c/data-dictionary/
```

## Parse 19c PL/SQL Language Reference

```bash

python plsql_scraper.py \
    --path /mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/arpls \
    --version 19c \
    --doctype plsql_packages \
    --output ./output/19c/pl-sql

python plsql_scraper.py \
    --path /mnt/zips/zips/oracle/oracle_docs/19c-all-docs/oracle-database_19_20230703/content/arpls \
    --version 19c \
    --doctype plsql_packages \
    --output ./output/19c/pl-sql
    --max-files 20 \
    --verbose
```

## Output

Three output formats are produced by default, all in `--output` directory:

### 1. `oracle_docs.jsonl`
One JSON object per line, one chunk per object. Each chunk has:
```json
{
  "id": "19c__DBA_SEGMENTS",
  "name": "DBA_SEGMENTS",
  "object_type": "data_dictionary_view",
  "oracle_version": "19c",
  "doc_type": "database_reference",
  "parent": null,
  "category": "storage",
  "description": "DBA_SEGMENTS describes storage allocated for all segments...",
  "columns": [
    {"name": "OWNER", "type": "VARCHAR2(128)", "description": "Username of the segment owner"},
    ...
  ],
  "parameters": [],
  "return_type": null,
  "syntax": null,
  "usage_notes": "...",
  "source_file": "refrn20241.htm",
  "source_url": "file:///opt/oracle/docs/19c/refrn/refrn20241.htm",
  "tags": ["dba"]
}
```

### 2. `markdown/` directory
One `.md` file per chunk with YAML front-matter (for embedding pipelines
that accept Markdown with metadata, e.g. LlamaIndex, LangChain).

```markdown
---
id: 19c__DBA_SEGMENTS
name: DBA_SEGMENTS
object_type: data_dictionary_view
oracle_version: 19c
category: storage
tags: [dba]
---

# DBA_SEGMENTS

DBA_SEGMENTS describes storage allocated for all segments...

## Columns
| Column | Type | Description |
|--------|------|-------------|
| OWNER  | VARCHAR2(128) | Username of segment owner |
...
```

### 3. `oracle_docs.db` — SQLite with FTS5
Schema:
- `chunks` table — full structured data, one row per chunk
- `chunks_fts` virtual table — full-text search over name, description, columns, parameters, notes

Example queries:
```sql
-- Find all DBA_ views about segments
SELECT name, description FROM chunks
WHERE object_type = 'data_dictionary_view'
  AND name LIKE 'DBA_%'
  AND oracle_version = '19c'
  AND category = 'storage';

-- Full-text search
SELECT name, description FROM chunks_fts
WHERE chunks_fts MATCH 'redo log sequence';

-- All subprograms in DBMS_STATS
SELECT name, return_type, parameters_json FROM chunks
WHERE parent = 'DBMS_STATS'
  AND oracle_version = '19c'
ORDER BY name;
```

## Doc Type Detection (`--doctype all`)

When `--doctype all` is used, each HTML file is classified by:
1. Directory name patterns (`refrn`, `arpls`, etc.)
2. Content sniffing (presence of DBA_/V$ patterns or DBMS_/PROCEDURE keywords)

For best results, point `--path` at a directory that contains only one doc type,
and specify `--doctype` explicitly.

## Oracle Docs Directory Structure

Oracle downloads typically look like:
```
/opt/oracle/docs/
├── 19c/
│   ├── refrn/          ← Database Reference  → --doctype database_reference
│   │   ├── refrn20001.htm
│   │   └── ...
│   └── arpls/          ← PL/SQL Packages     → --doctype plsql_packages
│       ├── arpls001.htm
│       └── ...
├── 21c/
│   └── ...
└── 23ai/
    └── ...
```

## Tips for RAG Quality

- **Chunk at the view/subprogram level** (already done) — not the whole page.
  This gives retrieval the right granularity.
- **Include column names in the chunk text** — LLMs need column names to write
  correct SELECT/WHERE clauses. The JSONL `columns` array and Markdown table
  both serve this purpose.
- **Filter by `oracle_version` at retrieval time** — mixing 12c and 23ai column
  definitions causes hallucinations of a different kind.
- **Use `category` and `tags` as pre-filters** — e.g. restrict to `storage`
  category when answering questions about tablespace usage.
- **FTS5 + vector hybrid search** — keyword search on view/column names (FTS5)
  combined with semantic vector search on descriptions works well for Oracle
  data dictionary queries.

