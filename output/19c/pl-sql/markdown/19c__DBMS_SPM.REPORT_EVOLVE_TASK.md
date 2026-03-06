---
id: 19c__DBMS_SPM.REPORT_EVOLVE_TASK
name: DBMS_SPM.REPORT_EVOLVE_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.REPORT_EVOLVE_TASK

The procedure displays the results of an evolved task.

## Syntax

```sql
DBMS_SPM.REPORT_EVOLVE_TASK  (
   task_name       IN  VARCHAR2,
   type            IN  VARCHAR2  := TYPE_TEXT,
   level           IN  VARCHAR2  := LEVEL_TYPICAL,
   section         IN  VARCHAR2  := SECTION_ALL,
   object_id       IN  NUMBER    := NULL,
   task_owner      IN  VARCHAR2  := NULL,
   execution_name  IN  VARCHAR2  := NULL)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Identifier of task to report |
| type | VARCHAR2 | IN | Type of the report. Possible values are TEXT , HTML , XML |
| level | VARCHAR2 | IN | Format of the report. Possible values are BASIC , TYPICAL , ALL . |
| section | VARCHAR2 | IN | Particular section in the report. Possible values are: SUMMARY , FINDINGS , PLANS , INFORMATION , ERRORS , ALL . |
| object_id | NUMBER | IN | Identifier of the advisor framework object that represents a single plan. If NULL , the report is generated for all objects. |
| task_owner | VARCHAR2 | IN | Owner of the evolve task. Defaults to the current schema owner. |
| execution_name | VARCHAR2 | IN | Name to qualify and identify an execution. If NULL , the report is generated for the last task execution. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_SPM.REPORT_EVOLVE_TASK ( task_name IN VARCHAR2, type IN VARCHAR2 := TYPE_TEXT, level IN VARCHAR2 := LEVEL_TYPICAL, section IN VARCHAR2 := SECTION_ALL, object_id IN NUMBER := NULL, task_owner IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL) RETURN CLOB; Parameters Table 161-26 REPORT_EVOLVE_TASK Function Parameters Parameter Description task_name Identifier of task to report type Type of the report. Possible values are TEXT , HTML , XML level Format of the report. Possible values are BASIC , TYPICAL , ALL . section Particular section in the report. Possible values are: SUMMARY , FINDINGS , PLANS , INFORMATION , ERRORS , ALL . object_id Identifier of the advisor framework object that represents a single plan. If NULL , the report is generated for all objects. task_owner Owner of the evolve task. Defaults to the current schema owner. execution_name Name to qualify and identify an execution. If NULL , the report is generated for the last task execution. Return Values The report