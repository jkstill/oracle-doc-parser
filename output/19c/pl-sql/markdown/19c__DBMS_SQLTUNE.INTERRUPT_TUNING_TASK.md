---
id: 19c__DBMS_SQLTUNE.INTERRUPT_TUNING_TASK
name: DBMS_SQLTUNE.INTERRUPT_TUNING_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.INTERRUPT_TUNING_TASK

This procedure interrupts the currently executing tuning task. The task ends its operations as it would at normal exit so that the user can access the intermediate results.

## Syntax

```sql
DBMS_SQLTUNE.INTERRUPT_TUNING_TASK (
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the tuning task to interrupt |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.INTERRUPT_TUNING_TASK ( task_name IN VARCHAR2); Parameters Table 169-25 INTERRUPT_TUNING_TASK Procedure Parameters Parameter Description task_name Name of the tuning task to interrupt Examples EXEC DBMS_SQLTUNE.INTERRUPT_TUNING_TASK(:my_task);