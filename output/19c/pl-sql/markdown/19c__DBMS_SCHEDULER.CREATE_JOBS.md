---
id: 19c__DBMS_SCHEDULER.CREATE_JOBS
name: DBMS_SCHEDULER.CREATE_JOBS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.CREATE_JOBS

This procedure creates multiple jobs and sets the values of their arguments in a single call.

## Syntax

```sql
DBMS_SCHEDULER.CREATE_JOBS (
   jobdef_array      IN SYS.JOB_DEFINITION_ARRAY,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobdef_array | SYS.JOB_DEFINITION_ARRAY | IN | The array of job definitions. See " Data Structures " for a description of the JOB_DEFINITION_ARRAY and JOB_DEFINITION datatypes. |
| commit_semantics | VARCHAR2 | IN | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error. Previous successfully created jobs are committed to disk. This is the default. TRANSACTIONAL returns on the first error and everything that happened before that error is rolled back. ABSORB_ERRORS tries to absorb any errors and attempts to create the rest of the jobs on the list. It commits all successfully created jobs. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. |

## Usage Notes

Syntax DBMS_SCHEDULER.CREATE_JOBS ( jobdef_array IN SYS.JOB_DEFINITION_ARRAY, commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR'); Parameters Table 151-30 CREATE_JOBS Procedure Parameters Parameter Description jobdef_array The array of job definitions. See " Data Structures " for a description of the JOB_DEFINITION_ARRAY and JOB_DEFINITION datatypes. commit_semantics The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error. Previous successfully created jobs are committed to disk. This is the default. TRANSACTIONAL returns on the first error and everything that happened before that error is rolled back. ABSORB_ERRORS tries to absorb any errors and attempts to create the rest of the jobs on the list. It commits all successfully created jobs. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. Usage Notes This procedure creates many jobs in the context of a single transaction. To realize the desired performance gains, the jobs being created must be grouped in batches of sufficient size. Calling CREATE_JOBS with a small array size may not be much faster than calling CREATE_JOB once for each job. You cannot use this procedure to create multiple-destination jobs. That is, the destination attribute of the job_definition object cannot reference a destination group. Examples See Oracle Database Administrator's Guide .