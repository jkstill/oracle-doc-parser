---
id: 19c__DBMS_SPM.SET_EVOLVE_TASK_PARAMETER
name: DBMS_SPM.SET_EVOLVE_TASK_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.SET_EVOLVE_TASK_PARAMETER

The procedure sets a parameter of an evolve task, either a VARCHAR2 or a NUMBER .

## Syntax

```sql
DBMS_SPM.SET_EVOLVE_TASK_PARAMETER  (
   task_name     IN  VARCHAR2,
   parameter     IN  VARCHAR2,
   value         IN  NUMBER);

DBMS_SPM.SET_EVOLVE_TASK_PARAMETER  (
   task_name     IN  VARCHAR2  := NULL,
   parameter     IN  VARCHAR2,
   value         IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Evolve task name |
| parameter | VARCHAR2 | IN | Name of the parameter to set (see following table) |
| value | NUMBER) | IN | Value of the parameter (see following table) |

## Usage Notes

Syntax DBMS_SPM.SET_EVOLVE_TASK_PARAMETER ( task_name IN VARCHAR2, parameter IN VARCHAR2, value IN NUMBER); DBMS_SPM.SET_EVOLVE_TASK_PARAMETER ( task_name IN VARCHAR2 := NULL, parameter IN VARCHAR2, value IN VARCHAR2); Parameters Table 161-27 SET_EVOLVE_TASK_PARAMETER Procedure Parameters Parameter Description task_name Evolve task name parameter Name of the parameter to set (see following table) value Value of the parameter (see following table) The following table describes parameters for the SET_EVOLVE_TASK_PARAMETER procedure. Table 161-28 DBMS_SPM.SET_EVOLVE_TASK_PARAMETER Parameters Parameter Description Default alternate_plan_source Determines which sources to search for additional plans: AUTO (the database selects the source automatically) AUTOMATIC_WORKLOAD_REPOSITORY CURSOR_CACHE SQL_TUNING_SET You can combine multiple values with the plus sign ( + ). The default depends on whether the SPM Evolve Advisor task is automated or manual: If automated, the default is AUTO . If manual, the default is CURSOR_CACHE+AUTOMATIC_WORKLOAD_REPOSITORY . alternate_plan_baseline Determines which alternative plans should be loaded: AUTO lets Autonomous Database choose whether to load plans for statements with or without baselines. EXISTING loads alternate plans with for statements with existing baselines. NEW loads alternative plans for statements without a baseline, in which case a new baseline is created. You can combine multiple values with the plus sign ( + ), as in EXISTING+NEW . EXISTING alternate_plan_limit Specifies the maximum number of plans to load in total (that is, not the limit for each SQL statement). The default depends on whether the SPM Evolve Advisor task is automated or manual: If automated, the default is UNLIMITED . If manual, the default is 10 . accept_plans Specifies whether to accept recommended plans automatically. When ACCEPT_PLANS is true , SQL plan management automatically accepts all plans recommended by the task. When ACCEPT_PLANS is false , the task verifies the plans and generates a report of its findings, but does not evolve the plans automatically. You can use a report to identify new SQL plan baselines and accept them manually. true (regardless of whether the advisor is run automatically or manually) time_limit Global time limit in seconds. This is the total time allowed for the task. The default depends on whether the SPM Evolve Advisor task is automated or manual: If automated, the default is 3600 . If manual, the default is 2147483646 . See Also: Oracle Database Licensing Information User Manual for details on which features are supported for different editions and services See Also: Oracle Database Licensing Information User Manual for details on which features are supported for different editions and services