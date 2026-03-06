---
id: 19c__DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER
name: DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_SQLTUNE
tags: [dbms_auto_sqltune]
source_file: DBMS_AUTO_SQLTUNE.html
---

# DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER

This procedure updates the value of a SQL tuning parameter of type VARCHAR2 or NUMBER for SYS_AUTO_SQL_TUNING_TASK .

## Syntax

```sql
DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER(
   parameter    IN  VARCHAR2,
   value        IN  VARCHAR2);
 
DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER(
   parameter    IN  VARCHAR2,
   value        IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| parameter | VARCHAR2 | IN | Name of the parameter to set. The possible tuning parameters that can be set by this procedure using the parameter in the form VARCHAR2 : MODE : tuning scope (comprehensive, limited) USERNAME : user name under which the statement is parsed DAYS_TO_EXPIRE : number of days until the task is deleted EXECUTION_DAYS_TO_EXPIRE : number of days until the task execution is deleted DEFAULT_EXECUTION_TYPE : default execution when none is specified by the EXECUTE_AUTO_TUNING_TASK Function and Procedure TIME_LIMIT : global timeout in seconds LOCAL_TIME_LIMIT : per-statement timeout in seconds TEST_EXECUTE : FULL - test-execute for as much time as necessary, up to the local time limit for the SQL (or the global task time limit if no SQL time limit is set) AUTO - test-execute for an automatically chosen time proportional to the tuning time OFF - do not test-execute BASIC_FILTER : basic filter for SQL tuning set OBJECT_FILTER : object filter for SQL tuning set PLAN_FILTER : plan filter for SQL tuning set (see SELECT_SQLSET for possible values) RANK_MEASURE1 : first ranking measure for SQL tuning set RANK_MEASURE2 : second ranking measure for SQL tuning set RANK_MEASURE3 : third ranking measure for SQL tuning set RESUME_FILTER : extra filter for SQL tuning sets besides BASIC_FILTER SQL_LIMIT : maximum number of SQL statements to tune SQL_PERCENTAGE : percentage filter of SQL tuning set statements The following parameters are supported for the automatic tuning task only: ACCEPT_SQL_PROFILES : whether the task should accept SQL profiles automatically ( TRUE or FALSE ) MAX_AUTO_SQL_PROFILES : maximum number of automatic SQL profiles allowed on the system, in sum MAX_SQL_PROFILES_PER_EXEC : maximum number of SQL profiles that can be automatically implemented per execution of the task. |
| value | VARCHAR2) | IN | New value of the specified parameter |

## Usage Notes

Syntax DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER( parameter IN VARCHAR2, value IN VARCHAR2); DBMS_AUTO_SQLTUNE.SET_AUTO_TUNING_TASK_PARAMETER( parameter IN VARCHAR2, value IN NUMBER); Parameters Table 29-4 SET_AUTO_TUNING_TASK_PARAMETER Procedure Parameters Parameter Description parameter Name of the parameter to set. The possible tuning parameters that can be set by this procedure using the parameter in the form VARCHAR2 : MODE : tuning scope (comprehensive, limited) USERNAME : user name under which the statement is parsed DAYS_TO_EXPIRE : number of days until the task is deleted EXECUTION_DAYS_TO_EXPIRE : number of days until the task execution is deleted DEFAULT_EXECUTION_TYPE : default execution when none is specified by the EXECUTE_AUTO_TUNING_TASK Function and Procedure TIME_LIMIT : global timeout in seconds LOCAL_TIME_LIMIT : per-statement timeout in seconds TEST_EXECUTE : FULL - test-execute for as much time as necessary, up to the local time limit for the SQL (or the global task time limit if no SQL time limit is set) AUTO - test-execute for an automatically chosen time proportional to the tuning time OFF - do not test-execute BASIC_FILTER : basic filter for SQL tuning set OBJECT_FILTER : object filter for SQL tuning set PLAN_FILTER : plan filter for SQL tuning set (see SELECT_SQLSET for possible values) RANK_MEASURE1 : first ranking measure for SQL tuning set RANK_MEASURE2 : second ranking measure for SQL tuning set RANK_MEASURE3 : third ranking measure for SQL tuning set RESUME_FILTER : extra filter for SQL tuning sets besides BASIC_FILTER SQL_LIMIT : maximum number of SQL statements to tune SQL_PERCENTAGE : percentage filter of SQL tuning set statements The following parameters are supported for the automatic tuning task only: ACCEPT_SQL_PROFILES : whether the task should accept SQL profiles automatically ( TRUE or FALSE ) MAX_AUTO_SQL_PROFILES : maximum number of automatic SQL profiles allowed on the system, in sum MAX_SQL_PROFILES_PER_EXEC : maximum number of SQL profiles that can be automatically implemented per execution of the task. value New value of the specified parameter