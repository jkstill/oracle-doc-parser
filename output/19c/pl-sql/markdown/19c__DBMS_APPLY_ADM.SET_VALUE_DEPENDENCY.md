---
id: 19c__DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY
name: DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLY_ADM
tags: [dbms_apply_adm]
source_file: DBMS_APPLY_ADM.html
---

# DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY

This procedure sets or removes a value dependency. A value dependency is a virtual dependency definition that defines a relationship between the columns of two or more tables.

## Syntax

```sql
DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY(
   dependency_name IN VARCHAR2,
   object_name     IN VARCHAR2,
   attribute_list  IN VARCHAR2);

DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY(
   dependency_name IN VARCHAR2,
   object_name     IN VARCHAR2,
   attribute_table IN DBMS_UTILITY.NAME_ARRAY);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dependency_name | VARCHAR2 | IN | The name of the value dependency. If a dependency with the specified name does not exist, then it is created. If a dependency with the specified name exists, then the specified object and attributes are added to the dependency. If NULL , an error is raised. |
| object_name | VARCHAR2 | IN | The name of the table, specified as [ schema_name .] table_name . For example, hr.employees . If the schema is not specified, then the current user is the default. If NULL and the specified dependency exists, then the dependency is removed. If NULL and the specified dependency does not exist, then an error is raised. If NULL , then attribute_list and attribute_table also must be NULL . |
| attribute_list | VARCHAR2) | IN | A comma-delimited list of column names in the table. There must be no spaces between entries. |
| attribute_table | DBMS_UTILITY.NAME_ARRAY) | IN | A PL/SQL associative array of type DBMS_UTILITY.NAME_ARRAY that contains names of columns in the table. The first column name should be at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. |

## Usage Notes

An apply component uses the name of a value dependencies to detect dependencies between row logical change records (row LCRs) that contain the columns defined in the value dependency. Value dependencies can define virtual foreign key relationships between tables, but, unlike foreign key relationships, value dependencies can involve more than two database objects. This procedure is overloaded. The attribute_list and attribute_table parameters are mutually exclusive. Syntax DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY( dependency_name IN VARCHAR2, object_name IN VARCHAR2, attribute_list IN VARCHAR2); DBMS_APPLY_ADM.SET_VALUE_DEPENDENCY( dependency_name IN VARCHAR2, object_name IN VARCHAR2, attribute_table IN DBMS_UTILITY.NAME_ARRAY); Parameters Table 21-28 SET_VALUE_DEPENDENCY Procedure Parameters Parameter Description dependency_name The name of the value dependency. If a dependency with the specified name does not exist, then it is created. If a dependency with the specified name exists, then the specified object and attributes are added to the dependency. If NULL , an error is raised. object_name The name of the table, specified as [ schema_name .] table_name . For example, hr.employees . If the schema is not specified, then the current user is the default. If NULL and the specified dependency exists, then the dependency is removed. If NULL and the specified dependency does not exist, then an error is raised. If NULL , then attribute_list and attribute_table also must be NULL . attribute_list A comma-delimited list of column names in the table. There must be no spaces between entries. attribute_table A PL/SQL associative array of type DBMS_UTILITY.NAME_ARRAY that contains names of columns in the table. The first column name should be at position 1, the second at position 2, and so on. The table does not need to be NULL terminated. Usage Notes The following usage notes apply to this procedure: The SET_VALUE_DEPENDENCY Procedure and XStream Outbound Servers The SET_VALUE_DEPENDENCY Procedure and XStream Inbound Servers The SET_VALUE_DEPENDENCY Procedure and XStream Outbound Servers This procedure has no effect on XStream outbound servers. The SET_VALUE_DEPENDENCY Procedure and XStream Inbound Servers This procedure functions the same way for apply processes and inbound servers.