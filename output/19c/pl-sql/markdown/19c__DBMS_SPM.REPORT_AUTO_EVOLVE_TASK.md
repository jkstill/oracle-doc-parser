---
id: 19c__DBMS_SPM.REPORT_AUTO_EVOLVE_TASK
name: DBMS_SPM.REPORT_AUTO_EVOLVE_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.REPORT_AUTO_EVOLVE_TASK

The procedure displays the results of an execution of an automatic evolve task.

## Syntax

```sql
DBMS_SPM.REPORT_AUTO_EVOLVE_TASK  (
   type            IN  VARCHAR2  := TYPE_TEXT,
   level           IN  VARCHAR2  := LEVEL_TYPICAL,
   section         IN  VARCHAR2  := SECTION_ALL,
   object_id       IN  NUMBER    := NULL,
   execution_name  IN  VARCHAR2  := NULL)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| type | VARCHAR2 | IN | Type of the report. Possible values are TEXT , HTML , XML |
| level | VARCHAR2 | IN | Format of the report. Possible values are BASIC , TYPICAL , ALL . |
| section | VARCHAR2 | IN | Particular section in the report. Possible values are: SUMMARY , FINDINGS , PLANS , INFORMATION , ERRORS , ALL . |
| object_id | NUMBER | IN | Identifier of the advisor framework object that represents a single plan. If NULL , the report is generated for all objects. |
| execution_name | VARCHAR2 | IN | Name to qualify and identify an execution. If NULL , the report is generated for the last task execution. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_SPM.REPORT_AUTO_EVOLVE_TASK ( type IN VARCHAR2 := TYPE_TEXT, level IN VARCHAR2 := LEVEL_TYPICAL, section IN VARCHAR2 := SECTION_ALL, object_id IN NUMBER := NULL, execution_name IN VARCHAR2 := NULL) RETURN CLOB; Parameters Table 161-25 REPORT_AUTO_EVOLVE_TASK Function Parameters Parameter Description type Type of the report. Possible values are TEXT , HTML , XML level Format of the report. Possible values are BASIC , TYPICAL , ALL . section Particular section in the report. Possible values are: SUMMARY , FINDINGS , PLANS , INFORMATION , ERRORS , ALL . object_id Identifier of the advisor framework object that represents a single plan. If NULL , the report is generated for all objects. execution_name Name to qualify and identify an execution. If NULL , the report is generated for the last task execution. Return Values The report