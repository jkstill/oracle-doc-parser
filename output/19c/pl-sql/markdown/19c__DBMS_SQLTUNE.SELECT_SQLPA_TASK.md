---
id: 19c__DBMS_SQLTUNE.SELECT_SQLPA_TASK
name: DBMS_SQLTUNE.SELECT_SQLPA_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SELECT_SQLPA_TASK

This function collects SQL statements from a SQL Performance Analyzer comparison task.

## Syntax

```sql
DBMS_SQLTUNE.SELECT_SQLPA_TASK(
    task_name         IN VARCHAR2,
    task_owner        IN VARCHAR2 := NULL,
    execution_name    IN VARCHAR2 := NULL,
    level_filter      IN VARCHAR2 := 'REGRESSED',
    basic_filter      IN VARCHAR2 := NULL,
    object_filter     IN VARCHAR2 := NULL,
    attribute_list    IN VARCHAR2 := 'TYPICAL')
RETURN sys.sqlset PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Specifies the name of the SQL Performance Analyzer task. |
| task_owner | VARCHAR2 | IN | Specifies the owner of the SQL Performance Analyzer task. If NULL , then assume the current user. |
| execution_name | VARCHAR2 | IN | Specifies the name of the SQL Performance Analyzer task execution (type COMPARE PERFORMANCE ) from which the provided filters will be applied. If NULL , then assume the most recent COMPARE PERFORMANCE execution. |
| level_filter | VARCHAR2 | IN | Specifies which subset of SQL statements to include. Same format as DBMS_SQLPA.REPORT_ANALYSIS_TASK.LEVEL , with some possible strings removed. IMPROVED includes only improved SQL. REGRESSED includes only regressed SQL (default). CHANGED includes only SQL with changed performance. UNCHANGED includes only SQL with unchanged performance. CHANGED_PLANS includes only SQL with plan changes. UNCHANGED_PLANS includes only SQL with unchanged plans. ERRORS includes only SQL with errors only. MISSING_SQL includes only missing SQL statements (across STS). NEW_SQL includes only new SQL statements (across STS). |
| basic filter |  |  | Specifies the SQL predicate to filter the SQL in addition to the level filters. |
| object_filter | VARCHAR2 | IN | Currently not supported. |
| attribute_list | VARCHAR2 | IN | Defines the SQL statement attributes to return in the result. Possible values are: TYPICAL — Returns BASIC plus the SQL plan (without row source statistics) and without an object reference list. This is the default. BASIC — Returns all attributes (such as execution statistics and binds) except the plans. The execution context is always part of the result. ALL — Returns all attributes. Comma-separated list of attribute names this allows to return only a subset of SQL attributes: EXECUTION_STATISTICS , SQL_BINDS , SQL_PLAN_STATISTICS (similar to SQL_PLAN + row source statistics). |

**Returns:** `sys.sqlset`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Oracle Database Testing Guide for a SELECT_SQLPA_TASK example See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Oracle Database Testing Guide for a SELECT_SQLPA_TASK example Syntax DBMS_SQLTUNE.SELECT_SQLPA_TASK( task_name IN VARCHAR2, task_owner IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, level_filter IN VARCHAR2 := 'REGRESSED', basic_filter IN VARCHAR2 := NULL, object_filter IN VARCHAR2 := NULL, attribute_list IN VARCHAR2 := 'TYPICAL') RETURN sys.sqlset PIPELINED; Parameters Table 169-43 SELECT_SQLPA_TASK Function Parameters Parameter Description task_name Specifies the name of the SQL Performance Analyzer task. task_owner Specifies the owner of the SQL Performance Analyzer task. If NULL , then assume the current user. execution_name Specifies the name of the SQL Performance Analyzer task execution (type COMPARE PERFORMANCE ) from which the provided filters will be applied. If NULL , then assume the most recent COMPARE PERFORMANCE execution. level_filter Specifies which subset of SQL statements to include. Same format as DBMS_SQLPA.REPORT_ANALYSIS_TASK.LEVEL , with some possible strings removed. IMPROVED includes only improved SQL. REGRESSED includes only regressed SQL (default). CHANGED includes only SQL with changed performance. UNCHANGED includes only SQL with unchanged performance. CHANGED_PLANS includes only SQL with plan changes. UNCHANGED_PLANS includes only SQL with unchanged plans. ERRORS includes only SQL with errors only. MISSING_SQL includes only missing SQL statements (across STS). NEW_SQL includes only new SQL statements (across STS). basic filter Specifies the SQL predicate to filter the SQL in addition to the level filters. object_filter Currently not supported. attribute_list Defines the SQL statement attributes to return in the result. Possible values are: TYPICAL — Returns BASIC plus the SQL plan (without row source statistics) and without an object reference list. This is the default. BASIC — Returns all attributes (such as execution statistics and binds) except the plans. The execution context is always part of the result. ALL — Returns all attributes. Comma-separated list of attribute names this allows to return only a subset of SQL attributes: EXECUTION_STATISTICS , SQL_BINDS , SQL_PLAN_STATISTICS (similar to SQL_PLAN + row source statistics). Return Values This function returns a SQL tuning set object.