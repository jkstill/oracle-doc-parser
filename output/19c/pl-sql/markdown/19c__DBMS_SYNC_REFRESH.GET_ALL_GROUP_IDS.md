---
id: 19c__DBMS_SYNC_REFRESH.GET_ALL_GROUP_IDS
name: DBMS_SYNC_REFRESH.GET_ALL_GROUP_IDS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.GET_ALL_GROUP_IDS

This function returns the group IDs of all the sync refresh groups in the database.

## Syntax

```sql
FUNCTION DBMS_SYNC_REFRESH.GET_ALL_GROUP_IDS
           RETURN DBMS_UTILITY.NUMBER_ARRAY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| get_all_group_ids | RETURN | IN | Returns the group IDs of all the sync refresh groups in the database. |

**Returns:** `DBMS_UTILITY.NUMBER_ARRAY`

## Usage Notes

Syntax FUNCTION DBMS_SYNC_REFRESH.GET_ALL_GROUP_IDS RETURN DBMS_UTILITY.NUMBER_ARRAY; Parameters Table 173-6 GET_ALL_GROUP_IDS Function Parameter Parameter Description get_all_group_ids Returns the group IDs of all the sync refresh groups in the database.