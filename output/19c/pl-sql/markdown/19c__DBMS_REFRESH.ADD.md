---
id: 19c__DBMS_REFRESH.ADD
name: DBMS_REFRESH.ADD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REFRESH
tags: [dbms_refresh]
source_file: DBMS_REFRESH.html
---

# DBMS_REFRESH.ADD

This procedure adds materialized views to a refresh group.

## Syntax

```sql
DBMS_REFRESH.ADD (
   name     IN VARCHAR2,
   { list   IN VARCHAR2, 
   | tab    IN DBMS_UTILITY.UNCL_ARRAY, }
   lax      IN BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the refresh group to which you want to add members, specified as [ schema_name .] refresh_group_name . If the schema is not specified, then the current user is the default. |
| list | VARCHAR2 | IN | Comma-delimited list of materialized views that you want to add to the refresh group. Synonyms are not supported. Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. |
| tab | DBMS_UTILITY.UNCL_ARRAY | IN | Instead of a comma-delimited list, you can supply a PL/SQL associative array of type DBMS_UTILITY.UNCL_ARRAY , where each element is the name of a materialized view. The first materialized view should be in position 1. The last position must be NULL . Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. |
| lax | BOOLEAN | IN | A materialized view can belong to only one refresh group at a time. If you are moving a materialized view from one group to another, then you must set the lax flag to TRUE to succeed. Oracle then automatically removes the materialized view from the other refresh group and updates its refresh interval to be that of its new group. Otherwise, the call to ADD generates an error message. |

## Usage Notes

Syntax DBMS_REFRESH.ADD ( name IN VARCHAR2, { list IN VARCHAR2, | tab IN DBMS_UTILITY.UNCL_ARRAY, } lax IN BOOLEAN := FALSE); Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Parameters Table 139-2 ADD Procedure Parameters Parameter Description name Name of the refresh group to which you want to add members, specified as [ schema_name .] refresh_group_name . If the schema is not specified, then the current user is the default. list Comma-delimited list of materialized views that you want to add to the refresh group. Synonyms are not supported. Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. tab Instead of a comma-delimited list, you can supply a PL/SQL associative array of type DBMS_UTILITY.UNCL_ARRAY , where each element is the name of a materialized view. The first materialized view should be in position 1. The last position must be NULL . Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. lax A materialized view can belong to only one refresh group at a time. If you are moving a materialized view from one group to another, then you must set the lax flag to TRUE to succeed. Oracle then automatically removes the materialized view from the other refresh group and updates its refresh interval to be that of its new group. Otherwise, the call to ADD generates an error message.