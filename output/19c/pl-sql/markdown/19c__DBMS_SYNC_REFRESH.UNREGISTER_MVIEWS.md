---
id: 19c__DBMS_SYNC_REFRESH.UNREGISTER_MVIEWS
name: DBMS_SYNC_REFRESH.UNREGISTER_MVIEWS
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SYNC_REFRESH
tags: [dbms_sync_refresh]
source_file: DBMS_SYNC_REFRESH.html
---

# DBMS_SYNC_REFRESH.UNREGISTER_MVIEWS

This procedure unregisters a list of materialized views from synchronous refresh. Once a materialized view is unregistered, it can be maintained by the user with any of the traditional refresh methods, such as complete or PCT, refresh.

## Syntax

```sql
DBMS_SYNC_REFRESH.UNREGISTER_MVIEWS (
   mv_list   IN VARCHAR20;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mv_list | VARCHAR20 | IN | A comma-delimited list of materialized views to unregister. These names are optionally schema-qualified. |

## Usage Notes

Syntax DBMS_SYNC_REFRESH.UNREGISTER_MVIEWS ( mv_list IN VARCHAR20; Parameter Table 173-14 UNREGISTER_MVIEWS Parameter Parameter Description mv_list A comma-delimited list of materialized views to unregister. These names are optionally schema-qualified.