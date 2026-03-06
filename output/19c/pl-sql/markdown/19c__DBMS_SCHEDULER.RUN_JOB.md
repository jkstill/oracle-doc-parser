---
id: 19c__DBMS_SCHEDULER.RUN_JOB
name: DBMS_SCHEDULER.RUN_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.RUN_JOB

This procedure runs a job immediately.

## Syntax

```sql
DBMS_SCHEDULER.RUN_JOB (
   job_name                IN VARCHAR2,
   use_current_session     IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | A job name or a comma-separate list of entries, where each is the name of an existing job, optionally preceded by a schema name and dot separator. If you specify a multiple-destination job, the job runs on all destinations. In this case, the use_current_session argument must be FALSE . |
| use_current_session | BOOLEAN | IN | This specifies whether or not the job run should occur in the same session that the procedure was invoked from.The job always runs as the job owner, in the job owner's schema, unless it has credential specified, then the job runs using the user named in the credential. When use_current_session is set to TRUE : You can test a job and see any possible errors on the command line. state, run_count , last_start_date , last_run_duration , and failure_count of *_scheduler_jobs are not updated. RUN_JOB can be run in parallel with a regularly scheduled job run. When use_current_session is set to FALSE : You need to check the job log to find error information. All relevant fields in *_scheduler_jobs are updated. RUN_JOB fails if a regularly scheduled job is running. For jobs that have a specified destination or destination group, or point to chains or programs with the detached attribute set to TRUE , use_current_session must be FALSE . |

## Usage Notes

If a job is enabled, the Scheduler runs it automatically. It is not necessary to call RUN_JOB to run a job according to its schedule. Use RUN_JOB to run a job outside of its normal schedule. Syntax DBMS_SCHEDULER.RUN_JOB ( job_name IN VARCHAR2, use_current_session IN BOOLEAN DEFAULT TRUE); Parameters Table 151-79 RUN_JOB Procedure Parameters Parameter Description job_name A job name or a comma-separate list of entries, where each is the name of an existing job, optionally preceded by a schema name and dot separator. If you specify a multiple-destination job, the job runs on all destinations. In this case, the use_current_session argument must be FALSE . use_current_session This specifies whether or not the job run should occur in the same session that the procedure was invoked from.The job always runs as the job owner, in the job owner's schema, unless it has credential specified, then the job runs using the user named in the credential. When use_current_session is set to TRUE : You can test a job and see any possible errors on the command line. state, run_count , last_start_date , last_run_duration , and failure_count of *_scheduler_jobs are not updated. RUN_JOB can be run in parallel with a regularly scheduled job run. When use_current_session is set to FALSE : You need to check the job log to find error information. All relevant fields in *_scheduler_jobs are updated. RUN_JOB fails if a regularly scheduled job is running. For jobs that have a specified destination or destination group, or point to chains or programs with the detached attribute set to TRUE , use_current_session must be FALSE . Usage Notes Jobs do not have to be enabled. If a job is disabled, the following validity checks are performed before running it: The job points to a valid job class. The job owner has EXECUTE privileges on the job class. If a program or chain is referenced, the program/chain exists. If a program or chain is referenced, the job owner has privileges to execute the program/chain. All argument values have been set (or have defaults). The job owner has the CREATE EXTERNAL JOB privilege if this is an external job. A TRUE value for use_current_session is not permitted for the following types of jobs: Jobs that specify a destination or destination group in the destination_name attribute Jobs that point to chains (chain jobs) Jobs that make use of detached programs (detached jobs). above bug fix 1261887 6.12.11 When use_current_session is TRUE , the call to RUN_JOB blocks until the job completes. Any errors that occur during the execution of the job are returned as errors to the RUN_JOB procedure. Using RUN_JOB with use_current_session =TRUE does not update the job state and the job will not appear in *_SCHEDULER_RUNNING_JOBS views. above bug fix 19185117 9.15.14 When use_current_session is FALSE , RUN_JOB returns immediately and the job is picked up by the job coordinator and passed on to a job slave for execution. The Scheduler views and logs must be queried for the outcome of the job. Multiple user sessions can use RUN_JOB in their sessions simultaneously when use_current_session is set to TRUE . RUN_JOB requires that you own the job or have ALTER privileges on that job. You can also run a job if you have the CREATE ANY JOB privilege. Example The following is an example of using RUN_JOB . BEGIN DBMS_SCHEDULER.RUN_JOB( JOB_NAME => 'EODJOB, DSS.ETLJOB', USE_CURRENT_SESSION => FALSE); END;