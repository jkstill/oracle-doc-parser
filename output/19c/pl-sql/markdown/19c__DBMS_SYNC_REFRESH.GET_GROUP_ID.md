---
id: 19c__DBMS_SYNC_REFRESH.GET_GROUP_ID
name: DBMS_SYNC_REFRESH.GET_GROUP_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.GET_GROUP_ID

This function returns the group ID of a materialized view. The group ID identifies the sync refresh group the table belongs to. A sync refresh group is a group of related tables and their dependent materialized views which must be all refreshed together jointly to ensure consistency and correctness.

## Syntax

```sql
DBMS_SYNC_REFRESH.GET_GROUP_ID (
   object_name_list   IN VARCHAR2)
RETURN DBMS_UTILITY.NUMBER_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_name_list | VARCHAR2) | IN | The name of the materialized view. The name can be schema-qualified. |

**Returns:** `DBMS_UTILITY.NUMBER_ARRAY`

## Usage Notes

Syntax DBMS_SYNC_REFRESH.GET_GROUP_ID ( object_name_list IN VARCHAR2) RETURN DBMS_UTILITY.NUMBER_ARRAY; Parameters Table 173-7 GET_GROUP_ID Function Parameter Parameter Description object_name_list The name of the materialized view. The name can be schema-qualified.