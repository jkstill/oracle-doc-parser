---
id: 19c__DBMS_SPM.IMPLEMENT_EVOLVE_TASK
name: DBMS_SPM.IMPLEMENT_EVOLVE_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.IMPLEMENT_EVOLVE_TASK

The function implements all the actions recommended by an evolve task.

## Syntax

```sql
DBMS_SPM.IMPLEMENT_EVOLVE_TASK  (
   task_name       IN  VARCHAR2,
   task_owner      IN  VARCHAR2  := NULL,
   execution_name  IN  VARCHAR2  := NULL,
   force           IN BOOLEAN    := FALSE)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Identifier of task to report |
| task_owner | VARCHAR2 | IN | Owner of the evolve task. Defaults to the current schema owner. |
| execution_name | VARCHAR2 | IN | Name to qualify and identify an execution. If NULL , the action will be taken for the last task execution. |
| force | BOOLEAN | IN | Accept all plans even if the advisor did not recommend such an action. The default is FALSE requiring acceptance of the plan only if the plan is verified and shows sufficient improvement in benefit. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SPM.IMPLEMENT_EVOLVE_TASK ( task_name IN VARCHAR2, task_owner IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, force IN BOOLEAN := FALSE) RETURN NUMBER; Parameters Table 161-16 IMPLEMENT_EVOLVE_TASK Function Parameters Parameter Description task_name Identifier of task to report task_owner Owner of the evolve task. Defaults to the current schema owner. execution_name Name to qualify and identify an execution. If NULL , the action will be taken for the last task execution. force Accept all plans even if the advisor did not recommend such an action. The default is FALSE requiring acceptance of the plan only if the plan is verified and shows sufficient improvement in benefit. Return Values The number of plans accepted