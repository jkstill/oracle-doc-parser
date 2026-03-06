---
id: 19c__DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK
name: DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK

This procedure interrupts the currently executing analysis task. All intermediate result data will not be removed from the task.

## Syntax

```sql
DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK(
   task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Identifier of the analysis task to interrupt |

## Usage Notes

Syntax DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK( task_name IN VARCHAR2); Parameters Table 166-6 INTERRUPT_ANALYSIS_TASK Procedure Parameters Parameter Description task_name Identifier of the analysis task to interrupt Examples EXEC DBMS_SQLPA.INTERRUPT_ANALYSIS_TASK(:my_task);