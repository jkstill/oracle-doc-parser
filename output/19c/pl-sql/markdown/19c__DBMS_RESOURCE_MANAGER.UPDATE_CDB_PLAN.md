---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN
name: DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN

This procedure updates the consolidation resource plan.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN (
   plan                        IN    VARCHAR2(32), 
   new_comment                 IN    VARCHAR2(2000)   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2(32) | IN | Name of the consolidation plan |
| new_comment | VARCHAR2(2000) | IN | User comment |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.UPDATE_CDB_PLAN ( plan IN VARCHAR2(32), new_comment IN VARCHAR2(2000) DEFAULT NULL); Parameters Table 142-30 UPDATE_CDB_PLAN Procedure Parameters Parameter Description plan Name of the consolidation plan new_comment User comment Usage Notes This procedure can be run only from the CDB root ( CDB$ROOT ). To clear (reset to the directive's default value), use the value -1 .