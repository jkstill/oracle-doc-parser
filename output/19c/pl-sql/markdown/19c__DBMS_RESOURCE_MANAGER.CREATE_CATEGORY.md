---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_CATEGORY
name: DBMS_RESOURCE_MANAGER.CREATE_CATEGORY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_CATEGORY

This procedure creates a new consumer group category. The primary purpose of this attribute is to support Exadata I/O Resource Manager category plans.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_CATEGORY (
   category    IN    VARCHAR2,
   comment     IN    VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| category | VARCHAR2 | IN | Name of consumer group category |
| comment | VARCHAR2 | IN | User comment |

## Usage Notes

The view DBA_RSRC_CATEGORIES defines the currently defined categories. The ADMINISTRATIVE , INTERACTIVE , BATCH , MAINTENANCE , and OTHER categories are available. Syntax DBMS_RESOURCE_MANAGER.CREATE_CATEGORY ( category IN VARCHAR2, comment IN VARCHAR2 DEFAULT NULL); Parameters Table 142-4 CREATE_CATEGORY Procedure Parameters Parameter Description category Name of consumer group category comment User comment