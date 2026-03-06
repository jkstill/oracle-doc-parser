---
id: 19c__DBMS_SCHEDULER.END_DETACHED_JOB_RUN
name: DBMS_SCHEDULER.END_DETACHED_JOB_RUN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.END_DETACHED_JOB_RUN

This procedure ends a detached job run. A detached job points to a detached program, which is a program with the detached attribute set to TRUE .

## Syntax

```sql
DBMS_SCHEDULER.END_DETACHED_JOB_RUN (
   job_name          IN VARCHAR2,
   error_number      IN PLS_INTEGER DEFAULT 0,
   additional_info   IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of the job to end. Must be a detached job that is running. |
| error_number | PLS_INTEGER | IN | If zero, then the job run is logged as succeeded. If -1013, then the job run is logged as stopped. If any other number, then the job run is logged as failed with that error number. |
| additional_info | VARCHAR2 | IN | This text is stored in the additional_info column of the *_scheduler_job_run_details views for this job run. |

## Usage Notes

A detached job run does not end until this procedure or the STOP_JOB Procedure is called. Syntax DBMS_SCHEDULER.END_DETACHED_JOB_RUN ( job_name IN VARCHAR2, error_number IN PLS_INTEGER DEFAULT 0, additional_info IN VARCHAR2 DEFAULT NULL); Parameters Table 151-60 END_DETACHED_JOB_RUN Procedure Parameters Parameter Description job_name The name of the job to end. Must be a detached job that is running. error_number If zero, then the job run is logged as succeeded. If -1013, then the job run is logged as stopped. If any other number, then the job run is logged as failed with that error number. additional_info This text is stored in the additional_info column of the *_scheduler_job_run_details views for this job run. Usage Notes This procedure requires that you either own the job or have ALTER privileges on it. You can also end any detached job run if you have the CREATE ANY JOB privilege. See Also: Oracle Database Administrator's Guide for information about detached jobs.