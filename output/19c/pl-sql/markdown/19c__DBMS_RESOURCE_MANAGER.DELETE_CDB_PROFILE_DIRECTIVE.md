---
id: 19c__DBMS_RESOURCE_MANAGER.DELETE_CDB_PROFILE_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.DELETE_CDB_PROFILE_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.DELETE_CDB_PROFILE_DIRECTIVE

This procedure deletes the performance profile directive of the consolidation resource plan. Once the directive is deleted, the pluggable databases (PDBs) that use the performance profile use the default resource allocation.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.DELETE_CDB_PROFILE_DIRECTIVE (
   plan          IN    VARCHAR2(32)   DEFAULT NULL,
   profile       IN    VARCHAR2(32)   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2(32) | IN | Name of the consolidation plan |
| profile | VARCHAR2(32) | IN | Name of the performance profile directive to be deleted |

## Usage Notes

For a PDB to use a performance profile, the PDB must have the DB_PERFORMANCE_PROFILE initialization parameter set to the performance profile name. Syntax DBMS_RESOURCE_MANAGER.DELETE_CDB_PROFILE_DIRECTIVE ( plan IN VARCHAR2(32) DEFAULT NULL, profile IN VARCHAR2(32) DEFAULT NULL); Parameters Table 142-15 DELETE_CDB_PROFILE_DIRECTIVE Procedure Parameters Parameter Description plan Name of the consolidation plan profile Name of the performance profile directive to be deleted Usage Notes This procedure can be run only from the CDB root ( CDB$ROOT ).