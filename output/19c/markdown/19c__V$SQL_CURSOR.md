---
id: 19c__V$SQL_CURSOR
name: V$SQL_CURSOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_CURSOR.html
---

# V$SQL_CURSOR

V$SQL_CURSOR displays debugging information for each cursor associated with the session querying this view.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CURNO | NUMBER |  |
| FLAG | NUMBER |  |
| STATUS | VARCHAR2(9) |  |
| PARENT_HANDLE | RAW(4 | 8) |  |
| PARENT_LOCK | RAW(4 | 8) |  |
| CHILD_LOCK | RAW(4 | 8) |  |
| CHILD_PIN | RAW(4 | 8) |  |
| PERS_HEAP_MEM | NUMBER |  |
| WORK_HEAP_MEM | NUMBER |  |
| BIND_VARS | NUMBER |  |
| DEFINE_VARS | NUMBER |  |
| BIND_MEM_LOC | VARCHAR2(64) |  |
| INST_FLAG | VARCHAR2(64) |  |
| INST_FLAG2 | VARCHAR2(64) |  |
| CHILD_HANDLE | RAW(4 | 8) |  |
| CON_ID | NUMBER |  |