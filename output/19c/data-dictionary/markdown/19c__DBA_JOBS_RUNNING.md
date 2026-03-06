---
id: 19c__DBA_JOBS_RUNNING
name: DBA_JOBS_RUNNING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_JOBS_RUNNING.html
---

# DBA_JOBS_RUNNING

DBA_JOBS_RUNNING lists all jobs that are currently running in the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER | Identifier of process that is executing the job. See " V$LOCK " . |
| JOB | NUMBER | Identifier of job. This job is currently executing. |
| FAILURES | NUMBER | Number of times this job started and failed since its last success. |
| LAST_DATE | DATE | Date that this job last successfully executed. |
| LAST_SEC | VARCHAR2(8) | Same as LAST_DATE . This is when the last successful execution started. |
| THIS_DATE | DATE | Date that this job started executing. |
| THIS_SEC | VARCHAR2(8) | Same as THIS_DATE . This is when the last successful execution started. |
| INSTANCE | NUMBER | Indicates which instance can execute or is executing the job; the default is 0 . |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content