---
id: 19c__DBMS_JOB.INSTANCE
name: DBMS_JOB.INSTANCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.INSTANCE

This procedure changes job instance affinity.

## Syntax

```sql
DBMS_JOB.INSTANCE ( 
   job        IN BINARY_INTEGER,
   instance   IN BINARY_INTEGER,
   force      IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| instance | BINARY_INTEGER | IN | When a job is submitted, a user can specify which instance can run the job. |
| force | BOOLEAN | IN | If this is TRUE , then any positive integer is acceptable as the job instance. If this is FALSE (the default), then the specified instance must be running; otherwise the routine raises an exception. |

## Usage Notes

Syntax DBMS_JOB.INSTANCE ( job IN BINARY_INTEGER, instance IN BINARY_INTEGER, force IN BOOLEAN DEFAULT FALSE); Parameters Table 94-4 INSTANCE Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. instance When a job is submitted, a user can specify which instance can run the job. force If this is TRUE , then any positive integer is acceptable as the job instance. If this is FALSE (the default), then the specified instance must be running; otherwise the routine raises an exception. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed.