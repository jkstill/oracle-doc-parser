---
id: 19c__DBA_PARALLEL_EXECUTE_CHUNKS
name: DBA_PARALLEL_EXECUTE_CHUNKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_PARALLEL_EXECUTE_CHUNKS.html
---

# DBA_PARALLEL_EXECUTE_CHUNKS

DBA_PARALLEL_EXECUTE_CHUNKS displays the chunks for all tasks in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CHUNK_ID | NUMBER | Unique ID for the chunk |
| TASK_OWNER | VARCHAR2(128) | Owner of the task |
| TASK_NAME | VARCHAR2(128) | Name of the task |
| STATUS | VARCHAR2(20) | Status of the chunk: UNASSIGNED ASSIGNED PROCESSED PROCESSED_WITH_ERROR |
| START_ROWID | ROWID | Rowid for the first row in the chunk |
| END_ROWID | ROWID | Rowid for the last row in the chunk |
| START_ID | NUMBER | Number column value of the first row in the chunk |
| END_ID | NUMBER | Number column value of the last row in the chunk |
| JOB_NAME | VARCHAR2(128) | Name of the job which processed this chunk |
| START_TS | TIMESTAMP(6) | Processing start time for the chunk |
| END_TS | TIMESTAMP(6) | Processing end time for the chunk |
| ERROR_CODE | NUMBER | Error code returned during the execution of the chunk if the STATUS column is PROCESSED_WITH_ERROR |
| ERROR_MESSAGE | VARCHAR2(4000) | Error message returned during the execution of the chunk if the STATUS column is PROCESSED_WITH_ERROR |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_PARALLEL_EXECUTE_CHUNKS displays the chunks for tasks created by the current user. This view does not display the TASK_OWNER column. See Also: " USER_PARALLEL_EXECUTE_CHUNKS " See Also: " USER_PARALLEL_EXECUTE_CHUNKS "