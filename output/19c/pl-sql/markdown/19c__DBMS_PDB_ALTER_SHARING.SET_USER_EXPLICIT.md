---
id: 19c__DBMS_PDB_ALTER_SHARING.SET_USER_EXPLICIT
name: DBMS_PDB_ALTER_SHARING.SET_USER_EXPLICIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB_ALTER_SHARING
tags: [dbms_pdb_alter_sharing]
source_file: DBMS_PDB_ALTER_SHARING.html
---

# DBMS_PDB_ALTER_SHARING.SET_USER_EXPLICIT

This procedure sets a local user as an application common user in an application container.

## Syntax

```sql
DBMS_PDB_ALTER_SHARING.SET_USER_EXPLICIT (
   user_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| user_name | VARCHAR2) | IN | The name of the user. |

## Usage Notes

This procedure must be invoked in an application install, patch, upgrade, or uninstall operation in an application root. Syntax DBMS_PDB_ALTER_SHARING.SET_USER_EXPLICIT ( user_name IN VARCHAR2); Parameters Table 125-8 SET_USER_EXPLICIT Procedure Parameters Parameter Description user_name The name of the user. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container.