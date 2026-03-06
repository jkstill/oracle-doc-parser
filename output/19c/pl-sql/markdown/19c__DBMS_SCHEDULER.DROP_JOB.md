---
id: 19c__DBMS_SCHEDULER.DROP_JOB
name: DBMS_SCHEDULER.DROP_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_JOB

This procedure drops one or more jobs or all jobs in one or more job classes. Dropping a job also drops all argument values set for that job.

## Syntax

```sql
DBMS_SCHEDULER.DROP_JOB (
   job_name                IN VARCHAR2,
   force                   IN BOOLEAN DEFAULT FALSE,
   defer                   IN BOOLEAN DEFAULT FALSE,
   commit_semantics        IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job_name | VARCHAR2 | IN | The name of a job or job class. Can be a comma-delimited list. For a job class, the SYS schema should be specified. If the name of a job class is specified, the jobs that belong to that job class are dropped, but the job class itself is not dropped. |
| force | BOOLEAN | IN | If force is set to TRUE , the Scheduler first attempts to stop the running job instances (by issuing the STOP_JOB call with the force flag set to false ), and then drops the jobs. |
| defer | BOOLEAN | IN | If defer is set to TRUE , the Scheduler allows the running jobs to complete and then drops the jobs. |
| commit_semantics | VARCHAR2 | IN | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error and previous successful drop operations are committed to disk. This is the default. TRANSACTIONAL returns on the first error. Everything that happened before that error is rolled back. This type is not supported when force is set to TRUE . ABSORB_ERRORS tries to absorb any errors and drop the rest of the jobs, and commits all the successful drops. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. Only STOP_ON_FIRST_ERROR is permitted when job classes are included in the job_name list. |

## Usage Notes

Syntax DBMS_SCHEDULER.DROP_JOB ( job_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE, defer IN BOOLEAN DEFAULT FALSE, commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR'); Parameters Table 151-52 DROP_JOB Procedure Parameters Parameter Description job_name The name of a job or job class. Can be a comma-delimited list. For a job class, the SYS schema should be specified. If the name of a job class is specified, the jobs that belong to that job class are dropped, but the job class itself is not dropped. force If force is set to TRUE , the Scheduler first attempts to stop the running job instances (by issuing the STOP_JOB call with the force flag set to false ), and then drops the jobs. defer If defer is set to TRUE , the Scheduler allows the running jobs to complete and then drops the jobs. commit_semantics The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error and previous successful drop operations are committed to disk. This is the default. TRANSACTIONAL returns on the first error. Everything that happened before that error is rolled back. This type is not supported when force is set to TRUE . ABSORB_ERRORS tries to absorb any errors and drop the rest of the jobs, and commits all the successful drops. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. Only STOP_ON_FIRST_ERROR is permitted when job classes are included in the job_name list. Usage Notes If both force and defer are set to FALSE and a job is running at the time of the call, the attempt to drop that job fails. The entire call to DROP_JOB may then fail, depending on the setting of commit_semantics . Setting both force and defer to TRUE results in an error. Dropping a job requires ALTER privileges on the job either as the owner of the job or as a user with the ALTER object privilege on the job or the CREATE ANY JOB system privilege.