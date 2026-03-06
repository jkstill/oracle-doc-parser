---
id: 19c__DBMS_SQLTUNE.IMPLEMENT_TUNING_TASK
name: DBMS_SQLTUNE.IMPLEMENT_TUNING_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.IMPLEMENT_TUNING_TASK

This procedure implements a set of SQL profile recommendations made by SQL Tuning Advisor.

## Syntax

```sql
DBMS_SQLTUNE.IMPLEMENT_TUNING_TASK(
    task_name         IN  VARCHAR2,
    rec_type          IN  VARCHAR2 := REC_TYPE_SQL_PROFILES,
    owner_name        IN  VARCHAR2 := NULL,
    execution_name    IN  VARCHAR2 := NULL,
    database_link_to  IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the tuning task for which to implement recommendations. |
| rec_type | VARCHAR2 | IN | Filter the types of recommendations to implement. Only ' PROFILES ' is supported. |
| owner_name | VARCHAR2 | IN | Owner of the relevant tuning task or NULL for the current user. |
| execution_name | VARCHAR2 | IN | Name of the task execution to use. If NULL , then the procedure implements recommendations from the last task execution. |
| database_link_to | VARCHAR2 | IN | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

## Usage Notes

Executing IMPLEMENT_TUNING_TASK is equivalent to executing the SCRIPT_TUNING_TASK Function and then running the script. See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.IMPLEMENT_TUNING_TASK( task_name IN VARCHAR2, rec_type IN VARCHAR2 := REC_TYPE_SQL_PROFILES, owner_name IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, database_link_to IN VARCHAR2 := NULL); Parameters Table 169-24 IMPLEMENT_TUNING_TASK Procedure Parameters Parameter Description task_name Name of the tuning task for which to implement recommendations. rec_type Filter the types of recommendations to implement. Only ' PROFILES ' is supported. owner_name Owner of the relevant tuning task or NULL for the current user. execution_name Name of the task execution to use. If NULL , then the procedure implements recommendations from the last task execution. database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1';