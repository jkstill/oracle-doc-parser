---
id: 19c__DBMS_PDB_ALTER_SHARING.SET_ROLE_EXPLICIT
name: DBMS_PDB_ALTER_SHARING.SET_ROLE_EXPLICIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB_ALTER_SHARING
tags: [dbms_pdb_alter_sharing]
source_file: DBMS_PDB_ALTER_SHARING.html
---

# DBMS_PDB_ALTER_SHARING.SET_ROLE_EXPLICIT

This procedure sets a role as an application common role in an application container. This procedure is intended for migrating a role from a previous release to an application container in the current release.

## Syntax

```sql
DBMS_PDB_ALTER_SHARING.SET_ROLE_EXPLICIT (
   role_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| role_name | VARCHAR2) | IN | The name of the role. |

## Usage Notes

This procedure must be invoked in an application install, patch, upgrade, or uninstall operation in an application root. Syntax DBMS_PDB_ALTER_SHARING.SET_ROLE_EXPLICIT ( role_name IN VARCHAR2); Parameters Table 125-7 SET_ROLE_EXPLICIT Procedure Parameters Parameter Description role_name The name of the role. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container.