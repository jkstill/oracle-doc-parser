---
id: 19c__DBMS_SQLPA.SET_ANALYSIS_DEFAULT_PARAMETER
name: DBMS_SQLPA.SET_ANALYSIS_DEFAULT_PARAMETER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLPA
tags: [dbms_sqlpa]
source_file: DBMS_SQLPA.html
---

# DBMS_SQLPA.SET_ANALYSIS_DEFAULT_PARAMETER

This procedure sets the SQL analysis task parameter default value.

## Syntax

```sql
DBMS_SQLPA.SET_ANALYSIS_DEFAULT_PARAMETER(
   parameter    IN  VARCHAR2,
   value        IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parameter | VARCHAR2 | IN | Name of the parameter to set. The possible analysis parameters that can be set by this procedure are: APPLY_CAPTURED_COMPILENV : indicates whether the advisor could use the compilation environment captured with the SQL statements. The default is 0 (that is, NO ). BASIC_FILTER : basic filter for SQL tuning set COMPARISON_METRIC : specify an expression of execution statistics to use in performance comparison (Example: buffer_gets , cpu_time + buffer_gets * 10) DATABASE_LINK : can be set to the global name of a PUBLIC database link. When it is set, SQL Performance Analyzer will use the database link for all TEST EXECUTE and EXPLAIN PLAN operations by sending the SQL statements to the remote database to be processed remotely. The analysis results will still be stored on the local database. DAYS_TO_EXPIRE : number of days until the task is deleted DEFAULT_EXECUTION_TYPE : the task will default to this type of execution when none is specified by the EXECUTE_ANALYSIS_TASK Function & Procedure . EXECUTE_FULLDML : TRUE to execute DML statement fully, including acquiring row locks and modifying rows; FALSE (default) to execute only the query part of the DML without modifying data. When TRUE , SQL Performance Analyzer will issue a rollback following DML execution to prevent persistent changes from being made by the DML. EXECUTION_DAYS_TO_EXPIRE : number of days until the tasks's executions will be deleted (without deleting the task) EXECUTION_NAME1 : name of the first task execution to analyze EXECUTION_NAME2 : name of the second task execution to analyze LOCAL_TIME_LIMIT : per-statement time out (seconds) |
| parameter (contd.) |  |  | PLAN_FILTER : plan filter for SQL tuning set (see SELECT_SQLSET for possible values) RANK_MEASURE1 : first ranking measure for SQL tuning set RANK_MEASURE2 : second possible ranking measure for SQL tuning set RANK_MEASURE3 : third possible ranking measure for SQL tuning set RESUME_FILTER : a extra filter for SQL tuning sets besides BASIC_FILTER SQL_IMPACT_THRESHOLD : threshold of a change impact on a SQL statement. Same as the previous parameter, but at the level of the SQL statement. SQL_LIMIT : maximum number of SQL statements to process SQL_PERCENTAGE : percentage filter of SQL tuning set statements TIME_LIMIT : global time out (seconds) WORKLOAD_IMPACT_THRESHOLD : threshold of a SQL statement impact on a workload. Statements which workload change impact is below the absolute value of this threshold will be ignored and not considered for improvement or regression. |
| value | VARCHAR2) | IN | New value of the specified parameter |

## Usage Notes

Syntax This form of the procedure updates the default value of an analyzer parameter of type VARCHAR2 . DBMS_SQLPA.SET_ANALYSIS_DEFAULT_PARAMETER( parameter IN VARCHAR2, value IN VARCHAR2); This form of the procedure updates the default value of an analyzer parameter of type NUMBER . DBMS_SQLPA.SET_ANALYSIS_DEFAULT_PARAMETER( parameter IN VARCHAR2, value IN NUMBER); Parameters Table 166-11 SET_ANALYSIS_DEFAULT_PARAMETER Procedure Parameters Parameter Description parameter Name of the parameter to set. The possible analysis parameters that can be set by this procedure are: APPLY_CAPTURED_COMPILENV : indicates whether the advisor could use the compilation environment captured with the SQL statements. The default is 0 (that is, NO ). BASIC_FILTER : basic filter for SQL tuning set COMPARISON_METRIC : specify an expression of execution statistics to use in performance comparison (Example: buffer_gets , cpu_time + buffer_gets * 10) DATABASE_LINK : can be set to the global name of a PUBLIC database link. When it is set, SQL Performance Analyzer will use the database link for all TEST EXECUTE and EXPLAIN PLAN operations by sending the SQL statements to the remote database to be processed remotely. The analysis results will still be stored on the local database. DAYS_TO_EXPIRE : number of days until the task is deleted DEFAULT_EXECUTION_TYPE : the task will default to this type of execution when none is specified by the EXECUTE_ANALYSIS_TASK Function & Procedure . EXECUTE_FULLDML : TRUE to execute DML statement fully, including acquiring row locks and modifying rows; FALSE (default) to execute only the query part of the DML without modifying data. When TRUE , SQL Performance Analyzer will issue a rollback following DML execution to prevent persistent changes from being made by the DML. EXECUTION_DAYS_TO_EXPIRE : number of days until the tasks's executions will be deleted (without deleting the task) EXECUTION_NAME1 : name of the first task execution to analyze EXECUTION_NAME2 : name of the second task execution to analyze LOCAL_TIME_LIMIT : per-statement time out (seconds) parameter (contd.) PLAN_FILTER : plan filter for SQL tuning set (see SELECT_SQLSET for possible values) RANK_MEASURE1 : first ranking measure for SQL tuning set RANK_MEASURE2 : second possible ranking measure for SQL tuning set RANK_MEASURE3 : third possible ranking measure for SQL tuning set RESUME_FILTER : a extra filter for SQL tuning sets besides BASIC_FILTER SQL_IMPACT_THRESHOLD : threshold of a change impact on a SQL statement. Same as the previous parameter, but at the level of the SQL statement. SQL_LIMIT : maximum number of SQL statements to process SQL_PERCENTAGE : percentage filter of SQL tuning set statements TIME_LIMIT : global time out (seconds) WORKLOAD_IMPACT_THRESHOLD : threshold of a SQL statement impact on a workload. Statements which workload change impact is below the absolute value of this threshold will be ignored and not considered for improvement or regression. value New value of the specified parameter