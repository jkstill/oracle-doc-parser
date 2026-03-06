---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN
name: DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN

Creates entries which define consolidation resource plans.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN (
   plan                    IN    VARCHAR2(32), 
   comment                 IN    VARCHAR2(2000) DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2(32) | IN | Name of the consolidation plan |
| comment | VARCHAR2(2000) | IN | User comment |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN ( plan IN VARCHAR2(32), comment IN VARCHAR2(2000) DEFAULT NULL); Parameters Table 142-5 CREATE_CDB_PLAN Procedure Parameters Parameter Description plan Name of the consolidation plan comment User comment Usage Notes This procedure can be run only from the CDB root ( CDB$ROOT ).