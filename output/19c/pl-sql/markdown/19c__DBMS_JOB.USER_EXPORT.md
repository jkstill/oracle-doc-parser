---
id: 19c__DBMS_JOB.USER_EXPORT
name: DBMS_JOB.USER_EXPORT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_JOB
tags: [dbms_job]
source_file: DBMS_JOB.html
---

# DBMS_JOB.USER_EXPORT

There are two overloaded procedures. The first produces the text of a call to re-create the given job. The second alters instance affinity (8 i and after) and preserves the compatibility.

## Syntax

```sql
DBMS_JOB.USER_EXPORT ( 
   job    IN     BINARY_INTEGER,
   mycall IN OUT VARCHAR2);

DBMS_JOB.USER_EXPORT ( 
   job      IN     BINARY_INTEGER,
   mycall   IN OUT VARCHAR2,
   myinst   IN OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| job | BINARY_INTEGER | IN | System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. |
| mycall | VARCHAR2) | IN OUT | Text of a call to re-create the given job. |
| myinst | VARCHAR2) | IN OUT | Text of a call to alter instance affinity. |

## Usage Notes

Syntax DBMS_JOB.USER_EXPORT ( job IN BINARY_INTEGER, mycall IN OUT VARCHAR2); DBMS_JOB.USER_EXPORT ( job IN BINARY_INTEGER, mycall IN OUT VARCHAR2, myinst IN OUT VARCHAR2); Parameters Table 94-10 USER_EXPORT Procedure Parameter Parameter Description job System-assigned ID of the job being run. To find this ID, query the JOB column of the USER_JOBS or DBA_JOBS view. mycall Text of a call to re-create the given job. myinst Text of a call to alter instance affinity.