---
id: 19c__DBA_AUTOTASK_CLIENT_HISTORY
name: DBA_AUTOTASK_CLIENT_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTOTASK_CLIENT_HISTORY.html
---

# DBA_AUTOTASK_CLIENT_HISTORY

DBA_AUTOTASK_CLIENT_HISTORY displays per-window history of job execution counts for each automated maintenance task.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT_NAME | VARCHAR2(64) | Name of the client |
| WINDOW_NAME | VARCHAR2(261) | Name of the maintenance window |
| WINDOW_START_TIME | TIMESTAMP(6) WITH TIME ZONE | Maintenance window start time |
| WINDOW_DURATION | INTERVAL DAY(9) TO SECOND(6) | Window duration (NULL for currently open window) |
| JOBS_CREATED | NUMBER | Number of jobs created on behalf of the client in this window |
| JOBS_STARTED | NUMBER | Number of jobs started on behalf of the client during the maintenance window |
| JOBS_COMPLETED | NUMBER | Number of jobs successfully completed on behalf of the client during the maintenance window |
| WINDOW_END_TIME | TIMESTAMP(6) WITH TIME ZONE | Window end time |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This information is viewable in the Job History page of Enterprise Manager.