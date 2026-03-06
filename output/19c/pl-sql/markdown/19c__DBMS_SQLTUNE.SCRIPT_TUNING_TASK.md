---
id: 19c__DBMS_SQLTUNE.SCRIPT_TUNING_TASK
name: DBMS_SQLTUNE.SCRIPT_TUNING_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.SCRIPT_TUNING_TASK

This function creates a SQL*Plus script which can then be executed to implement a set of SQL Tuning Advisor recommendations.

## Syntax

```sql
DBMS_SQLTUNE.SCRIPT_TUNING_TASK(
  task_name         IN VARCHAR2,
  rec_type          IN VARCHAR2  := REC_TYPE_ALL,
  object_id         IN NUMBER    := NULL,
  result_limit      IN NUMBER    := NULL,
  owner_name        IN VARCHAR2  := NULL,
  execution_name    IN VARCHAR2  := NULL,
  database_link_to  IN VARCHAR2  := NULL)
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the tuning task for which to apply a script. |
| rec_type | VARCHAR2 | IN | Filter the script by types of recommendations to include. You can use any subset of the following values, separated by commas: ' ALL : ' 'PROFILES' ' 'STATISTICS' ' 'INDEXES' . For example, a script with profiles and statistics would use the filter 'PROFILES,STATISTICS' . |
| object_id | NUMBER | IN | Optionally filters by a single object ID. |
| result_limit | NUMBER | IN | Optionally shows commands for only top n SQL (ordered by object_id and ignored if an object_id is also specified). |
| owner_name | VARCHAR2 | IN | Owner of the relevant tuning task. Defaults to the current schema owner. |
| excution_name |  |  | Name of the task execution to use. If NULL , the script is generated for the last task execution. |
| database_link_to | VARCHAR2 | IN | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

**Returns:** `CLOB`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.SCRIPT_TUNING_TASK( task_name IN VARCHAR2, rec_type IN VARCHAR2 := REC_TYPE_ALL, object_id IN NUMBER := NULL, result_limit IN NUMBER := NULL, owner_name IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, database_link_to IN VARCHAR2 := NULL) RETURN CLOB; Parameters Table 169-40 SCRIPT_TUNING_TASK Function Parameters Parameter Description task_name Name of the tuning task for which to apply a script. rec_type Filter the script by types of recommendations to include. You can use any subset of the following values, separated by commas: ' ALL : ' 'PROFILES' ' 'STATISTICS' ' 'INDEXES' . For example, a script with profiles and statistics would use the filter 'PROFILES,STATISTICS' . object_id Optionally filters by a single object ID. result_limit Optionally shows commands for only top n SQL (ordered by object_id and ignored if an object_id is also specified). owner_name Owner of the relevant tuning task. Defaults to the current schema owner. excution_name Name of the task execution to use. If NULL , the script is generated for the last task execution. database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; Return Values Returns a script in the form of a CLOB .