---
id: 19c__DBMS_SQLTUNE.RESET_TUNING_TASK
name: DBMS_SQLTUNE.RESET_TUNING_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.RESET_TUNING_TASK

This procedure is called on a tuning task that is not currently executing to prepare it for re-execution.

## Syntax

```sql
DBMS_SQLTUNE.RESET_TUNING_TASK(
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | The name of the tuning task to reset |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.RESET_TUNING_TASK( task_name IN VARCHAR2); Parameters Table 169-37 RESET_TUNING_TASK Procedure Parameters Parameter Description task_name The name of the tuning task to reset Examples -- reset and re-execute a task EXEC DBMS_SQLTUNE.RESET_TUNING_TASK(:sts_task); -- re-execute the task EXEC DBMS_SQLTUNE.EXECUTE_TUNING_TASK(:sts_task);