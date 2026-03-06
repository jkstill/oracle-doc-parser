---
id: 19c__V$SQL_SHARED_MEMORY
name: V$SQL_SHARED_MEMORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_SHARED_MEMORY.html
---

# V$SQL_SHARED_MEMORY

SQL text of the shared cursor child object for which this row is displaying information

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SQL_TEXT | VARCHAR2(1000) |  |
| SQL_FULLTEXT | CLOB |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| HEAP_DESC | RAW(4 | 8) |  |
| STRUCTURE | VARCHAR2(64) |  |
| FUNCTION | VARCHAR2(64) |  |
| CHUNK_COM | VARCHAR2(16) |  |
| CHUNK_PTR | RAW(4 | 8) |  |
| CHUNK_SIZE | NUMBER |  |
| ALLOC_CLASS | VARCHAR2(8) |  |
| CHUNK_TYPE | NUMBER |  |
| SUBHEAP_DESC | RAW(4 | 8) |  |
| CON_ID | NUMBER |  |