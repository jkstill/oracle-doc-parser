---
id: 19c__DBMS_SQLPA.DROP_ANALYSIS_TASK
name: DBMS_SQLPA.DROP_ANALYSIS_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.DROP_ANALYSIS_TASK

This procedure drops a SQL analysis task.The task and all its result data are deleted.

## Syntax

```sql
DBMS_SQLPA.DROP_ANALYSIS_TASK(
 task_name         IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | The name of the analysis task to drop |

## Usage Notes

Syntax DBMS_SQLPA.DROP_ANALYSIS_TASK( task_name IN VARCHAR2); Parameters Table 166-4 DROP_ANALYSIS_TASK Procedure Parameters Parameter Description task_name The name of the analysis task to drop