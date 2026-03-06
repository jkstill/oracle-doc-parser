---
id: 19c__DBMS_PARALLEL_EXECUTE.STOP_TASK
name: DBMS_PARALLEL_EXECUTE.STOP_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.STOP_TASK

This procedure stops the task and related job slaves.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.STOP_TASK (
   task_name       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.STOP_TASK ( task_name IN VARCHAR2); Parameters Table 121-22 STOP_TASK Procedure Parameters Parameter Description task_name Name of the task