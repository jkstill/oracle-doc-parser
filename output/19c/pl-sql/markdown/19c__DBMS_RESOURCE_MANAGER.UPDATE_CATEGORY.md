---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_CATEGORY
name: DBMS_RESOURCE_MANAGER.UPDATE_CATEGORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_CATEGORY

This procedure updates an existing resource consumer group category.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_CATEGORY (
   category        IN    VARCHAR2,
   new_comment     IN    VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category | VARCHAR2 | IN | Name of consumer group category |
| new_comment | VARCHAR2 | IN | User comment |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.UPDATE_CATEGORY ( category IN VARCHAR2, new_comment IN VARCHAR2 DEFAULT NULL); Parameters Table 142-27 UPDATE_CATEGORY Procedure Parameters Parameter Description category Name of consumer group category new_comment User comment Usage Notes To clear (reset to the directive's default value), use the value -1 .