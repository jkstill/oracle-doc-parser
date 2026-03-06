---
id: 19c__DBMS_JOB.INTERVAL
name: DBMS_JOB.INTERVAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.INTERVAL

This procedure changes how often a job runs.

## Syntax

```sql
DBMS_JOB.INTERVAL ( 
   job       IN  BINARY_INTEGER,
   interval  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| interval | VARCHAR2) | IN | Date function, evaluated immediately before the job starts running. |

## Usage Notes

Syntax DBMS_JOB.INTERVAL ( job IN BINARY_INTEGER, interval IN VARCHAR2); Parameters Table 94-5 INTERVAL Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. interval Date function, evaluated immediately before the job starts running. Usage Notes If the job completes successfully, then this new date is placed in next_date . interval is evaluated by plugging it into the statement select interval into next_date from dual; The interval parameter must evaluate to a time in the future. Legal intervals include: Interval Description 'sysdate + 7' Run once a week. 'next_day(sysdate,''TUESDAY'')' Run once every Tuesday. 'null' Run only once. If interval evaluates to NULL and if a job completes successfully, then the job is automatically deleted from the queue. Your job will not be available for processing by the job queue in the background until it is committed.