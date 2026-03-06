---
id: 19c__DBMS_RESOURCE_MANAGER.UPDATE_CONSUMER_GROUP
name: DBMS_RESOURCE_MANAGER.UPDATE_CONSUMER_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.UPDATE_CONSUMER_GROUP

This procedure updates entries which define resource consumer groups.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.UPDATE_CONSUMER_GROUP (
   consumer_group  IN VARCHAR2, 
   new_comment     IN VARCHAR2 DEFAULT NULL, 
   new_cpu_mth     IN VARCHAR2 DEFAULT NULL,
   new_mgmt_mth    IN VARCHAR2 DEFAULT NULL,
   new_category    IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| consumer_group | VARCHAR2 | IN | Name of consumer group |
| new_comment | VARCHAR2 | IN | New user comment |
| new_cpu_mth | VARCHAR2 | IN | Name of new method for CPU resource allocation (deprecated) |
| new_mgmt_mth | VARCHAR2 | IN | Name of new method for CPU resource allocation |
| new_category | VARCHAR2 | IN | New consumer group category |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.UPDATE_CONSUMER_GROUP ( consumer_group IN VARCHAR2, new_comment IN VARCHAR2 DEFAULT NULL, new_cpu_mth IN VARCHAR2 DEFAULT NULL, new_mgmt_mth IN VARCHAR2 DEFAULT NULL, new_category IN VARCHAR2 DEFAULT NULL); Parameters Table 142-33 UPDATE_CONSUMER_GROUP Procedure Parameter Parameter Description consumer_group Name of consumer group new_comment New user comment new_cpu_mth Name of new method for CPU resource allocation (deprecated) new_mgmt_mth Name of new method for CPU resource allocation new_category New consumer group category Usage Notes If the parameters to the UPDATE_CONSUMER_GROUP procedure are not specified, then they remain unchanged in the data dictionary. To clear (reset to the directive's default value), use the value -1 .