---
id: 19c__ALL_MVIEW_JOINS
name: ALL_MVIEW_JOINS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_JOINS.html
---

# ALL_MVIEW_JOINS

ALL_MVIEW_JOINS describes joins between two columns in the WHERE clause of the subquery that defines a materialized view accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| MVIEW_NAME | VARCHAR2(128) | Materialized view name |
| DETAILOBJ1_OWNER | VARCHAR2(128) | Owner of the first object in the join Foot 1 |
| DETAILOBJ1_RELATION | VARCHAR2(128) | Name of the first object in the join Foot 1 |
| DETAILOBJ1_COLUMN | VARCHAR2(128) | Join column of the first object in the join Foot 1 |
| OPERATOR | CHAR(1) | Join operator Foot 1 |
| OPERATOR_TYPE | VARCHAR2(1) | Indicates whether the join is an inner join ( I ) or the DETAILOBJ1 table is the left side of an outer join ( L ) Foot 1 |
| DETAILOBJ2_OWNER | VARCHAR2(128) | Owner of the second object in the join Foot 1 |
| DETAILOBJ2_RELATION | VARCHAR2(128) | Name of the second object in the join Foot 1 |
| DETAILOBJ2_COLUMN | VARCHAR2(128) | Join column of the second object in the join Foot 1 |

## Usage Notes

Related Views DBA_MVIEW_JOINS describes all such joins for all materialized views in the database. USER_MVIEW_JOINS describes such joins for all materialized views owned by the current user. Note: All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as "snapshots" before Oracle8 i and that were never altered to enable query rewrite. Note: All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as SYSDATE or USER . These views also exclude materialized views that were created as "snapshots" before Oracle8 i and that were never altered to enable query rewrite. See Also: " DBA_MVIEW_JOINS " " USER_MVIEW_JOINS " See Also: " DBA_MVIEW_JOINS " " USER_MVIEW_JOINS "