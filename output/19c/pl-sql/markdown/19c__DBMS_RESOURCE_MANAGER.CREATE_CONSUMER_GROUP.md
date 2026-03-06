---
id: 19c__DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP
name: DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP

This procedure creates entries which define resource consumer groups.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP (
   consumer_group  IN VARCHAR2,
   comment         IN VARCHAR2 DEFAULT NULL, 
   cpu_mth         IN VARCHAR2 DEFAULT NULL,
   mgmt_mth        IN VARCHAR2 DEFAULT 'ROUND-ROBIN',
   category        IN VARCHAR2 DEFAULT 'OTHER');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| consumer_group | VARCHAR2 | IN | Name of the consumer group |
| comment | VARCHAR2 | IN | User comment |
| cpu_mth | VARCHAR2 | IN | Name of CPU resource allocation method (deprecated) |
| mgmt_mth | VARCHAR2 | IN | Name of CPU resource allocation method |
| category | VARCHAR2 | IN | Describes the category of the consumer group. The primary purpose of this attribute is to support Exadata I/O Resource Manager category plans. The view DBA_RSRC_CATEGORIES defines the currently defined categories. Categories can be modified, using the CREATE_CATEGORY Procedure , UPDATE_CATEGORY Procedure , and DELETE_CATEGORY Procedure . |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.CREATE_CONSUMER_GROUP ( consumer_group IN VARCHAR2, comment IN VARCHAR2 DEFAULT NULL, cpu_mth IN VARCHAR2 DEFAULT NULL, mgmt_mth IN VARCHAR2 DEFAULT 'ROUND-ROBIN', category IN VARCHAR2 DEFAULT 'OTHER'); Parameters Table 142-8 CREATE_CONSUMER_GROUP Procedure Parameters Parameter Description consumer_group Name of the consumer group comment User comment cpu_mth Name of CPU resource allocation method (deprecated) mgmt_mth Name of CPU resource allocation method category Describes the category of the consumer group. The primary purpose of this attribute is to support Exadata I/O Resource Manager category plans. The view DBA_RSRC_CATEGORIES defines the currently defined categories. Categories can be modified, using the CREATE_CATEGORY Procedure , UPDATE_CATEGORY Procedure , and DELETE_CATEGORY Procedure .