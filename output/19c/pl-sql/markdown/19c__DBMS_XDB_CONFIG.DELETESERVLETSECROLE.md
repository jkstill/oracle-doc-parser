---
id: 19c__DBMS_XDB_CONFIG.DELETESERVLETSECROLE
name: DBMS_XDB_CONFIG.DELETESERVLETSECROLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.DELETESERVLETSECROLE

This procedure deletes the specified role from a servlet in the XDB configuration.

## Syntax

```sql
DBMS_XDB_CONFIG.DELETESERVLETSECROLE(
     servname    IN   VARCHAR2,     rolename    IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| servname | VARCHAR2 | IN | Servlet name |
| rolename | VARCHAR2) | IN | Name of the role to be deleted |

## Usage Notes

Syntax DBMS_XDB_CONFIG.DELETESERVLETSECROLE( servname IN VARCHAR2, rolename IN VARCHAR2); Parameters Table 196-16 DELETESERVLETSECROLE Procedure Parameters Parameter Description servname Servlet name rolename Name of the role to be deleted