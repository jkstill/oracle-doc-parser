---
id: 19c__V$SQL_WORKAREA
name: V$SQL_WORKAREA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_WORKAREA.html
---

# V$SQL_WORKAREA

You can use this view to find out answers to the following questions:

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| CHILD_NUMBER | NUMBER |  |
| WORKAREA_ADDRESS | RAW(4 | 8) |  |
| OPERATION_TYPE | VARCHAR2(160) |  |
| OPERATION_ID | NUMBER |  |
| POLICY | VARCHAR2(40) |  |
| ESTIMATED_OPTIMAL_SIZE | NUMBER |  |
| ESTIMATED_ONEPASS_SIZE | NUMBER |  |
| LAST_MEMORY_USED | NUMBER |  |
| LAST_EXECUTION | VARCHAR2(40) |  |
| LAST_DEGREE | NUMBER |  |
| TOTAL_EXECUTIONS | NUMBER |  |
| OPTIMAL_EXECUTIONS | NUMBER |  |
| ONEPASS_EXECUTIONS | NUMBER |  |
| MULTIPASSES_EXECUTIONS | NUMBER |  |
| ACTIVE_TIME | NUMBER |  |
| MAX_TEMPSEG_SIZE | NUMBER |  |
| LAST_TEMPSEG_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content You can use this view to find out answers to the following questions: What are the top 10 work areas that require the most cache area? For work areas allocated in AUTO mode, what percentage of work areas are running using maximum memory? See Also: " V$SQLAREA " " V$SQL " See Also: " V$SQLAREA " " V$SQL "