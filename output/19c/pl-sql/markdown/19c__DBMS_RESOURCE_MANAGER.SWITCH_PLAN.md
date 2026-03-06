---
id: 19c__DBMS_RESOURCE_MANAGER.SWITCH_PLAN
name: DBMS_RESOURCE_MANAGER.SWITCH_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SWITCH_PLAN

This procedure sets the current resource manager plan.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SWITCH_PLAN(
   plan_name                     IN   VARCHAR2,
   sid                           IN   VARCHAR2 DEFAULT '*',
   allow_scheduler_plan_switches IN   BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan_name | VARCHAR2 | IN | Name of the plan to which to switch. Passing in an empty string ('') for the plan_name , disables the resource manager |
| sid | VARCHAR2 | IN | The sid parameter is relevant only in an Oracle Real Application Clusters environment. This parameter lets you change the plan for a particular instance. Specify the sid of the instance where you want to change the plan. Or specify '*' if you want Oracle to change the plan for all instances. |
| allow_scheduler_plan_switches | BOOLEAN | IN | FALSE - disables automated plan switches by the job scheduler at window boundaries. To reenable automated plan switches, switch_plan must be called again by the administrator with allow_scheduler_plan_switches set to TRUE . By default automated plan switches by the job scheduler are enabled. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.SWITCH_PLAN( plan_name IN VARCHAR2, sid IN VARCHAR2 DEFAULT '*', allow_scheduler_plan_switches IN BOOLEAN DEFAULT TRUE); Parameters Table 142-26 SWITCH_PLAN Procedure Parameters Parameter Description plan_name Name of the plan to which to switch. Passing in an empty string ('') for the plan_name , disables the resource manager sid The sid parameter is relevant only in an Oracle Real Application Clusters environment. This parameter lets you change the plan for a particular instance. Specify the sid of the instance where you want to change the plan. Or specify '*' if you want Oracle to change the plan for all instances. allow_scheduler_plan_switches FALSE - disables automated plan switches by the job scheduler at window boundaries. To reenable automated plan switches, switch_plan must be called again by the administrator with allow_scheduler_plan_switches set to TRUE . By default automated plan switches by the job scheduler are enabled.