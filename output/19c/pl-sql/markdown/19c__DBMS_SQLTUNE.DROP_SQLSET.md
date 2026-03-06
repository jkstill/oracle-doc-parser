---
id: 19c__DBMS_SQLTUNE.DROP_SQLSET
name: DBMS_SQLTUNE.DROP_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.DROP_SQLSET

This procedure drops a SQL tuning set if it is not active.

## Syntax

```sql
DBMS_SQLTUNE.DROP_SQLSET (
   sqlset_name   IN  VARCHAR2,
   sqlset_owner  IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the SQL tuning set. |
| sqlset_owner | VARCHAR2 | IN | Specifies the owner of the SQL tuning set, or NULL for current schema owner. |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.DROP_SQLSET ( sqlset_name IN VARCHAR2, sqlset_owner IN VARCHAR2 := NULL); Parameters Table 169-21 DROP_SQLSET Procedure Parameters Parameter Description sqlset_name Specifies the name of the SQL tuning set. sqlset_owner Specifies the owner of the SQL tuning set, or NULL for current schema owner. Usage Notes You cannot drop a SQL tuning set when it is referenced by one or more clients.