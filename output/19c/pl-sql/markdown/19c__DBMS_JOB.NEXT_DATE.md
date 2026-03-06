---
id: 19c__DBMS_JOB.NEXT_DATE
name: DBMS_JOB.NEXT_DATE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.NEXT_DATE

This procedure changes when an existing job next runs.

## Syntax

```sql
DBMS_JOB.NEXT_DATE ( 
   job       IN  BINARY_INTEGER,
   next_date IN  DATE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| next_date | DATE) | IN | Date of the next refresh: it is when the job will be automatically run, assuming there are background processes attempting to run it. |

## Usage Notes

Syntax DBMS_JOB.NEXT_DATE ( job IN BINARY_INTEGER, next_date IN DATE); Parameters Table 94-6 NEXT_DATE Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. next_date Date of the next refresh: it is when the job will be automatically run, assuming there are background processes attempting to run it. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed.