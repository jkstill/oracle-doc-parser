---
id: 19c__DBMS_PARALLEL_EXECUTE.TASK_STATUS
name: DBMS_PARALLEL_EXECUTE.TASK_STATUS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.TASK_STATUS

This procedure returns the task status.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.TASK_STATUS (
   task_name       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.TASK_STATUS ( task_name IN VARCHAR2); Parameters Table 121-23 TASK_STATUS Procedure Parameters Parameter Description task_name Name of the task