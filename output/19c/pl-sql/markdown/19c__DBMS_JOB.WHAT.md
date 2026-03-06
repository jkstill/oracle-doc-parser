---
id: 19c__DBMS_JOB.WHAT
name: DBMS_JOB.WHAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.WHAT

This procedure changes what an existing job does, and replaces its environment.

## Syntax

```sql
DBMS_JOB.WHAT ( 
   job       IN  BINARY_INTEGER,
   what      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| what | VARCHAR2) | IN | PL/SQL procedure to run. |

## Usage Notes

Syntax DBMS_JOB.WHAT ( job IN BINARY_INTEGER, what IN VARCHAR2); Parameters Table 94-11 WHAT Procedure Parameters Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. what PL/SQL procedure to run. Usage Notes Your job will not be available for processing by the job queue in the background until it is committed. Some legal values of what (assuming the routines exist) are: 'myproc(''10-JAN-82'', next_date, broken);' 'scott.emppackage.give_raise(''JENKINS'', 30000.00);' 'dbms_job.remove(job);'