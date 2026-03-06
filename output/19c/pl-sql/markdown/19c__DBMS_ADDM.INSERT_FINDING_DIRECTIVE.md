---
id: 19c__DBMS_ADDM.INSERT_FINDING_DIRECTIVE
name: DBMS_ADDM.INSERT_FINDING_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.INSERT_FINDING_DIRECTIVE

This procedure creates a directive to limit reporting of a specific finding type. The directive can be created for a specific task (only when the task is in INITIAL status), or for all subsequently created ADDM tasks (such as a system directive).

## Syntax

```sql
DBMS_ADDM.INSERT_FINDING_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   finding_name          IN VARCHAR2,
   min_active_sessions   IN NUMBER := 0,
   min_perc_impact       IN NUMBER := 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. |
| dir_name | VARCHAR2 | IN | Name of the directive. All directives must be given unique names. |
| finding_name | VARCHAR2 | IN | Name of an ADDM finding to which this directive applies. All valid findings names appear in the NAME column of view DBA_ADVISOR_FINDING_NAMES . |
| min_active_sessions | NUMBER | IN | Minimal number of active sessions for the finding. If a finding has less than this number, it is filtered from the ADDM result. |
| min_perc_impact | NUMBER | IN | Minimal number for the "percent impact" of the finding relative to total database time in the analysis period. If the finding's impact is less than this number, it is filtered from the ADDM result. |

## Usage Notes

Syntax DBMS_ADDM.INSERT_FINDING_DIRECTIVE ( task_name IN VARCHAR2, dir_name IN VARCHAR2, finding_name IN VARCHAR2, min_active_sessions IN NUMBER := 0, min_perc_impact IN NUMBER := 0); Parameters Table 14-16 INSERT_FINDING_DIRECTIVE Procedure Parameters Parameter Description task_name Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. dir_name Name of the directive. All directives must be given unique names. finding_name Name of an ADDM finding to which this directive applies. All valid findings names appear in the NAME column of view DBA_ADVISOR_FINDING_NAMES . min_active_sessions Minimal number of active sessions for the finding. If a finding has less than this number, it is filtered from the ADDM result. min_perc_impact Minimal number for the "percent impact" of the finding relative to total database time in the analysis period. If the finding's impact is less than this number, it is filtered from the ADDM result. Examples A new ADDM task is created to analyze a local instance. However, it has special treatment for 'Undersized SGA' findings. The result of GET_REPORT shows only an 'Undersized SGA' finding if the finding is responsible for at least 2 average active sessions during the analysis period, and this constitutes at least 10% of the total database time during that period. var tname VARCHAR2(60); BEGIN DBMS_ADDM.INSERT_FINDING_DIRECTIVE( NULL, 'Undersized SGA directive', 'Undersized SGA', 2, 10); :tname := 'my_instance_analysis_mode_task'; DBMS_ADDM.ANALYZE_INST(:tname, 1, 2); END; To see a report containing 'Undersized SGA' findings regardless of the directive: SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;