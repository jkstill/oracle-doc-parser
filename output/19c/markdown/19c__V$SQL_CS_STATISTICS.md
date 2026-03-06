---
id: 19c__V$SQL_CS_STATISTICS
name: V$SQL_CS_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SQL_CS_STATISTICS.html
---

# V$SQL_CS_STATISTICS

Address of the handle to the parent for this cursor

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| BIND_SET_HASH_VALUE | NUMBER |  |
| PEEKED | VARCHAR2(1) |  |
| EXECUTIONS | NUMBER |  |
| ROWS_PROCESSED | NUMBER |  |
| BUFFER_GETS | NUMBER |  |
| CPU_TIME | NUMBER |  |
| CON_ID | NUMBER |  |