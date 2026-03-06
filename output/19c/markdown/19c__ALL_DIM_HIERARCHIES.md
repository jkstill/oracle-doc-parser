---
id: 19c__ALL_DIM_HIERARCHIES
name: ALL_DIM_HIERARCHIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIM_HIERARCHIES.html
---

# ALL_DIM_HIERARCHIES

ALL_DIM_HIERARCHIES describes all dimension hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| HIERARCHY_NAME | VARCHAR2(128) | Hierarchy name |

## Usage Notes

Related Views DBA_DIM_HIERARCHIES describes all such hierarchies in the database. USER_DIM_HIERARCHIES describes all such hierarchies owned by the current user. See Also: " DBA_DIM_HIERARCHIES " " USER_DIM_HIERARCHIES " See Also: " DBA_DIM_HIERARCHIES " " USER_DIM_HIERARCHIES "