---
id: 19c__DBMS_PARALLEL_EXECUTE.PURGE_PROCESSED_CHUNKS
name: DBMS_PARALLEL_EXECUTE.PURGE_PROCESSED_CHUNKS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.PURGE_PROCESSED_CHUNKS

This procedure deletes all the processed chunks whose status is PROCESSED or PROCESSED_WITH_ERROR .

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.PURGE_PROCESSED_CHUNKS (
   task_name       IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task |

## Usage Notes

Syntax DBMS_PARALLEL_EXECUTE.PURGE_PROCESSED_CHUNKS ( task_name IN VARCHAR2); Parameters Table 121-18 PURGE_PROCESSED_CHUNKS Procedure Parameters Parameter Description task_name Name of the task