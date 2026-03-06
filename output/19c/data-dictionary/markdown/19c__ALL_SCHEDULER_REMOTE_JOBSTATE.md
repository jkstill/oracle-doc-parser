---
id: 19c__ALL_SCHEDULER_REMOTE_JOBSTATE
name: ALL_SCHEDULER_REMOTE_JOBSTATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_SCHEDULER_REMOTE_JOBSTATE.html
---

# ALL_SCHEDULER_REMOTE_JOBSTATE

ALL_SCHEDULER_REMOTE_JOBSTATE displays information about the state of the jobs accessible to the current user at remote databases.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Scheduler job |
| JOB_NAME | VARCHAR2(128) | Name of the Scheduler job |
| DESTINATION | VARCHAR2(512) | Name of the job destination |
| STATE | VARCHAR2(15) | State of the job at the destination: DISABLED RETRY SCHEDULED SCHEDULED RUNNING COMPLETED BROKEN FAILED SUCCEEDED STOPPED |
| NEXT_START_DATE | TIMESTAMP(6) WITH TIME ZONE | Next start date of the job at the destination |
| RUN_COUNT | NUMBER | Run count of the job at the destination |
| FAILURE_COUNT | NUMBER | Failure count of the job at the destination |
| RETRY_COUNT | NUMBER | Retry count of the job at the destination |
| LAST_START_DATE | TIMESTAMP(6) WITH TIME ZONE | Last start date of the job at the destination |
| LAST_END_DATE | TIMESTAMP(6) WITH TIME ZONE | Last end date of the job at the destination |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_REMOTE_JOBSTATE displays information about the state of all jobs at remote databases. USER_SCHEDULER_REMOTE_JOBSTATE displays information about the state of the jobs owned by the current user at remote databases. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_REMOTE_JOBSTATE " " USER_SCHEDULER_REMOTE_JOBSTATE " See Also: " DBA_SCHEDULER_REMOTE_JOBSTATE " " USER_SCHEDULER_REMOTE_JOBSTATE "