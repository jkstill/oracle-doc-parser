---
id: 19c__ALL_MVIEW_KEYS
name: ALL_MVIEW_KEYS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_KEYS.html
---

# ALL_MVIEW_KEYS

ALL_MVIEW_KEYS describes the columns or expressions in the SELECT list upon which materialized views accessible to the current user are based.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| MVIEW_NAME | VARCHAR2(128) | Materialized view name |
| POSITION_IN_SELECT | NUMBER | Ordinal position of this key within the SELECT list |
| CONTAINER_COLUMN | VARCHAR2(128) | Name of the column in the container table |
| DETAILOBJ_OWNER | VARCHAR2(128) | Detail object owner |
| DETAILOBJ_NAME | VARCHAR2(128) | Detail object name (for example, the name of a table or view) |
| DETAILOBJ_ALIAS | VARCHAR2(128) | Implicit or explicit alias for detail relation |
| DETAILOBJ_TYPE | VARCHAR2(5) | Detail object type: TABLE VIEW |
| DETAILOBJ_COLUMN | VARCHAR2(128) | Name of the detail relation column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_MVIEW_KEYS describes such columns and expressions for all materialized views in the database. USER_MVIEW_KEYS describes such columns and expressions for all materialized views owned by the current user. Note: All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as snapshots before Oracle8 i and that were never altered to enable query rewrite. Note: All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as snapshots before Oracle8 i and that were never altered to enable query rewrite. See Also: " DBA_MVIEW_KEYS " " USER_MVIEW_KEYS "