---
id: 19c__DBMS_SQLTUNE.CREATE_SQLSET
name: DBMS_SQLTUNE.CREATE_SQLSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.CREATE_SQLSET

This procedure or function creates a SQL tuning set object in the database.

## Syntax

```sql
DBMS_SQLTUNE.CREATE_SQLSET (
   sqlset_name  IN  VARCHAR2,
   description  IN  VARCHAR2 := NULL
   sqlset_owner IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the created SQL tuning set. The name is the name passed to the function. If no name is passed to the function, then the function generates an automatic name. |
| description | VARCHAR2 | IN | Provides an optional description of the SQL tuning set. |
| sqlset_owner | VARCHAR2 | IN | Specifies the owner of the SQL tuning set, or NULL for the current schema owner. |

**Returns:** `UNKNOWN`

## Usage Notes

Syntax DBMS_SQLTUNE.CREATE_SQLSET ( sqlset_name IN VARCHAR2, description IN VARCHAR2 := NULL sqlset_owner IN VARCHAR2 := NULL); DBMS_SQLTUNE.CREATE_SQLSET ( sqlset_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, sqlset_owner IN VARCHAR2 := NULL) RETURN VARCHAR2; Parameters Table 169-15 CREATE_SQLSET Procedure Parameters Parameter Description sqlset_name Specifies the name of the created SQL tuning set. The name is the name passed to the function. If no name is passed to the function, then the function generates an automatic name. description Provides an optional description of the SQL tuning set. sqlset_owner Specifies the owner of the SQL tuning set, or NULL for the current schema owner. Examples EXEC DBMS_SQLTUNE.CREATE_SQLSET(- sqlset_name => 'my_workload', - description => 'complete application workload');