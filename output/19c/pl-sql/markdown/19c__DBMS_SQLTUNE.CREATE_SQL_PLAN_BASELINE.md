---
id: 19c__DBMS_SQLTUNE.CREATE_SQL_PLAN_BASELINE
name: DBMS_SQLTUNE.CREATE_SQL_PLAN_BASELINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.CREATE_SQL_PLAN_BASELINE

This procedure creates a SQL plan baseline for an execution plan. It can be used in the context of an Alternative Plan Finding made by SQL Tuning Advisor.

## Syntax

```sql
DBMS_SQLTUNE.CREATE_SQL_PLAN_BASELINE (
   task_name            IN VARCHAR2,
   object_id            IN NUMBER   := NULL,
   plan_hash_value      IN NUMBER,
   owner_name           IN VARCHAR2 := NULL,
   database_link_to     IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task for which to get a script |
| object_id | NUMBER | IN | Object ID to which the SQL corresponds |
| plan_hash_value | NUMBER | IN | Plan to create plan baseline |
| owner_name | VARCHAR2 | IN | Owner of the relevant tuning task. Defaults to the current schema owner. |
| database_link_to | VARCHAR2 | IN | Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1'; |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Advisor Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.CREATE_SQL_PLAN_BASELINE ( task_name IN VARCHAR2, object_id IN NUMBER := NULL, plan_hash_value IN NUMBER, owner_name IN VARCHAR2 := NULL, database_link_to IN VARCHAR2 := NULL); Parameters Table 169-14 CREATE_SQL_PLAN_BASELINE Procedure Parameters Parameter Description task_name Name of the task for which to get a script object_id Object ID to which the SQL corresponds plan_hash_value Plan to create plan baseline owner_name Owner of the relevant tuning task. Defaults to the current schema owner. database_link_to Name of a database link that exists on a standby database. The link specifies the connection to a primary database. By default, the value is null, which means that the SQL Tuning Advisor session is local. Use DBMS_SQLTUNE to tune high-load SQL statements running on a standby database in an Active Data Guard scenario. When you execute REPORT_TUNING_TASK locally on the standby database, the function uses the database link to obtain the data from the primary database, and then constructs it locally on the standby database. The database_link_to parameter must specify a private database link. This link must be owned by SYS and accessed by the default privileged user SYS$UMF . The following sample statement creates a link named lnk_to_pri : CREATE DATABASE LINK lnk_to_pri CONNECT TO SYS$UMF IDENTIFIED BY password USING 'inst1';