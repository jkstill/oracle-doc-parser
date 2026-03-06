---
id: 19c__DBMS_SPM.RESET_EVOLVE_TASK
name: DBMS_SPM.RESET_EVOLVE_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.RESET_EVOLVE_TASK

This procedure resets an evolve task to its initial state.

## Syntax

```sql
DBMS_SPM.RESET_EVOLVE_TASK  (
   task_name        IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Identifier of task to reset |

## Usage Notes

All intermediate results will be removed from the task. Call this procedure on a task that is not currently executing. Syntax DBMS_SPM.RESET_EVOLVE_TASK ( task_name IN VARCHAR2); Parameters Table 161-23 RESET_EVOLVE_TASK Procedure Parameters Parameter Description task_name Identifier of task to reset