---
id: 19c__DBMS_JOB.BROKEN
name: DBMS_JOB.BROKEN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.BROKEN

This procedure sets the broken flag. Broken jobs are never run.

## Syntax

```sql
DBMS_JOB.BROKEN ( 
   job       IN  BINARY_INTEGER,
   broken    IN  BOOLEAN,
   next_date IN  DATE DEFAULT SYSDATE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| broken | BOOLEAN | IN | Sets the job as broken or not broken. TRUE sets it as broken; FALSE sets it as not broken. |
| next_date | DATE | IN | Next date when the job will be run. |

## Usage Notes

Syntax DBMS_JOB.BROKEN ( job IN BINARY_INTEGER, broken IN BOOLEAN, next_date IN DATE DEFAULT SYSDATE); Parameters Table 94-2 BROKEN Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. broken Sets the job as broken or not broken. TRUE sets it as broken; FALSE sets it as not broken. next_date Next date when the job will be run. Note: If you set job as broken while it is running, Oracle resets the job's status to normal after the job completes. Therefore, only execute this procedure for jobs that are not running. Note: If you set job as broken while it is running, Oracle resets the job's status to normal after the job completes. Therefore, only execute this procedure for jobs that are not running. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed. If a job fails 16 times in a row, Oracle automatically sets it as broken and then stops trying to run it.