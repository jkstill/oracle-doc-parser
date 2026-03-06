---
id: 19c__DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_NUMBER_COL
name: DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_NUMBER_COL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_NUMBER_COL

This procedure chunks the table (associated with the specified task) by the specified column. The specified column must be a NUMBER column. This procedure takes the MIN and MAX value of the column, and then divides the range evenly according to chunk_size .

## Syntax

```sql
START_ID                              END_ID
---------------------------           ---------------------------
min_id_val                            min_id_val+1*chunk_size-1
min_id_val+1*chunk_size               min_id_val+2*chunk_size-1
…                                     …
min_id_val+i*chunk_size               max_id_val
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name |  |  | Name of the task |
| table_owner |  |  | Owner of the table |
| table_name |  |  | Name of the table |
| table_column |  |  | Name of the NUMBER column |
| chunk_size | min_id_val | IN | Range of each chunk |

## Usage Notes

The chunks are: START_ID END_ID --------------------------- --------------------------- min_id_val min_id_val+1*chunk_size-1 min_id_val+1*chunk_size min_id_val+2*chunk_size-1 … … min_id_val+i*chunk_size max_id_val Syntax DBMS_PARALLEL_EXECUTE.CREATE_CHUNKS_BY_NUMBER_COL ( task_name IN VARCHAR2, table_owner IN VARCHAR2, table_name IN VARCHAR2, table_column IN VARCHAR2, chunk_size IN NUMBER); Parameters Table 121-10 CREATE_CHUNKS_BY_NUMBER_COL Procedure Parameters Parameter Description task_name Name of the task table_owner Owner of the table table_name Name of the table table_column Name of the NUMBER column chunk_size Range of each chunk