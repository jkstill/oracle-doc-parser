---
id: 19c__DBMS_PARALLEL_EXECUTE.GET_NUMBER_COL_CHUNK
name: DBMS_PARALLEL_EXECUTE.GET_NUMBER_COL_CHUNK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.GET_NUMBER_COL_CHUNK

This procedure picks an unassigned NUMBER chunk and changes it to ASSIGNED . If there are no more chunks to assign, any_rows is set to FALSE . Otherwise, the chunk_id , start , and end _id of the chunk are returned as OUT parameters.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.GET_NUMBER_COL_CHUNK (
   task_name       IN VARCHAR2,
   chunk_id        OUT NUMBER,
   start_rowid     OUT ROWID,      
   end_id          OUT ROWID,
   any_rows        OUT BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task |
| chunk_id | NUMBER | OUT | Chunk_id of the chunk |
| start_rowid | ROWID | OUT | Start rowid in the returned range |
| end_id | ROWID | OUT | End rowid in the returned range |
| any_rows | BOOLEAN) | OUT | Indicating if there could be any rows to process in the range |

## Usage Notes

The chunk information in DBMS_PARALLEL_EXECUTE_CHUNKS$ is updated as follows: STATUS becomes ASSIGNED ; START_TIMESTAMP records the current time; END_TIMESTAMP is cleared. See Also: Views Syntax DBMS_PARALLEL_EXECUTE.GET_NUMBER_COL_CHUNK ( task_name IN VARCHAR2, chunk_id OUT NUMBER, start_rowid OUT ROWID, end_id OUT ROWID, any_rows OUT BOOLEAN); Parameters Table 121-16 GET_NUMBER_COL_CHUNK Procedure Parameters Parameter Description task_name Name of the task chunk_id Chunk_id of the chunk start_rowid Start rowid in the returned range end_id End rowid in the returned range any_rows Indicating if there could be any rows to process in the range Usage Notes If the task is chunked by ROWID , then use get_rowid_range . If the task is chunked by NUMBER column, then use get_number_col_range . If you make the wrong function call, the returning chunk_id and any_rows have valid values but start_id and end_id are NULL .