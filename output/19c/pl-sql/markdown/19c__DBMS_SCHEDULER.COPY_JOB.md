---
id: 19c__DBMS_SCHEDULER.COPY_JOB
name: DBMS_SCHEDULER.COPY_JOB
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.COPY_JOB

This procedure copies all attributes of an existing job to a new job. The new job is created disabled, while the state of the existing job is unaltered.

## Syntax

```sql
DBMS_SCHEDULER.COPY_JOB (
   old_job                IN VARCHAR2,
   new_job                IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| old_job | VARCHAR2 | IN | The name of the existing job |
| new_job | VARCHAR2) | IN | The name of the new job |

## Usage Notes

Syntax DBMS_SCHEDULER.COPY_JOB ( old_job IN VARCHAR2, new_job IN VARCHAR2); Parameters Table 151-20 COPY_JOB Procedure Parameters Parameter Description old_job The name of the existing job new_job The name of the new job Usage Notes To copy a job, you must have privileges to create a job in the schema of the new job (the CREATE JOB system privilege if it is in your own schema, otherwise, the CREATE ANY JOB system privilege). If the old job is not in the your own schema, then you must also have ALTER privileges on the old job or the CREATE ANY JOB system privilege.