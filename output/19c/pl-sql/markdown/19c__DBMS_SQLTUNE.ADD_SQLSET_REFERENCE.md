---
id: 19c__DBMS_SQLTUNE.ADD_SQLSET_REFERENCE
name: DBMS_SQLTUNE.ADD_SQLSET_REFERENCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.ADD_SQLSET_REFERENCE

This procedure adds a new reference to an existing SQL tuning set to indicate its use by a client.

## Syntax

```sql
DBMS_SQLTUNE.ADD_SQLSET_REFERENCE (
   sqlset_name  IN  VARCHAR2,
   description  IN  VARCHAR2 := NULL)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the SQL tuning set. |
| description | VARCHAR2 | IN | Provides an optional description of the usage of SQL tuning set. The description is truncated if longer than 256 characters. |
| sqlset_owner |  |  | Specifies the owner of the SQL tuning set, or NULL for the current schema owner. |

**Returns:** `NUMBER`

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.ADD_SQLSET_REFERENCE ( sqlset_name IN VARCHAR2, description IN VARCHAR2 := NULL) RETURN NUMBER; Parameters The parameters are identical for DBMS_SQLTUNE.ADD_SQLSET_REFERENCE and DBMS_SQLSET.ADD_REFERENCE . Table 169-10 ADD_SQLSET_REFERENCE and ADD_REFERENCE Function Parameters Parameter Description sqlset_name Specifies the name of the SQL tuning set. description Provides an optional description of the usage of SQL tuning set. The description is truncated if longer than 256 characters. sqlset_owner Specifies the owner of the SQL tuning set, or NULL for the current schema owner. Return Values The identifier of the added reference.