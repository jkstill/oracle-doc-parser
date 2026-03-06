---
id: 19c__DBMS_SQLTUNE.DROP_TUNING_TASK
name: DBMS_SQLTUNE.DROP_TUNING_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.DROP_TUNING_TASK

This procedure drops a SQL tuning task. The task and all its result data are deleted.

## Syntax

```sql
DBMS_SQLTUNE.DROP_TUNING_TASK (
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Specifies name of the tuning task to drop. |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.DROP_TUNING_TASK ( task_name IN VARCHAR2); Parameters Table 169-22 DROP_TUNING_TASK Procedure Parameters Parameter Description task_name Specifies name of the tuning task to drop.