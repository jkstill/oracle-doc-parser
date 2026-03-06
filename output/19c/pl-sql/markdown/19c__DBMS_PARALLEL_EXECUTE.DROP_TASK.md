---
id: 19c__DBMS_PARALLEL_EXECUTE.DROP_TASK
name: DBMS_PARALLEL_EXECUTE.DROP_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.DROP_TASK

This procedure drops the task and all related chunks.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.DROP_TASK (
   task_name       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.DROP_TASK ( task_name IN VARCHAR2); Parameters Table 121-13 DROP_TASK Procedure Parameters Parameter Description task_name Name of the task