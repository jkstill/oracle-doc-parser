---
id: 19c__DBMS_REFRESH.SUBTRACT
name: DBMS_REFRESH.SUBTRACT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_REFRESH
tags: [dbms_refresh]
source_file: DBMS_REFRESH.html
---

# DBMS_REFRESH.SUBTRACT

This procedure removes materialized views from a refresh group.

## Syntax

```sql
DBMS_REFRESH.SUBTRACT (
   name      IN    VARCHAR2,
   { list    IN    VARCHAR2,
   | tab     IN    DBMS_UTILITY.UNCL_ARRAY, }
   lax       IN    BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the refresh group from which you want to remove members, specified as [ schema_name .] refresh_group_name . If the schema is not specified, then the current user is the default. |
| list | VARCHAR2 | IN | Comma-delimited list of materialized views that you want to remove from the refresh group. (Synonyms are not supported.) These materialized views can be located in different schemas and have different master tables or master materialized views. However, all of the listed materialized views must be in your current database. Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. |
| tab | DBMS_UTILITY.UNCL_ARRAY | IN | Instead of a comma-delimited list, you can supply a PL/SQL associative array of type DBMS_UTILITY.UNCL_ARRAY , where each element is the name of a materialized view. The first materialized view should be in position 1. The last position must be NULL . Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. |
| lax | BOOLEAN | IN | Set this to FALSE if you want Oracle to generate an error message if the materialized view you are attempting to remove is not a member of the refresh group. |

## Usage Notes

Syntax DBMS_REFRESH.SUBTRACT ( name IN VARCHAR2, { list IN VARCHAR2, | tab IN DBMS_UTILITY.UNCL_ARRAY, } lax IN BOOLEAN := FALSE); Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Note: This procedure is overloaded. The list and tab parameters are mutually exclusive. Parameters Table 139-7 SUBTRACT Procedure Parameters Parameter Description name Name of the refresh group from which you want to remove members, specified as [ schema_name .] refresh_group_name . If the schema is not specified, then the current user is the default. list Comma-delimited list of materialized views that you want to remove from the refresh group. (Synonyms are not supported.) These materialized views can be located in different schemas and have different master tables or master materialized views. However, all of the listed materialized views must be in your current database. Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. tab Instead of a comma-delimited list, you can supply a PL/SQL associative array of type DBMS_UTILITY.UNCL_ARRAY , where each element is the name of a materialized view. The first materialized view should be in position 1. The last position must be NULL . Each materialized view is specified as [ schema_name .] materialized_view_name . If the schema is not specified, then the refresh group owner is the default. lax Set this to FALSE if you want Oracle to generate an error message if the materialized view you are attempting to remove is not a member of the refresh group.