---
id: 19c__ALL_DIM_CHILD_OF
name: ALL_DIM_CHILD_OF
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIM_CHILD_OF.html
---

# ALL_DIM_CHILD_OF

ALL_DIM_CHILD_OF describes hierarchical relationships of 1 to n between the pairs of levels in the dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| HIERARCHY_NAME | VARCHAR2(128) | Hierarchy name |
| POSITION | NUMBER | Hierarchical position within this hierarchy, position 1 being the most detailed |
| CHILD_LEVEL_NAME | VARCHAR2(128) | Child side of 1:n relationship |
| JOIN_KEY_ID | VARCHAR2(40) | If non-null, then the child joins to the parent |
| PARENT_LEVEL_NAME | VARCHAR2(128) | Parent side of 1:n relationship in relation to the CHILD_LEVEL_NAME |

## Usage Notes

Related Views DBA_DIM_CHILD_OF describes all such hierarchical relationships in the database. USER_DIM_CHILD_OF describes all such hierarchical attributes in the current user's schema. See Also: " DBA_DIM_CHILD_OF " " USER_DIM_CHILD_OF " See Also: " DBA_DIM_CHILD_OF " " USER_DIM_CHILD_OF "