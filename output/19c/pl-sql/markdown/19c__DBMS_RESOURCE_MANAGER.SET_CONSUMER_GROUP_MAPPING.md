---
id: 19c__DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING
name: DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING

This procedure adds, deletes, or modifies entries that map sessions to consumer groups, based on the session's login and runtime attributes.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING(
   attribute        IN VARCHAR2, 
   value            IN VARCHAR2, 
   consumer_group   IN VARCHAR2 DEFAULT NULL);
```

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.SET_CONSUMER_GROUP_MAPPING( attribute IN VARCHAR2, value IN VARCHAR2, consumer_group IN VARCHAR2 DEFAULT NULL); Parameters Table 142-21 SET_CONSUMER_GROUP_MAPPING Procedure Parameters Parameters Description attribute Mapping attribute to add or modify. It can be one of the Constants listed. value Attribute value to match. This includes both absolute mapping and regular expressions. consumer_group Name of the mapped consumer group, or NULL to delete a mapping Usage Notes If no mapping exists for the given attribute and value, a mapping to the given consumer group will be created. If a mapping already exists for the given attribute and value, the mapped consumer group will be updated to the one given. If the consumer_group argument is NULL , then any mapping from the given attribute and value will be deleted. The subprogram supports simple regex expressions for the value parameter. It implements the same semantics as the SQL 'LIKE' operator. Specifically, it uses '%' as amulticharacter wildcard and '_' as a single character wildcard. The '\' character can be used to escape the wildcards. Note that wildcards can only be used if the attribute is one of the following: CLIENT_OS_USER CLIENT_PROGRAM CLIENT_MACHINE MODULE_NAME MODULE_NAME_ACTION SERVICE_MODULE SERVICE_MODULE_ACTION Consumer group mapping comparisons for DBMS_RESOURCE_MANAGER.CLIENT_PROGRAM are performed by stripping the @ sign and following characters from V$SESSION.PROGRAM before comparing it to the CLIENT_PROGRAM value supplied.