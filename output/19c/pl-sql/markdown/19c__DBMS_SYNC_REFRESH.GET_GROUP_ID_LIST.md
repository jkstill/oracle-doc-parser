---
id: 19c__DBMS_SYNC_REFRESH.GET_GROUP_ID_LIST
name: DBMS_SYNC_REFRESH.GET_GROUP_ID_LIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.GET_GROUP_ID_LIST

This function returns the group IDs of the tables in a given list of objects (materialized views).

## Syntax

```sql
DBMS_SYNC_REFRESH.GET_GROUP_ID_LIST (
   object_name_list   IN VARCHAR2)
RETURN DBMS_UTILITY.NUMBER_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name_list | VARCHAR2) | IN | A comma-separated list of object names (materialized views). Each name can be schema-qualified. |

**Returns:** `DBMS_UTILITY.NUMBER_ARRAY`

## Usage Notes

Syntax DBMS_SYNC_REFRESH.GET_GROUP_ID_LIST ( object_name_list IN VARCHAR2) RETURN DBMS_UTILITY.NUMBER_ARRAY; Parameters Table 173-8 GET_GROUP_ID_LIST Function Parameter Parameter Description object_name_list A comma-separated list of object names (materialized views). Each name can be schema-qualified.