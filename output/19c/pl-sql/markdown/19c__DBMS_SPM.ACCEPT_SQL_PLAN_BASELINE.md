---
id: 19c__DBMS_SPM.ACCEPT_SQL_PLAN_BASELINE
name: DBMS_SPM.ACCEPT_SQL_PLAN_BASELINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.ACCEPT_SQL_PLAN_BASELINE

The procedure accepts a plan based on the recommendation of an evolve task.

## Syntax

```sql
DBMS_SPM.ACCEPT_SQL_PLAN_BASELINE  (
   task_name       IN  VARCHAR2,
   object_id       IN  NUMBER    := NULL,
   task_owner      IN  VARCHAR2  := NULL,
   force           IN  BOOLEAN   := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Identifier of task to implement |
| object_id | NUMBER | IN | Identifier of the advisor framework object that represents a single plan. If NULL , the report is generated for all objects. |
| task_owner | VARCHAR2 | IN | Owner of the evolve task. Defaults to the current schema owner. |
| force | BOOLEAN | IN | Accept the plan even if the advisor did not recommend such an action. The default is FALSE requiring acceptance of the plan only if the plan is verified and shows sufficient improvement in benefit. |

## Usage Notes

Syntax DBMS_SPM.ACCEPT_SQL_PLAN_BASELINE ( task_name IN VARCHAR2, object_id IN NUMBER := NULL, task_owner IN VARCHAR2 := NULL, force IN BOOLEAN := FALSE); Parameters Table 161-3 ACCEPT_SQL_PLAN_BASELINE Procedure Parameters Parameter Description task_name Identifier of task to implement object_id Identifier of the advisor framework object that represents a single plan. If NULL , the report is generated for all objects. task_owner Owner of the evolve task. Defaults to the current schema owner. force Accept the plan even if the advisor did not recommend such an action. The default is FALSE requiring acceptance of the plan only if the plan is verified and shows sufficient improvement in benefit.