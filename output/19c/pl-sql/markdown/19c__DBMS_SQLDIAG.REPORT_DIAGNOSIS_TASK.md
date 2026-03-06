---
id: 19c__DBMS_SQLDIAG.REPORT_DIAGNOSIS_TASK
name: DBMS_SQLDIAG.REPORT_DIAGNOSIS_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.REPORT_DIAGNOSIS_TASK

This function reports on a diagnostic task. It returns a CLOB containing the desired report.

## Syntax

```sql
DBMS_SQLDIAG.REPORT_DIAGNOSIS_TASK (
    taskname           IN   VARCHAR2,
    type               IN   VARCHAR2  := TYPE_TEXT,
    level              IN   VARCHAR2  := LEVEL_TYPICAL,
    section            IN   VARCHAR2  := SECTION_ALL,
    object_id          IN   NUMBER    := NULL,
    result_limit       IN   NUMBER    := NULL,
    owner_name         IN   VARCHAR2  := NULL)
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| taskname | VARCHAR2 | IN | Name of task to report |
| type | VARCHAR2 | IN | Type of the report. Possible values are: TEXT, HTML, XML (see Table 165-4 ). |
| level | VARCHAR2 | IN | Format of the recommendations. Possible values are TYPICAL, BASIC, ALL ( Table 165-5 ). |
| section | VARCHAR2 | IN | Particular section in the report. Possible values are: SUMMARY, FINDINGS, PLAN, INFORMATION, ERROR, ALL ( Table 165-6 ). |
| object_id | NUMBER | IN | Identifier of the advisor framework object that represents a given statement in a SQL Tuning Set (STS). |
| result_limit | NUMBER | IN | Number of statements in a STS for which the report is generated |
| owner_name | VARCHAR2 | IN | Name of the task execution to use. If NULL , the report will be generated for the last task execution. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_SQLDIAG.REPORT_DIAGNOSIS_TASK ( taskname IN VARCHAR2, type IN VARCHAR2 := TYPE_TEXT, level IN VARCHAR2 := LEVEL_TYPICAL, section IN VARCHAR2 := SECTION_ALL, object_id IN NUMBER := NULL, result_limit IN NUMBER := NULL, owner_name IN VARCHAR2 := NULL) RETURN CLOB; Parameters Table 165-31 REPORT_DIAGNOSIS_TASK Function Parameters Parameter Description taskname Name of task to report type Type of the report. Possible values are: TEXT, HTML, XML (see Table 165-4 ). level Format of the recommendations. Possible values are TYPICAL, BASIC, ALL ( Table 165-5 ). section Particular section in the report. Possible values are: SUMMARY, FINDINGS, PLAN, INFORMATION, ERROR, ALL ( Table 165-6 ). object_id Identifier of the advisor framework object that represents a given statement in a SQL Tuning Set (STS). result_limit Number of statements in a STS for which the report is generated owner_name Name of the task execution to use. If NULL , the report will be generated for the last task execution.