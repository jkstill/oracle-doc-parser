---
id: 19c__DBMS_SQLTUNE.LOAD_SQLSET
name: DBMS_SQLTUNE.LOAD_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.LOAD_SQLSET

This procedure populates the SQL tuning set with a set of selected SQL statements. You can call the procedure multiple times to add new SQL statements or replace attributes of existing statements.

## Syntax

```sql
DBMS_SQLTUNE.LOAD_SQLSET (
   sqlset_name       IN  VARCHAR2,
   populate_cursor   IN  sqlset_cursor,
   load_option       IN VARCHAR2 := 'INSERT', 
   update_option     IN VARCHAR2 := 'REPLACE', 
   update_condition  IN VARCHAR2 :=  NULL,
   update_attributes IN VARCHAR2 :=  NULL,
   ignore_null       IN BOOLEAN  :=  TRUE,
   commit_rows       IN POSITIVE :=  NULL,
   sqlset_owner      IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of SQL tuning set to be loaded. |
| populate_cursor | sqlset_cursor | IN | Specifies the cursor reference to the SQL tuning set to be loaded. |
| load_option | VARCHAR2 | IN | Specifies which statements are loaded into the SQL tuning set. The possible values are: INSERT (default) — Adds only new statements. UPDATE — Updates existing the SQL statements and ignores any new statements. MERGE — Inserts new statements and updates the information of the existing ones. |
| update_option | VARCHAR2 | IN | Specifies how existing SQL statements are updated. This parameter is considered only if load_option is specified with UPDATE or MERGE as an option. The possible values are: REPLACE (default) — Updates the statement using the new statistics, bind list, object list, and so on. ACCUMULATE — Combines attributes when possible (for example, statistics such as elapsed_time ), and otherwise replaces the existing values (for example, module and action) with the provided values. The SQL statement attributes that can be accumulated are: elapsed_time , buffer_gets , direct_writes , disk_reads , row_processed , fetches , executions , end_of_fetch_count , stat_period and active_stat_period . |
| update_condition | VARCHAR2 | IN | Specifies when to perform the update. The procedure only performs the update when the specified condition is satisfied. The condition can refer to either the data source or destination. The condition must use the following prefixes to refer to attributes from the source or the destination: OLD — Refers to statement attributes from the SQL tuning set (destination). NEW — Refers to statement attributes from the input statements (source). |
| update_attributes | VARCHAR2 | IN | Specifies the list of SQL statement attributes to update during a merge or update. The possible values are: NULL (default) — Specifies the content of the input cursor except the execution context. On other terms, it is equivalent to ALL without execution contexts such as module and action. BASIC — Specifies statistics and binds only. TYPICAL — Specifies BASIC with SQL plans (without row source statistics) and without an object reference list. ALL — Specifies all attributes, including the execution context attributes such as module and action. List of comma separated attribute names to update: EXECUTION_CONTEXT EXECUTION_STATISTICS SQL_BINDS SQL_PLAN SQL_PLAN_STATISTICS (similar to SQL_PLAN with added row source statistics) |
| ignore_null | BOOLEAN | IN | Specifies whether to update attributes when the new value is NULL . If TRUE , then the procedure does not update an attribute when the new value is NULL . That is, do not override with NULL values unless intentional. |
| commit_rows | POSITIVE | IN | Specifies whether to commit statements after DML. If a value is provided, then the load commits after each specified number of statements is inserted. If NULL is provided, then the load commits only once, at the end of the operation. Providing a value for this argument enables you to monitor the progress of a SQL tuning set load operation in the DBA_SQLSET views. The STATEMENT_COUNT value increases as new SQL statements are loaded. |
| sqlset_owner | VARCHAR2 | IN | Defines the owner of the SQL tuning set, or the current schema owner (or NULL for the current owner). |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.LOAD_SQLSET ( sqlset_name IN VARCHAR2, populate_cursor IN sqlset_cursor, load_option IN VARCHAR2 := 'INSERT', update_option IN VARCHAR2 := 'REPLACE', update_condition IN VARCHAR2 := NULL, update_attributes IN VARCHAR2 := NULL, ignore_null IN BOOLEAN := TRUE, commit_rows IN POSITIVE := NULL, sqlset_owner IN VARCHAR2 := NULL); Parameters Table 169-26 LOAD_SQLSET Procedure Parameters Parameter Description sqlset_name Specifies the name of SQL tuning set to be loaded. populate_cursor Specifies the cursor reference to the SQL tuning set to be loaded. load_option Specifies which statements are loaded into the SQL tuning set. The possible values are: INSERT (default) — Adds only new statements. UPDATE — Updates existing the SQL statements and ignores any new statements. MERGE — Inserts new statements and updates the information of the existing ones. update_option Specifies how existing SQL statements are updated. This parameter is considered only if load_option is specified with UPDATE or MERGE as an option. The possible values are: REPLACE (default) — Updates the statement using the new statistics, bind list, object list, and so on. ACCUMULATE — Combines attributes when possible (for example, statistics such as elapsed_time ), and otherwise replaces the existing values (for example, module and action) with the provided values. The SQL statement attributes that can be accumulated are: elapsed_time , buffer_gets , direct_writes , disk_reads , row_processed , fetches , executions , end_of_fetch_count , stat_period and active_stat_period . update_condition Specifies when to perform the update. The procedure only performs the update when the specified condition is satisfied. The condition can refer to either the data source or destination. The condition must use the following prefixes to refer to attributes from the source or the destination: OLD — Refers to statement attributes from the SQL tuning set (destination). NEW — Refers to statement attributes from the input statements (source). update_attributes Specifies the list of SQL statement attributes to update during a merge or update. The possible values are: NULL (default) — Specifies the content of the input cursor except the execution context. On other terms, it is equivalent to ALL without execution contexts such as module and action. BASIC — Specifies statistics and binds only. TYPICAL — Specifies BASIC with SQL plans (without row source statistics) and without an object reference list. ALL — Specifies all attributes, including the execution context attributes such as module and action. List of comma separated attribute names to update: EXECUTION_CONTEXT EXECUTION_STATISTICS SQL_BINDS SQL_PLAN SQL_PLAN_STATISTICS (similar to SQL_PLAN with added row source statistics) ignore_null Specifies whether to update attributes when the new value is NULL . If TRUE , then the procedure does not update an attribute when the new value is NULL . That is, do not override with NULL values unless intentional. commit_rows Specifies whether to commit statements after DML. If a value is provided, then the load commits after each specified number of statements is inserted. If NULL is provided, then the load commits only once, at the end of the operation. Providing a value for this argument enables you to monitor the progress of a SQL tuning set load operation in the DBA_SQLSET views. The STATEMENT_COUNT value increases as new SQL statements are loaded. sqlset_owner Defines the owner of the SQL tuning set, or the current schema owner (or NULL for the current owner). Exceptions This procedure returns an error when sqlset_name is invalid, or a corresponding SQL tuning set does not exist, or the populate_cursor is incorrect and cannot be executed. Exceptions are also raised when invalid filters are provided. Filters can be invalid either because they don't parse (for example, they refer to attributes not in sqlset_row ), or because they violate the user's privileges.