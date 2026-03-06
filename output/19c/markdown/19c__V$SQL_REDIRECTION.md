---
id: 19c__V$SQL_REDIRECTION
name: V$SQL_REDIRECTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_REDIRECTION.html
---

# V$SQL_REDIRECTION

V$SQL_REDIRECTION displays SQL statements that are redirected.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| PARENT_HANDLE | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| PARSING_USER_ID | NUMBER |  |
| PARSING_SCHEMA_ID | NUMBER |  |
| COMMAND_TYPE | NUMBER |  |
| REASON | VARCHAR2(14) |  |
| ERROR_CODE | NUMBER |  |
| POSITION | NUMBER |  |
| SQL_TEXT_PIECE | VARCHAR2(1000) |  |
| ERROR_MESSAGE | VARCHAR2(1000) |  |
| CON_ID | NUMBER |  |