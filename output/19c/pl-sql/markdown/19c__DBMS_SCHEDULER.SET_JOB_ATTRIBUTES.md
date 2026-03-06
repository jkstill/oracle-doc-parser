---
id: 19c__DBMS_SCHEDULER.SET_JOB_ATTRIBUTES
name: DBMS_SCHEDULER.SET_JOB_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.SET_JOB_ATTRIBUTES

This procedure changes an attribute of a job.

## Syntax

```sql
DBMS_SCHEDULER.SET_JOB_ATTRIBUTES (
   jobattr_array     IN JOBATTR_ARRAY,
   commit_semantics  IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobattr_array | JOBATTR_ARRAY | IN | The array of job attribute changes. |
| commit_semantics | VARCHAR2 | IN | The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error and commits previous successful attribute changes to disk. This is the default. TRANSACTIONAL returns on the first error and rolls back everything that happened before that error. ABSORB_ERRORS tries to absorb any errors and complete the rest of the job attribute changes on the list. It commits all the successful changes. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. |

## Usage Notes

Syntax DBMS_SCHEDULER.SET_JOB_ATTRIBUTES ( jobattr_array IN JOBATTR_ARRAY, commit_semantics IN VARCHAR2 DEFAULT 'STOP_ON_FIRST_ERROR'); Parameters Table 151-99 SET_JOB_ATTRIBUTES Procedure Parameters Parameter Description jobattr_array The array of job attribute changes. commit_semantics The commit semantics. The following types are supported: STOP_ON_FIRST_ERROR returns on the first error and commits previous successful attribute changes to disk. This is the default. TRANSACTIONAL returns on the first error and rolls back everything that happened before that error. ABSORB_ERRORS tries to absorb any errors and complete the rest of the job attribute changes on the list. It commits all the successful changes. If errors occur, you can query the view SCHEDULER_BATCH_ERRORS for details. Usage Notes Calling SET_ATTRIBUTE on an enabled job disables the job, changes the attribute value, and reenables the job. SET_JOB_ATTRIBUTES changes the attribute values in the context of a single transaction.