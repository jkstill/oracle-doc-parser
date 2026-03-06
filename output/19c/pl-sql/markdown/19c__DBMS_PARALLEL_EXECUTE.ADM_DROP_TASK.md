---
id: 19c__DBMS_PARALLEL_EXECUTE.ADM_DROP_TASK
name: DBMS_PARALLEL_EXECUTE.ADM_DROP_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.ADM_DROP_TASK

This procedure drops the task of the specified user and all related chunks.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.ADM_DROP_TASK (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_owner | VARCHAR2 | IN | Owner of the task |
| task_name | VARCHAR2) | IN | Name of the task |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.ADM_DROP_TASK ( task_owner IN VARCHAR2, task_name IN VARCHAR2); Parameters Table 121-6 ADM_DROP_TASK Procedure Parameters Parameter Description task_owner Owner of the task task_name Name of the task