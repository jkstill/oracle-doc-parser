---
id: 19c__ALL_MVIEW_DETAIL_PARTITION
name: ALL_MVIEW_DETAIL_PARTITION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_DETAIL_PARTITION.html
---

# ALL_MVIEW_DETAIL_PARTITION

ALL_MVIEW_DETAIL_PARTITION displays freshness information, with respect to partition change tracking (PCT) detail partitions, for the materialized views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| MVIEW_NAME | VARCHAR2(128) | Name of the materialized view |
| DETAILOBJ_OWNER | VARCHAR2(128) | Owner of the detail object |
| DETAILOBJ_NAME | VARCHAR2(128) | Name of the detail object |
| DETAIL_PARTITION_NAME | VARCHAR2(128) | Name of the detail object partition |
| DETAIL_PARTITION_POSITION | NUMBER | Position of the detail object partition |
| FRESHNESS | VARCHAR2(7) | Freshness state of the detail object logical partition. Possible values: FRESH STALE UNKNOWN |
| LAST_REFRESH_TIME Foot 1 | DATE | Date and time at which the materialized view was last refreshed |

## Usage Notes

Related Views DBA_MVIEW_DETAIL_PARTITION displays freshness information, with respect to PCT detail partitions, for all materialized views in the database. USER_MVIEW_DETAIL_PARTITION displays freshness information, with respect to PCT detail partitions, for the materialized views owned by the current user. See Also: " DBA_MVIEW_DETAIL_PARTITION " " USER_MVIEW_DETAIL_PARTITION " See Also: " DBA_MVIEW_DETAIL_PARTITION " " USER_MVIEW_DETAIL_PARTITION "