---
id: 19c__DBMS_RESOURCE_MANAGER.DELETE_PLAN_CASCADE
name: DBMS_RESOURCE_MANAGER.DELETE_PLAN_CASCADE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.DELETE_PLAN_CASCADE

This procedure deletes the specified plan and all of its descendants (plan directives, subplans, consumer groups). Mandatory objects and directives are not deleted.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.DELETE_PLAN_CASCADE (
   plan IN VARCHAR2);
```

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.DELETE_PLAN_CASCADE ( plan IN VARCHAR2); Parameters Table 142-18 DELETE_PLAN_CASCADE Procedure Parameters Parameters Description plan Name of the plan Usage Notes If DELETE_PLAN_CASCADE encounters any error, then it rolls back the operation, and nothing is deleted.