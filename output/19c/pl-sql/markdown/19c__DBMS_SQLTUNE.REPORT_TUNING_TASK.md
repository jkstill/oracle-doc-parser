---
id: 19c__DBMS_SQLTUNE.REPORT_TUNING_TASK
name: DBMS_SQLTUNE.REPORT_TUNING_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REPORT_TUNING_TASK

This function displays the results of a tuning task. By default the report is in text format.

## Syntax

```sql
DBMS_SQLTUNE.REPORT_TUNING_TASK(
   task_name        IN   VARCHAR2,
   type             IN   VARCHAR2   := 'TEXT',
   level            IN   VARCHAR2   := 'TYPICAL',
   section          IN   VARCHAR2   := ALL,
   object_id        IN   NUMBER     := NULL,
   result_limit     IN   NUMBER     := NULL,
   owner_name       IN   VARCHAR2   := NULL,
   execution_name   IN   VARCHAR2   := NULL,
   database_link_to IN   VARCHAR2   := NULL)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the tuning task. |
| type | VARCHAR2 | IN | Type of the report to produce. Possible values are TEXT which produces a text report. |
| level | VARCHAR2 | IN | Level of detail in the report: BASIC : simple version of the report. Just show info about the actions taken by the advisor. TYPICAL : show information about every statement analyzed, including requests not implemented. ALL : highly detailed report level, also provides annotations about statements skipped over. |
| section | VARCHAR2 | IN | Section of the report to include. You can limit the report to any of the following single sections ( ALL for all sections): SUMMARY - Summary information FINDINGS - Tuning findings PLAN - Explain plans INFORMATION - General information ERROR - Statements with errors ALL - All statements |
| object_id | NUMBER | IN | Advisor framework object ID that represents a single statement to restrict reporting to. NULL for all statements. Only valid for reports that target a single execution. |
| result_limit | NUMBER | IN | Maximum number of SQL statements to show in the report. |
| owner_name | VARCHAR2 | IN | Owner of the relevant tuning task. The default is the current schema owner. |
| execution_name | VARCHAR2 | IN | Name of the task execution to use. If NULL , then the function generates the report for the last task execution. |
| database_link_to | VARCHAR2 | IN | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

**Returns:** `CLOB`

## Usage Notes

Syntax See Also: DBMS_SQLTUNE SQL Performance Reporting Subprograms for other subprograms in this group DBMS_SQLTUNE.REPORT_TUNING_TASK( task_name IN VARCHAR2, type IN VARCHAR2 := 'TEXT', level IN VARCHAR2 := 'TYPICAL', section IN VARCHAR2 := ALL, object_id IN NUMBER := NULL, result_limit IN NUMBER := NULL, owner_name IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, database_link_to IN VARCHAR2 := NULL) RETURN CLOB; See Also: DBMS_SQLTUNE SQL Performance Reporting Subprograms for other subprograms in this group Parameters Table 169-35 REPORT_TUNING_TASK Function Parameters Parameter Description task_name Name of the tuning task. type Type of the report to produce. Possible values are TEXT which produces a text report. level Level of detail in the report: BASIC : simple version of the report. Just show info about the actions taken by the advisor. TYPICAL : show information about every statement analyzed, including requests not implemented. ALL : highly detailed report level, also provides annotations about statements skipped over. section Section of the report to include. You can limit the report to any of the following single sections ( ALL for all sections): SUMMARY - Summary information FINDINGS - Tuning findings PLAN - Explain plans INFORMATION - General information ERROR - Statements with errors ALL - All statements object_id Advisor framework object ID that represents a single statement to restrict reporting to. NULL for all statements. Only valid for reports that target a single execution. result_limit Maximum number of SQL statements to show in the report. owner_name Owner of the relevant tuning task. The default is the current schema owner. execution_name Name of the task execution to use. If NULL , then the function generates the report for the last task execution. database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; Return Values A CLOB containing the desired report. Examples -- Display the report for a single statement. SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(:stmt_task) FROM DUAL; -- Display the summary for a SQL tuning set. SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(:sts_task, 'TEXT', 'TYPICAL', 'SUMMARY') FROM DUAL; -- Display the findings for a specific statement. SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(:sts_task, 'TEXT', 'TYPICAL','FINDINGS', 5) FROM DUAL;