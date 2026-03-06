---
id: 19c__ALL_MVIEW_DETAIL_RELATIONS
name: ALL_MVIEW_DETAIL_RELATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_DETAIL_RELATIONS.html
---

# ALL_MVIEW_DETAIL_RELATIONS

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| MVIEW_NAME | VARCHAR2(128) | Name of the materialized view |
| DETAILOBJ_OWNER | VARCHAR2(128) | Detail object owner |
| DETAILOBJ_NAME | VARCHAR2(128) | Detail object name (that is, the name of a table or view) |
| DETAILOBJ_TYPE | VARCHAR2(9) | Detail object type: TABLE VIEW SNAPSHOT CONTAINER UNDEFINED |
| DETAILOBJ_ALIAS | VARCHAR2(128) | Implicit or explicit alias for detail relation |
| DETAILOBJ_PCT | VARCHAR2(1) | Indicates whether the detail object PCT is supported ( Y ) or not ( N ) |
| NUM_FRESH_PCT_PARTITIONS | NUMBER | Number of fresh PCT partitions |
| NUM_STALE_PCT_PARTITIONS | NUMBER | Number of stale PCT partitions |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_MVIEW_DETAIL_RELATIONS describes all such detail relations defined for all materialized views in the database. USER_MVIEW_DETAIL_RELATIONS describes such detail relations defined for all materialized views owned by the current user. Note: All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as snapshots before Oracle8 i and that were never altered to enable query rewrite. Note: All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as snapshots before Oracle8 i and that were never altered to enable query rewrite. See Also: " DBA_MVIEW_DETAIL_RELATIONS " " USER_MVIEW_DETAIL_RELATIONS " See Also: " DBA_MVIEW_DETAIL_RELATIONS " " USER_MVIEW_DETAIL_RELATIONS "