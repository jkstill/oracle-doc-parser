---
id: 19c__DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER
name: DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER

This procedure updates the value of a SQL tuning parameter of type VARCHAR2 or NUMBER .

## Syntax

```sql
DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER (
   task_name        IN  VARCHAR2,
   parameter        IN  VARCHAR2,
   value            IN  VARCHAR2,
   database_link_to IN  VARCHAR2);

DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER (
   task_name        IN  VARCHAR2,
   parameter        IN  VARCHAR2,
   value            IN  NUMBER,
   database_link_to IN  VARCHAR2);
);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Identifier of the task to execute |
| parameter | VARCHAR2 | IN | Name of the parameter to set. The possible tuning parameters that can be set by this procedure using the parameter in the form VARCHAR2 : APPLY_CAPTURED_COMPILENV : indicates whether the advisor could use the compilation environment captured with the SQL statements. The default is 0 (that is, NO ). BASIC_FILTER : basic filter for SQL tuning set DAYS_TO_EXPIRE : number of days until the task is deleted DEFAULT_EXECUTION_TYPE : the task defaults to this type of execution when none is specified by the EXECUTE_TUNING_TASK Function and Procedure EXECUTION_DAYS_TO_EXPIRE : number of days until the tasks's executions is deleted (without deleting the task) LOCAL_TIME_LIMIT : per-statement time out (seconds) MODE : tuning scope (comprehensive, limited) OBJECT_FILTER : object filter for SQL tuning set PLAN_FILTER : plan filter for SQL tuning set (see SELECT_SQLSET for possible values) RANK_MEASURE1 : first ranking measure for SQL tuning set RANK_MEASURE2 : second possible ranking measure for SQL tuning set RANK_MEASURE3 : third possible ranking measure for SQL tuning set RESUME_FILTER : a extra filter for SQL tuning sets besides BASIC_FILTER SQL_LIMIT : maximum number of SQL statements to tune SQL_PERCENTAGE : percentage filter of SQL tuning set statements TEST_EXECUTE : FULL / AUTO / OFF . * FULL - test-execute for as much time as necessary, up to the local time limit for the SQL (or the global task time limit if no SQL time limit is set) * AUTO - test-execute for an automatically-chosen time proportional to the tuning time * OFF - do not test-execute TIME_LIMIT : global time out (seconds) USERNAME : username under which the statement is parsed |
| value | VARCHAR2 | IN | New value of the specified parameter |
| database_link_to | VARCHAR2) | IN | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER ( task_name IN VARCHAR2, parameter IN VARCHAR2, value IN VARCHAR2, database_link_to IN VARCHAR2); DBMS_SQLTUNE.SET_TUNING_TASK_PARAMETER ( task_name IN VARCHAR2, parameter IN VARCHAR2, value IN NUMBER, database_link_to IN VARCHAR2); ); Parameters Table 169-46 SET_TUNING_TASK_PARAMETER Procedure Parameters Parameter Description task_name Identifier of the task to execute parameter Name of the parameter to set. The possible tuning parameters that can be set by this procedure using the parameter in the form VARCHAR2 : APPLY_CAPTURED_COMPILENV : indicates whether the advisor could use the compilation environment captured with the SQL statements. The default is 0 (that is, NO ). BASIC_FILTER : basic filter for SQL tuning set DAYS_TO_EXPIRE : number of days until the task is deleted DEFAULT_EXECUTION_TYPE : the task defaults to this type of execution when none is specified by the EXECUTE_TUNING_TASK Function and Procedure EXECUTION_DAYS_TO_EXPIRE : number of days until the tasks's executions is deleted (without deleting the task) LOCAL_TIME_LIMIT : per-statement time out (seconds) MODE : tuning scope (comprehensive, limited) OBJECT_FILTER : object filter for SQL tuning set PLAN_FILTER : plan filter for SQL tuning set (see SELECT_SQLSET for possible values) RANK_MEASURE1 : first ranking measure for SQL tuning set RANK_MEASURE2 : second possible ranking measure for SQL tuning set RANK_MEASURE3 : third possible ranking measure for SQL tuning set RESUME_FILTER : a extra filter for SQL tuning sets besides BASIC_FILTER SQL_LIMIT : maximum number of SQL statements to tune SQL_PERCENTAGE : percentage filter of SQL tuning set statements TEST_EXECUTE : FULL / AUTO / OFF . * FULL - test-execute for as much time as necessary, up to the local time limit for the SQL (or the global task time limit if no SQL time limit is set) * AUTO - test-execute for an automatically-chosen time proportional to the tuning time * OFF - do not test-execute TIME_LIMIT : global time out (seconds) USERNAME : username under which the statement is parsed value New value of the specified parameter database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; Usage Notes When setting automatic tuning task parameters, use the SET_AUTO_TUNING_TASK_PARAMETER Procedures in the DBMS_AUTO_SQLTUNE package.