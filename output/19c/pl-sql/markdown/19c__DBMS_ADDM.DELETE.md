---
id: 19c__DBMS_ADDM.DELETE
name: DBMS_ADDM.DELETE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.DELETE

This procedure deletes an already created ADDM task (of any kind). For database analysis mode and partial analysis mode this deletes the local tasks associated with the main task.

## Syntax

```sql
DBMS_ADDM.DELETE (
   task_name           IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Name of the task to be deleted |

## Usage Notes

Syntax DBMS_ADDM.DELETE ( task_name IN VARCHAR2); Parameters Table 14-9 DELETE Procedure Parameters Parameter Description task_name Name of the task to be deleted Examples BEGIN DBMS_ADDM.DELETE ('my_partial_analysis_mode_task'); END