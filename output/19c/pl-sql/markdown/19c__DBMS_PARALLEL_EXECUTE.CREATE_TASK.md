---
id: 19c__DBMS_PARALLEL_EXECUTE.CREATE_TASK
name: DBMS_PARALLEL_EXECUTE.CREATE_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.CREATE_TASK

This procedure creates a task for the current user. The pairing of task_name and current_user must be unique.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.CREATE_TASK (
   task_name        IN   VARCHAR2,
   comment          IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task. The task_name can be any string in which related length must be less than or equal to 128 bytes. |
| comment | VARCHAR2 | IN | Comment field. The comment must be less than 4000 bytes. |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.CREATE_TASK ( task_name IN VARCHAR2, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 121-9 CREATE_TASK Procedure Parameters Parameter Description task_name Name of the task. The task_name can be any string in which related length must be less than or equal to 128 bytes. comment Comment field. The comment must be less than 4000 bytes.