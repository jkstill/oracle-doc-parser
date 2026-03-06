---
id: 19c__DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE

This procedure deletes the plan directives of the consolidation resource plan. Once the plan directive is deleted, the pluggable database will get the default resource allocation.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE (
   plan                    IN    VARCHAR2(32)   DEFAULT NULL,
   pluggable_database      IN    VARCHAR2(32)   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2(32) | IN | Name of the consolidation plan |
| pluggable_database | VARCHAR2(32) | IN | Name of the pluggable database in which the plan directive is to be deleted |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.DELETE_CDB_PLAN_DIRECTIVE ( plan IN VARCHAR2(32) DEFAULT NULL, pluggable_database IN VARCHAR2(32) DEFAULT NULL); Parameters Table 142-14 DELETE_CDB_PLAN_DIRECTIVE Procedure Parameters Parameter Description plan Name of the consolidation plan pluggable_database Name of the pluggable database in which the plan directive is to be deleted Usage Notes This procedure can be run only from the CDB root ( CDB$ROOT ).