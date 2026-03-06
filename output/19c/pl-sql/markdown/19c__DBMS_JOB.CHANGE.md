---
id: 19c__DBMS_JOB.CHANGE
name: DBMS_JOB.CHANGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.CHANGE

This procedure changes any of the fields a user can set in a job.

## Syntax

```sql
DBMS_JOB.CHANGE ( 
   job       IN  BINARY_INTEGER,
   what      IN  VARCHAR2,
   next_date IN  DATE,
   interval  IN  VARCHAR2,
   instance  IN  BINARY_INTEGER DEFAULT NULL,
   force     IN  BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| what | VARCHAR2 | IN | PL/SQL procedure to run. |
| next_date | DATE | IN | Next date when the job will be run. |
| interval | VARCHAR2 | IN | Date function; evaluated immediately before the job starts running. |
| instance | BINARY_INTEGER | IN | When a job is submitted, specifies which instance can run the job. This defaults to NULL , which indicates that instance affinity is not changed. |
| force | BOOLEAN | IN | If this is FALSE , then the specified instance (to which the instance number change) must be running. Otherwise, the routine raises an exception. If this is TRUE , then any positive integer is acceptable as the job instance. |

## Usage Notes

Syntax DBMS_JOB.CHANGE ( job IN BINARY_INTEGER, what IN VARCHAR2, next_date IN DATE, interval IN VARCHAR2, instance IN BINARY_INTEGER DEFAULT NULL, force IN BOOLEAN DEFAULT FALSE); Parameters Table 94-3 CHANGE Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. what PL/SQL procedure to run. next_date Next date when the job will be run. interval Date function; evaluated immediately before the job starts running. instance When a job is submitted, specifies which instance can run the job. This defaults to NULL , which indicates that instance affinity is not changed. force If this is FALSE , then the specified instance (to which the instance number change) must be running. Otherwise, the routine raises an exception. If this is TRUE , then any positive integer is acceptable as the job instance. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed. The parameters instance and force are added for job queue affinity. Job queue affinity gives users the ability to indicate whether a particular instance or any instance can run a submitted job. If the parameters what , next_date , or interval are NULL , then leave that value as it is. Example BEGIN DBMS_JOB.CHANGE(14144, null, null, 'sysdate+3'); COMMIT; END;