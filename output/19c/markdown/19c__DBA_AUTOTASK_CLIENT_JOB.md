---
id: 19c__DBA_AUTOTASK_CLIENT_JOB
name: DBA_AUTOTASK_CLIENT_JOB
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTOTASK_CLIENT_JOB.html
---

# DBA_AUTOTASK_CLIENT_JOB

DBA_AUTOTASK_CLIENT_JOB displays information about currently running Scheduler jobs created for automated maintenance tasks.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT_NAME | VARCHAR2(64) | Name of the client |
| JOB_NAME | VARCHAR2(65) | Name of the job |
| JOB_SCHEDULER_STATUS | VARCHAR2(15) | Job status: DISABLED RETRY SCHEDULED SCHEDULED RUNNING COMPLETED BROKEN FAILED REMOTE SUCCEEDED CHAIN_STALLED |
| TASK_NAME | VARCHAR2(64) | Name of the task being performed |
| TASK_TARGET_TYPE | VARCHAR2(64) | Type of the target being processed |
| TASK_TARGET_NAME | VARCHAR2(513) | Name of the target |
| TASK_PRIORITY | VARCHAR2(7) | Priority of the task: URGENT HIGH MEDIUM LOW |
| TASK_OPERATION | VARCHAR2(64) | Operation performed on the object |

## Usage Notes

DBA_AUTOTASK_CLIENT_JOB provides information about some objects targeted by those jobs, as well as some additional statistics from previous instantiations of the same task. Some of this additional data is taken from generic Scheduler views.