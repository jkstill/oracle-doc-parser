---
id: 19c__DBMS_SPM.INTERRUPT_EVOLVE_TASK
name: DBMS_SPM.INTERRUPT_EVOLVE_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.INTERRUPT_EVOLVE_TASK

The procedure interrupts a currently executing evolve task. The task ends its operations as at a normal exit and the user can access the intermediate results. The task can be resumed later.

## Syntax

```sql
DBMS_SPM.INTERRUPT_EVOLVE_TASK  (
   task_name        IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Identifier of task to interrupt |

## Usage Notes

Syntax DBMS_SPM.INTERRUPT_EVOLVE_TASK ( task_name IN VARCHAR2); Parameters Table 161-17 INTERRUPT_EVOLVE_TASK Procedure Parameters Parameter Description task_name Identifier of task to interrupt