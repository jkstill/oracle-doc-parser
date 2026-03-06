---
id: 19c__DBMS_SPM.RESUME_EVOLVE_TASK
name: DBMS_SPM.RESUME_EVOLVE_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.RESUME_EVOLVE_TASK

The procedure resumes a previously interrupted task.

## Syntax

```sql
DBMS_SPM.RESUME_EVOLVE_TASK  (
   task_name        IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | Identifier of task to resume |

## Usage Notes

Syntax DBMS_SPM.RESUME_EVOLVE_TASK ( task_name IN VARCHAR2); Parameters Table 161-24 RESUME_EVOLVE_TASK Procedure Parameters Parameter Description task_name Identifier of task to resume