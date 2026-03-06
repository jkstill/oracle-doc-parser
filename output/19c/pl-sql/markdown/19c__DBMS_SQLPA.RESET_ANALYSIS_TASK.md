---
id: 19c__DBMS_SQLPA.RESET_ANALYSIS_TASK
name: DBMS_SQLPA.RESET_ANALYSIS_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.RESET_ANALYSIS_TASK

This procedure is called on an analysis task that is not currently executing to prepare it for re-execution.

## Syntax

```sql
DBMS_SQLPA.RESET_ANALYSIS_TASK(
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Identifier of the analysis task to reset |

## Usage Notes

All intermediate result data will be deleted. Syntax DBMS_SQLPA.RESET_ANALYSIS_TASK( task_name IN VARCHAR2); Parameters Table 166-8 RESET_ANALYSIS_TASK Procedure Parameters Parameter Description task_name Identifier of the analysis task to reset Examples -- reset and re-execute a task EXEC DBMS_SQLPA.RESET_ANALYSIS_TASK(:sts_task); -- re-execute the task EXEC DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(:sts_task);