---
id: 19c__DBMS_RESOURCE_MANAGER.DELETE_PLAN_DIRECTIVE
name: DBMS_RESOURCE_MANAGER.DELETE_PLAN_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.DELETE_PLAN_DIRECTIVE

This procedure deletes resource plan directives.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.DELETE_PLAN_DIRECTIVE (
   plan              IN VARCHAR2, 
   group_or_subplan  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| plan | VARCHAR2 | IN | Name of the resource plan |
| group_or_subplan | VARCHAR2) | IN | Name of the group or subplan |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.DELETE_PLAN_DIRECTIVE ( plan IN VARCHAR2, group_or_subplan IN VARCHAR2); Parameters Table 142-19 DELETE_PLAN_DIRECTIVE Procedure Parameters Parameter Description plan Name of the resource plan group_or_subplan Name of the group or subplan