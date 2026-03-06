---
id: 19c__DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT
name: DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT

This procedure adds a single statement to the specified workload.

## Syntax

```sql
DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT (
   workload_name          IN VARCHAR2,
   module                 IN VARCHAR2,
   action                 IN VARCHAR2,
   cpu_time               IN NUMBER := 0,
   elapsed_time           IN NUMBER := 0,
   disk_reads             IN NUMBER := 0,
   buffer_gets            IN NUMBER := 0,
   rows_processed         IN NUMBER := 0,
   optimizer_cost         IN NUMBER := 0,
   executions             IN NUMBER := 1,
   priority               IN NUMBER := 2,
   last_execution_date    IN DATE := 'SYSDATE',
   stat_period            IN NUMBER := 0,
   username               IN VARCHAR2,
   sql_text               IN CLOB);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The workload name that uniquely identifies an existing workload. |
| module | VARCHAR2 | IN | An optional business application module that will be associated with the SQL statement. |
| action | VARCHAR2 | IN | An optional application action that will be associated with the SQL statement. |
| cpu_time | NUMBER | IN | The total CPU time in seconds that is consumed by the SQL statement. |
| elapsed_time | NUMBER | IN | The total elapsed time in seconds that is consumed by the SQL statement. |
| disk_reads | NUMBER | IN | The total disk-read operations that are consumed by the SQL statement. |
| buffer_gets | NUMBER | IN | The total buffer-get operations that are consumed by the SQL statement. |
| rows_processed | NUMBER | IN | The average number of rows processed by the SQL statement. |
| optimizer_cost | NUMBER | IN | The cost value calculated by the optimizer. |
| executions | NUMBER | IN | The total execution count of the SQL statement. This value should be greater than zero. |
| priority | NUMBER | IN | The relative priority of the SQL statement. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . |
| last_execution_date | DATE | IN | The date and time at which the SQL statement last executed. If the value is NULL , then the database uses the current date and time. |
| stat_period | NUMBER | IN | Time interval in seconds from which statement statistics were calculated. |
| username | VARCHAR2 | IN | The database user that executed the SQL statement. Because a user name is an Oracle identifier, the username value must be entered exactly as it is stored in the server. For example, if the user SCOTT is the executing user, then you must provide the user identifier SCOTT in all uppercase letters. It will not recognize the user scott or Scott as a match for SCOTT . |
| sql_text | CLOB) | IN | The complete SQL statement. To increase the quality of a recommendation, the SQL statement should not contain bind variables. |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT ( workload_name IN VARCHAR2, module IN VARCHAR2, action IN VARCHAR2, cpu_time IN NUMBER := 0, elapsed_time IN NUMBER := 0, disk_reads IN NUMBER := 0, buffer_gets IN NUMBER := 0, rows_processed IN NUMBER := 0, optimizer_cost IN NUMBER := 0, executions IN NUMBER := 1, priority IN NUMBER := 2, last_execution_date IN DATE := 'SYSDATE', stat_period IN NUMBER := 0, username IN VARCHAR2, sql_text IN CLOB); Parameters Table 16-3 ADD_SQLWKLD_STATEMENT Procedure Parameters Parameter Description workload_name The workload name that uniquely identifies an existing workload. module An optional business application module that will be associated with the SQL statement. action An optional application action that will be associated with the SQL statement. cpu_time The total CPU time in seconds that is consumed by the SQL statement. elapsed_time The total elapsed time in seconds that is consumed by the SQL statement. disk_reads The total disk-read operations that are consumed by the SQL statement. buffer_gets The total buffer-get operations that are consumed by the SQL statement. rows_processed The average number of rows processed by the SQL statement. optimizer_cost The cost value calculated by the optimizer. executions The total execution count of the SQL statement. This value should be greater than zero. priority The relative priority of the SQL statement. The value must be one of the following: 1- HIGH , 2- MEDIUM , or 3- LOW . last_execution_date The date and time at which the SQL statement last executed. If the value is NULL , then the database uses the current date and time. stat_period Time interval in seconds from which statement statistics were calculated. username The database user that executed the SQL statement. Because a user name is an Oracle identifier, the username value must be entered exactly as it is stored in the server. For example, if the user SCOTT is the executing user, then you must provide the user identifier SCOTT in all uppercase letters. It will not recognize the user scott or Scott as a match for SCOTT . sql_text The complete SQL statement. To increase the quality of a recommendation, the SQL statement should not contain bind variables. Usage Notes You cannot modify or delete a workload when it is currently referenced by an active task. A task is considered active if it is not in its initial state. See RESET_TASK Procedure for directions on setting a task to its initial state. The ADD_SQLWKLD_STATEMENT procedure accepts several parameters that may be ignored by the caller. The database only uses the disk_reads , buffer_gets , and optimizer_cost parameters to sort workload data when actual analysis occurs. Therefore, actual values are only necessary when the order_list task parameter references a particular statistic. To determine what statistics to provide when adding a new SQL statement to a workload, examine or set the task parameter order_list . The order_list parameter accepts any combination of the keys: cpu_time elapsed_time buffer_gets optimizer_cost disk_reads executions priority The optimizer_cost key, which is a typical setting of priority , indicates that SQL Access Advisor sorts the workload data by priority and optimizer_cost , and processes the highest cost statements first. Any statements that you add to the workload must include appropriate priority and optimizer_cost values. All other statistics can be defaulted or set to zero. For the statistical keys referenced by the order_list task parameter, the actual parameter values should be reasonably accurate since they will be compared to other statements in the workload. If the caller is unable to estimate values, then choose values that would determine its importance relative to other statements in the workload. For example, if the current statement is considered the most critical query in your business, then an appropriate value would be anything greater than all other values for the same statistic found in the workload.