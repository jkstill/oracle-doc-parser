---
id: 19c__DBMS_SQLTUNE.CANCEL_TUNING_TASK
name: DBMS_SQLTUNE.CANCEL_TUNING_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.CANCEL_TUNING_TASK

This procedure cancels the currently executing tuning task. All intermediate result data is deleted.

## Syntax

```sql
DBMS_SQLTUNE.CANCEL_TUNING_TASK (
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Specifies the name of the task to cancel |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.CANCEL_TUNING_TASK ( task_name IN VARCHAR2); Parameters Table 169-12 CANCEL_TUNING_TASK Procedure Parameters Parameter Description task_name Specifies the name of the task to cancel Examples You cancel a task when you need to stop it executing and do not require to view any already-completed results. EXEC DBMS_SQLTUNE.CANCEL_TUNING_TASK(:my_task);