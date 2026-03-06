---
id: 19c__DBMS_PDB.SET_PROFILE_EXPLICIT
name: DBMS_PDB.SET_PROFILE_EXPLICIT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PDB
tags: [dbms_pdb]
source_file: DBMS_PDB.html
---

# DBMS_PDB.SET_PROFILE_EXPLICIT

This procedure sets a profile as an application common profile in an application container. This procedure is intended for migrating a profile from a previous release to an application container in the current release.

## Syntax

```sql
DBMS_PDB.SET_PROFILE_EXPLICIT (
   profile_name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2) | IN | The name of the profile. |

## Usage Notes

This procedure must be invoked in an application install, patch, upgrade, or uninstall operation in an application root. Syntax DBMS_PDB.SET_PROFILE_EXPLICIT ( profile_name IN VARCHAR2); Parameters Table 124-11 SET_PROFILE_EXPLICIT Procedure Parameters Parameter Description profile_name The name of the profile. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container. See Also: Oracle Database Administrator’s Guide for information about migrating an application to an application container.