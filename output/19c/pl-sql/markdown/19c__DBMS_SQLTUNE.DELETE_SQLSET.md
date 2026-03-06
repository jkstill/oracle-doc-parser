---
id: 19c__DBMS_SQLTUNE.DELETE_SQLSET
name: DBMS_SQLTUNE.DELETE_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.DELETE_SQLSET

This procedure deletes a set of SQL statements from a SQL tuning set.

## Syntax

```sql
DBMS_SQLTUNE.DELETE_SQLSET (
   sqlset_name   IN  VARCHAR2,
   basic_filter  IN  VARCHAR2 := NULL,
   sqlset_owner  IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the SQL tuning set. |
| basic_filter | VARCHAR2 | IN | Specifies the SQL predicate to filter the SQL from the SQL tuning set. This basic filter is used as a where clause on the SQL tuning set content to select a desired subset of SQL from the SQL tuning set. |
| sqlset_owner | VARCHAR2 | IN | Specifies the owner of the SQL tuning set, or NULL for current schema owner. |

## Usage Notes

Syntax DBMS_SQLTUNE.DELETE_SQLSET ( sqlset_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL, sqlset_owner IN VARCHAR2 := NULL); Parameters Table 169-19 DELETE_SQLSET Procedure Parameters Parameter Description sqlset_name Specifies the name of the SQL tuning set. basic_filter Specifies the SQL predicate to filter the SQL from the SQL tuning set. This basic filter is used as a where clause on the SQL tuning set content to select a desired subset of SQL from the SQL tuning set. sqlset_owner Specifies the owner of the SQL tuning set, or NULL for current schema owner. Examples -- Delete all statements in a sql tuning set. EXEC DBMS_SQLTUNE.DELETE_SQLSET(sqlset_name => 'my_workload'); -- Delete all statements in a sql tuning set which ran for less than a second EXEC DBMS_SQLTUNE.DELETE_SQLSET(sqlset_name => 'my_workload', - basic_filter => 'elapsed_time < 1000000');