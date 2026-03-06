---
id: 19c__ALL_MVIEW_AGGREGATES
name: ALL_MVIEW_AGGREGATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_AGGREGATES.html
---

# ALL_MVIEW_AGGREGATES

ALL_MVIEW_AGGREGATES describes the grouping functions (aggregate operations) that appear in the SELECT list of materialized aggregate views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| MVIEW_NAME | VARCHAR2(128) | Name of the materialized view |
| POSITION_IN_SELECT | NUMBER | Ordinal position of this aggregation within the SELECT list. For the position of nonaggregate elements of the select list, see " ALL_MVIEW_KEYS " . |
| CONTAINER_COLUMN | VARCHAR2(128) | Name of this column in the container table |
| AGG_FUNCTION | VARCHAR2(8) | Aggregation function |
| DISTINCTFLAG | VARCHAR2(1) | Indicates whether this aggregation is distinct ( Y ) or not ( N ) |
| MEASURE | LONG | SQL text of the measure, excluding the aggregation function. Equal to * for COUNT(*) . |

## Usage Notes

Related Views DBA_MVIEW_AGGREGATES describes all such grouping functions defined for all materialized views in the database. USER_MVIEW_AGGREGATES describes all such grouping functions defined for all materialized views owned by the current user. Note: All three views exclude materialized views that reference remote tables or that include references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as "snapshots" before Oracle8 i and that were never altered to enable query rewrite. Note: All three views exclude materialized views that reference remote tables or that include references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as "snapshots" before Oracle8 i and that were never altered to enable query rewrite. See Also: " DBA_MVIEW_AGGREGATES " " USER_MVIEW_AGGREGATES " See Also: " DBA_MVIEW_AGGREGATES " " USER_MVIEW_AGGREGATES "