---
id: 19c__DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS
name: DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS

This procedure sets the status of the chunk.

## Syntax

```sql
Value of the new Status               Side Effect
---------------------------           ---------------------------
UNASSIGNED                            START_TIMESTAMP and END_TIMESTAMP 
                                      will be cleared
ASSIGNED                              START_TIMESTAMP will be the current time 
                                      and END_TIMESTAMP will be cleared.
PROCESSED or PROCESSED_WITH_ERROR     The current time will be recorded 
                                      in END_TIMESTAMP
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name |  |  | Name of the task |
| chunk_id |  |  | Chunk_id of the chunk |
| status | Side | IN | Status of the chunk: UNASSIGNED , ASSIGNED , PROCESSED PROCESSED_WITH_ERROR |
| err_num |  |  | Error code returned during the processing of the chunk |
| err_msg |  |  | Error message returned during the processing of the chunk |

## Usage Notes

The START_TIMESTAMP and END_TIMESTAMP of the chunk is updated according to the new status: Value of the new Status Side Effect --------------------------- --------------------------- UNASSIGNED START_TIMESTAMP and END_TIMESTAMP will be cleared ASSIGNED START_TIMESTAMP will be the current time and END_TIMESTAMP will be cleared. PROCESSED or PROCESSED_WITH_ERROR The current time will be recorded in END_TIMESTAMP See Also: Views Syntax DBMS_PARALLEL_EXECUTE.SET_CHUNK_STATUS ( task_name IN VARCHAR2, chunk_id OUT NUMBER, status IN NUMBER, err_num IN NUMBER DEFAULT NULL, err_msg IN VARCHAR2 DEFAULT NULL); Parameters Table 121-21 SET_CHUNK_STATUS Procedure Parameters Parameter Description task_name Name of the task chunk_id Chunk_id of the chunk status Status of the chunk: UNASSIGNED , ASSIGNED , PROCESSED PROCESSED_WITH_ERROR err_num Error code returned during the processing of the chunk err_msg Error message returned during the processing of the chunk