---
id: 19c__DBMS_SQLPA.CANCEL_ANALYSIS_TASK
name: DBMS_SQLPA.CANCEL_ANALYSIS_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.CANCEL_ANALYSIS_TASK

This procedure cancels the currently executing analysis task. All intermediate result data is removed from the task.

## Syntax

```sql
DBMS_SQLPA.CANCEL_ANALYSIS_TASK(
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task to cancel |

## Usage Notes

Syntax DBMS_SQLPA.CANCEL_ANALYSIS_TASK( task_name IN VARCHAR2); Parameters Table 166-2 CANCEL_ANALYSIS_TASK Procedure Parameters Parameter Description task_name Name of the task to cancel Examples Canceling a task when there is a need to stop it executing and it is not required to view any already-completed results: EXEC DBMS_SQLPA.CANCEL_ANALYSIS_TASK(:my_task);