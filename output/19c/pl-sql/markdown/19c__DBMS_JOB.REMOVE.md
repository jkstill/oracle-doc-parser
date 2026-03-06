---
id: 19c__DBMS_JOB.REMOVE
name: DBMS_JOB.REMOVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.REMOVE

This procedure removes an existing job from the job queue. This currently does not stop a running job.

## Syntax

```sql
DBMS_JOB.REMOVE ( 
   job       IN  BINARY_INTEGER );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |

## Usage Notes

Syntax DBMS_JOB.REMOVE ( job IN BINARY_INTEGER ); Parameters Table 94-7 REMOVE Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed. Example BEGIN DBMS_JOB.REMOVE(14144); COMMIT; END;