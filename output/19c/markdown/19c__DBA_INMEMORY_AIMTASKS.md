---
id: 19c__DBA_INMEMORY_AIMTASKS
name: DBA_INMEMORY_AIMTASKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_INMEMORY_AIMTASKS.html
---

# DBA_INMEMORY_AIMTASKS

DBA_INMEMORY_AIMTASKS displays information about Automatic In-Memory management tasks.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_ID | NUMBER | Number that uniquely identifies a specific automatic IM column store management task |
| CREATION_TIME | TIMESTAMP(6) | Creation time of the task |
| STATE | VARCHAR2(7) | State of the task |

## Usage Notes

See Also: Oracle Database In-Memory Guide for more information about configuring the Automatic In-Memory feature See Also: Oracle Database In-Memory Guide for more information about configuring the Automatic In-Memory feature