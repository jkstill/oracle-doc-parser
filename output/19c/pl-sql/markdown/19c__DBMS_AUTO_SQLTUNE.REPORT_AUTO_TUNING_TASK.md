---
id: 19c__DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK
name: DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_SQLTUNE
tags: [dbms_auto_sqltune]
source_file: DBMS_AUTO_SQLTUNE.html
---

# DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK

This procedure displays the results of an Automatic SQL Tuning task.

## Syntax

```sql
DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK(
   begin_exec      IN   VARCHAR2   := NULL,
   end_exec        IN   VARCHAR2   := NULL,
   type            IN   VARCHAR2   := 'TEXT',
   level           IN   VARCHAR2   := 'TYPICAL',
   section         IN   VARCHAR2   := ALL,
   object_id       IN   NUMBER     := NULL,
   result_limit    IN   NUMBER     := NULL)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| begin_exec | VARCHAR2 | IN | Name of the beginning task execution to use. If NULL , the report is generated for the most recent task execution. |
| end_exec | VARCHAR2 | IN | Name of the ending task execution to use. If NULL , the report is generated for the most recent task execution. |
| type | VARCHAR2 | IN | Type of the report to produce. Possible values are TEXT which produces a text report. |
| level | VARCHAR2 | IN | Level of detail in the report: BASIC : simple version of the report. Just show info about the actions taken by the advisor. TYPICAL : show information about every statement analyzed, including requests not implemented. ALL : highly detailed report level, also provides annotations about statements skipped over. |
| section | VARCHAR2 | IN | Section of the report to include: SUMMARY : summary information FINDINGS : tuning findings PLAN : explain plans INFORMATION : general information ERROR : statements with errors ALL : all sections |
| object_id | NUMBER | IN | Advisor framework object id that represents a single statement to restrict reporting to. NULL for all statements. Only valid for reports that target a single execution. |
| result_limit | NUMBER | IN | Maximum number of SQL statements to show in the report |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK( begin_exec IN VARCHAR2 := NULL, end_exec IN VARCHAR2 := NULL, type IN VARCHAR2 := 'TEXT', level IN VARCHAR2 := 'TYPICAL', section IN VARCHAR2 := ALL, object_id IN NUMBER := NULL, result_limit IN NUMBER := NULL) RETURN CLOB; Parameters Table 29-3 REPORT_AUTO_TUNING_TASK Function Parameters Parameter Description begin_exec Name of the beginning task execution to use. If NULL , the report is generated for the most recent task execution. end_exec Name of the ending task execution to use. If NULL , the report is generated for the most recent task execution. type Type of the report to produce. Possible values are TEXT which produces a text report. level Level of detail in the report: BASIC : simple version of the report. Just show info about the actions taken by the advisor. TYPICAL : show information about every statement analyzed, including requests not implemented. ALL : highly detailed report level, also provides annotations about statements skipped over. section Section of the report to include: SUMMARY : summary information FINDINGS : tuning findings PLAN : explain plans INFORMATION : general information ERROR : statements with errors ALL : all sections object_id Advisor framework object id that represents a single statement to restrict reporting to. NULL for all statements. Only valid for reports that target a single execution. result_limit Maximum number of SQL statements to show in the report Return Values A CLOB containing the desired report. Examples -- Get the whole report for the most recent execution SELECT DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK FROM DUAL; -- Show the summary for a range of executions SELECT DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK(:begin_exec, :end_exec, 'TEXT', 'TYPICAL', 'SUMMARY') FROM DUAL; -- Show the findings for the statement of interest SELECT DBMS_AUTO_SQLTUNE.REPORT_AUTO_TUNING_TASK(:exec, :exec, 'TEXT', 'TYPICAL', 'FINDINGS', 5) FROM DUAL;