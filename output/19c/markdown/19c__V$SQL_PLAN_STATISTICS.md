---
id: 19c__V$SQL_PLAN_STATISTICS
name: V$SQL_PLAN_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SQL_PLAN_STATISTICS.html
---

# V$SQL_PLAN_STATISTICS

V$SQL_PLAN_STATISTICS provides execution statistics at the row source level for each child cursor.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| PLAN_HASH_VALUE | NUMBER |  |
| FULL_PLAN_HASH_VALUE | NUMBER |  |
| CHILD_ADDRESS | RAW(4 | 8) |  |
| CHILD_NUMBER | NUMBER |  |
| OPERATION_ID | NUMBER |  |
| EXECUTIONS | NUMBER |  |
| LAST_STARTS | NUMBER |  |
| STARTS | NUMBER |  |
| LAST_OUTPUT_ROWS | NUMBER |  |
| OUTPUT_ROWS | NUMBER |  |
| LAST_CR_BUFFER_GETS | NUMBER |  |
| CR_BUFFER_GETS | NUMBER |  |
| LAST_CU_BUFFER_GETS | NUMBER |  |
| CU_BUFFER_GETS | NUMBER |  |
| LAST_DISK_READS | NUMBER |  |
| DISK_READS | NUMBER |  |
| LAST_DISK_WRITES | NUMBER |  |
| DISK_WRITES | NUMBER |  |
| LAST_ELAPSED_TIME | NUMBER |  |
| ELAPSED_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SQLAREA " See Also: " V$SQLAREA "