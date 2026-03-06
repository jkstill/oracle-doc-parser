---
id: 19c__ALL_DIM_JOIN_KEY
name: ALL_DIM_JOIN_KEY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIM_JOIN_KEY.html
---

# ALL_DIM_JOIN_KEY

DBA_DIM_JOIN_KEY describes all such joins in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| DIM_KEY_ID | NUMBER | Join key ID (unique within a dimension) |
| LEVEL_NAME | VARCHAR2(128) | Name of the hierarchy level |
| KEY_POSITION | NUMBER | Ordinal position of the key column within the level |
| HIERARCHY_NAME | VARCHAR2(128) | Name of the hierarchy |
| CHILD_JOIN_OWNER | VARCHAR2(128) | Owner of the join column table |
| CHILD_JOIN_TABLE | VARCHAR2(128) | Name of the join column table |
| CHILD_JOIN_COLUMN | VARCHAR2(128) | Name of the join column |
| CHILD_LEVEL_NAME | VARCHAR2(128) | Name of the child hierarchy level of the join key |

## Usage Notes

Related Views DBA_DIM_JOIN_KEY describes all such joins in the database. USER_DIM_JOIN_KEY describes all such joins owned by the current user. See Also: " DBA_DIM_JOIN_KEY " " USER_DIM_JOIN_KEY " See Also: " DBA_DIM_JOIN_KEY " " USER_DIM_JOIN_KEY "