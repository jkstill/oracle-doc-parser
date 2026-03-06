---
id: 19c__DBMS_STATS.CREATE_ADVISOR_TASK
name: DBMS_STATS.CREATE_ADVISOR_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.CREATE_ADVISOR_TASK

This function creates an advisor task for the Optimizer Statistics Advisor.

## Syntax

```sql
DBMS_STATS.CREATE_ADVISOR_TASK (
   task_name    IN   VARCHAR2   := NULL)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task. If the task name is already specified, then the function uses the specified task name. Otherwise, the function generates a new task name automatically. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_STATS.CREATE_ADVISOR_TASK ( task_name IN VARCHAR2 := NULL) RETURN VARCHAR2; Parameters Table 171-14 CREATE_ADVISOR_TASK Function Parameters Parameter Description task_name Name of the task. If the task name is already specified, then the function uses the specified task name. Otherwise, the function generates a new task name automatically. Security Model Note the following: To execute this subprogram, you must have the ADVISOR privilege. This subprogram executes using invoker's rights. Return Values This function returns the unique name of the Optimizer Statistics Advisor task. Exceptions ORA-20000 : Insufficient privileges / creating extension is not supported ORA-20001 : Error when processing extension ORA-20012 : Optimizer Statistics Advisor errors