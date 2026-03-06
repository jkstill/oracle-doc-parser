---
id: 19c__DBMS_RESOURCE_MANAGER.DELETE_PLAN
name: DBMS_RESOURCE_MANAGER.DELETE_PLAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.DELETE_PLAN

This procedure deletes the specified plan as well as all the plan directives to which it refers.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.DELETE_PLAN (
   plan IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2) | IN | Name of the resource plan to delete |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.DELETE_PLAN ( plan IN VARCHAR2); Parameters Table 142-17 DELETE_PLAN Procedure Parameters Parameter Description plan Name of the resource plan to delete