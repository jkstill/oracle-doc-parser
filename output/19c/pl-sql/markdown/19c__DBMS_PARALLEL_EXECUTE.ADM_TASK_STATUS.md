---
id: 19c__DBMS_PARALLEL_EXECUTE.ADM_TASK_STATUS
name: DBMS_PARALLEL_EXECUTE.ADM_TASK_STATUS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.ADM_TASK_STATUS

This function returns the task status.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.ADM_TASK_STATUS  (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_owner | VARCHAR2 | IN | Owner of the task |
| task_name | VARCHAR2) | IN | Name of the task |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.ADM_TASK_STATUS ( task_owner IN VARCHAR2, task_name IN VARCHAR2) RETURN NUMBER; Parameters Table 121-7 ADM_TASK_STATUS Function Parameters Parameter Description task_owner Owner of the task task_name Name of the task