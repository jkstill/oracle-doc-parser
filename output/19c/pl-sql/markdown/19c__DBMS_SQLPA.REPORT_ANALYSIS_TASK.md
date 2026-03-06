---
id: 19c__DBMS_SQLPA.REPORT_ANALYSIS_TASK
name: DBMS_SQLPA.REPORT_ANALYSIS_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.REPORT_ANALYSIS_TASK

This procedure displays the results of an analysis task.

## Syntax

```sql
DBMS_SQLPA.REPORT_ANALYSIS_TASK(
   task_name       IN   VARCHAR2,
   type            IN   VARCHAR2   := 'TEXT',
   level           IN   VARCHAR2   := 'TYPICAL',
   section         IN   VARCHAR2   := 'SUMMARY',
   object_id       IN   NUMBER     := NULL,
   top_sql         IN   NUMBER     := 100,
   execution_name  IN   VARCHAR2   := NULL,
   task_owner      IN   VARCHAR2   := NULL,
   order_by        IN   VARCHAR2   := NULL)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task to report |
| type | VARCHAR2 | IN | Type of the report to produce. Possible values are TEXT (default), HTML , XML and ACTIVE (see Usage Notes). |
| level | VARCHAR2 | IN | Level of detail in the report: ALL - details of all SQL BASIC - currently the same as typical CHANGED - only SQL with changed performance CHANGED_PLANS - only SQL with plan changes ERRORS - SQL with errors only IMPROVED - only improved SQL REGRESSED - only regressed SQL TIMEOUT - only SQL which timed-out during execution TYPICAL (default) - show information about every statement analyzed, including changing and errors UNCHANGED - only SQL with unchanged performance UNCHANGED_PLANS - only SQL with unchanged plans UNSUPPORTED - only SQL not supported by SPAs |
| section | VARCHAR2 | IN | Optionally limit the report to a single section ( ALL for all sections): SUMMARY (default) - workload summary only ALL - summary and details on SQL |
| object_id | NUMBER | IN | Identifier of the advisor framework object that represents a given SQL in a tuning set (STS) |
| top_sql | NUMBER | IN | Number of SQL statements in a STS for which the report is generated |
| execution_name | VARCHAR2 | IN | Name of the task execution to use. If NULL , the report will be generated for the last task execution. |
| task_owner | VARCHAR2 | IN | Owner of the relevant analysis task. Defaults to the current schema owner. |
| order_by | VARCHAR2 | IN | How to sort SQL statements in the report (summary and body). Possible values: CHANGE_DIFF - sort SQL statements by change difference in SQL performance in terms of the comparison Metric NULL (default) - order SQL statement by impact on workload SQL_IMPACT - order SQL statement by change impact on SQL WORKLOAD_IMPACT - same as NULL METRIC_DELTA - same as CHANGE_DIFF |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_SQLPA.REPORT_ANALYSIS_TASK( task_name IN VARCHAR2, type IN VARCHAR2 := 'TEXT', level IN VARCHAR2 := 'TYPICAL', section IN VARCHAR2 := 'SUMMARY', object_id IN NUMBER := NULL, top_sql IN NUMBER := 100, execution_name IN VARCHAR2 := NULL, task_owner IN VARCHAR2 := NULL, order_by IN VARCHAR2 := NULL) RETURN CLOB; Parameters Table 166-7 REPORT_ANALYSIS_TASK Function Parameters Parameter Description task_name Name of the task to report type Type of the report to produce. Possible values are TEXT (default), HTML , XML and ACTIVE (see Usage Notes). level Level of detail in the report: ALL - details of all SQL BASIC - currently the same as typical CHANGED - only SQL with changed performance CHANGED_PLANS - only SQL with plan changes ERRORS - SQL with errors only IMPROVED - only improved SQL REGRESSED - only regressed SQL TIMEOUT - only SQL which timed-out during execution TYPICAL (default) - show information about every statement analyzed, including changing and errors UNCHANGED - only SQL with unchanged performance UNCHANGED_PLANS - only SQL with unchanged plans UNSUPPORTED - only SQL not supported by SPAs section Optionally limit the report to a single section ( ALL for all sections): SUMMARY (default) - workload summary only ALL - summary and details on SQL object_id Identifier of the advisor framework object that represents a given SQL in a tuning set (STS) top_sql Number of SQL statements in a STS for which the report is generated execution_name Name of the task execution to use. If NULL , the report will be generated for the last task execution. task_owner Owner of the relevant analysis task. Defaults to the current schema owner. order_by How to sort SQL statements in the report (summary and body). Possible values: CHANGE_DIFF - sort SQL statements by change difference in SQL performance in terms of the comparison Metric NULL (default) - order SQL statement by impact on workload SQL_IMPACT - order SQL statement by change impact on SQL WORKLOAD_IMPACT - same as NULL METRIC_DELTA - same as CHANGE_DIFF Return Values A CLOB containing the desired report. Usage Notes ACTIVE reports have a rich, interactive user interface similar to Enterprise Manager while not requiring any EM installation. The report file built is in HTML format so it can be interpreted by most modern browsers. The code powering the active report is downloaded transparently by the web browser when the report is first viewed, hence viewing it requires outside connectivity. Examples -- Get the whole report for the single statement case. SELECT DBMS_SQLPA.REPORT_ANALYSIS_TASK(:stmt_task) from dual; -- Show me the summary for the sts case. SELECT DBMS_SQLPA.REPORT_ANALYSIS_TASK(:sts_task, 'TEXT', 'TYPICAL', 'SUMMARY') FROM DUAL; -- Show me the findings for the statement I'm interested in. SELECT DBMS_SQLPA.REPORT_ANALYSIS_TASK(:sts_task, 'TEXT', 'TYPICAL', 'ALL', 5) from dual;