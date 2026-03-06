---
id: 19c__DBMS_SQLTUNE.REPORT_AUTO_TUNING_TASK
name: DBMS_SQLTUNE.REPORT_AUTO_TUNING_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REPORT_AUTO_TUNING_TASK

This function displays a report from the automatic tuning task.

## Syntax

```sql
DBMS_SQLTUNE.REPORT_AUTO_TUNING_TASK(
    begin_exec     IN VARCHAR2  := NULL,
    end_exec       IN VARCHAR2  := NULL,
    type           IN VARCHAR2  := TYPE_TEXT,
    level          IN VARCHAR2  := LEVEL_TYPICAL,
    section        IN VARCHAR2  := SECTION_ALL,
    object_id      IN NUMBER    := NULL,
    result_limit   IN NUMBER    := NULL)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| begin_exec | VARCHAR2 | IN | Specifies the name of the execution from which to begin the report. NULL retrieves a report on the most recent run. |
| end_exec | VARCHAR2 | IN | Specifies the name of the execution at which to end the report. NULL retrieves a report on the most recent run. |
| type | VARCHAR2 | IN | Specifies the type of the report to produce. Possible values are TYPE_TEXT which produces a text report |
| level | VARCHAR2 | IN | Specifies the level of detail in the report: LEVEL_BASIC : simple version of the report. Just show info about the actions taken by the advisor. LEVEL_TYPICAL : show information about every statement analyzed, including requests not implemented. LEVEL_ALL : highly detailed report level, also provides annotations about statements skipped over. |
| section | VARCHAR2 | IN | Limits the report to a single section ( ALL for all sections): SECTION_SUMMARY - summary information SECTION_FINDINGS - tuning findings SECTION_PLAN - explain plans SECTION_INFORMATION - general information SECTION_ERROR - statements with errors SECTION_ALL - all statements |
| object_id | NUMBER | IN | Specifies the advisor framework object ID that represents a single statement to restrict reporting to. Specify NULL for all statements. Only valid for reports that target a single execution. |
| result_limit | NUMBER | IN | Specifies the maximum number of SQL statements to show in the report. |

**Returns:** `CLOB`

## Usage Notes

This function reports on a range of task executions, whereas the REPORT_TUNING_TASK Function reports on a single execution. Note that this function is deprecated with Oracle Database 11 g Release 2 (11.2) in favor of DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK . See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group REPORT_AUTO_TUNING_TASK Function See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group REPORT_AUTO_TUNING_TASK Function Syntax DBMS_SQLTUNE.REPORT_AUTO_TUNING_TASK( begin_exec IN VARCHAR2 := NULL, end_exec IN VARCHAR2 := NULL, type IN VARCHAR2 := TYPE_TEXT, level IN VARCHAR2 := LEVEL_TYPICAL, section IN VARCHAR2 := SECTION_ALL, object_id IN NUMBER := NULL, result_limit IN NUMBER := NULL) RETURN CLOB; Parameters Table 169-31 REPORT_AUTO_TUNING_TASK Function Parameters Parameter Description begin_exec Specifies the name of the execution from which to begin the report. NULL retrieves a report on the most recent run. end_exec Specifies the name of the execution at which to end the report. NULL retrieves a report on the most recent run. type Specifies the type of the report to produce. Possible values are TYPE_TEXT which produces a text report level Specifies the level of detail in the report: LEVEL_BASIC : simple version of the report. Just show info about the actions taken by the advisor. LEVEL_TYPICAL : show information about every statement analyzed, including requests not implemented. LEVEL_ALL : highly detailed report level, also provides annotations about statements skipped over. section Limits the report to a single section ( ALL for all sections): SECTION_SUMMARY - summary information SECTION_FINDINGS - tuning findings SECTION_PLAN - explain plans SECTION_INFORMATION - general information SECTION_ERROR - statements with errors SECTION_ALL - all statements object_id Specifies the advisor framework object ID that represents a single statement to restrict reporting to. Specify NULL for all statements. Only valid for reports that target a single execution. result_limit Specifies the maximum number of SQL statements to show in the report. Return Values A CLOB containing the desired report.