---
id: 19c__DBMS_PARALLEL_EXECUTE.ADM_DROP_CHUNKS
name: DBMS_PARALLEL_EXECUTE.ADM_DROP_CHUNKS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.ADM_DROP_CHUNKS

This procedure drops all chunks of the specified task owned by the specified owner.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.ADM_DROP_CHUNKS (
   task_owner      IN  VARCHAR2,
   task_name       IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_owner | VARCHAR2 | IN | Owner of the task |
| task_name | VARCHAR2) | IN | Name of the task |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.ADM_DROP_CHUNKS ( task_owner IN VARCHAR2, task_name IN VARCHAR2); Parameters Table 121-5 ADM_DROP_CHUNKS Procedure Parameters Parameter Description task_owner Owner of the task task_name Name of the task