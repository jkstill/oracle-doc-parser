---
id: 19c__V$MAPPED_SQL
name: V$MAPPED_SQL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-MAPPED_SQL.html
---

# V$MAPPED_SQL

V$MAPPED_SQL lists the SQL statements that are translated and mapped in memory to a different SQL statement for execution.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SQL_TEXT | VARCHAR2(1000) |  |
| SQL_FULLTEXT | CLOB |  |
| SQL_ID | VARCHAR2(13) |  |
| HASH_VALUE | NUMBER |  |
| MAPPED_SQL_TEXT | VARCHAR2(1000) |  |
| MAPPED_SQL_FULLTEXT | CLOB |  |
| MAPPED_SQL_ID | VARCHAR2(13) |  |
| MAPPED_HASH_VALUE | NUMBER |  |
| SQL_TRANSLATION_PROFILE_ID | NUMBER |  |
| CON_ID | NUMBER |  |
| TRANSLATION_TIMESTAMP | DATE |  |
| TRANSLATION_CPU_TIME | NUMBER |  |
| TRANSLATION_ELAPSED_TIME | NUMBER |  |
| TRANSLATION_METHOD | VARCHAR2(10) |  |
| DICTIONARY_SQL_ID | VARCHAR2(13) |  |
| USE_COUNT | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content