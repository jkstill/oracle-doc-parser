---
id: 19c__ALL_DIM_LEVELS
name: ALL_DIM_LEVELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIM_LEVELS.html
---

# ALL_DIM_LEVELS

DBA_DIM_LEVELS describes all dimension levels in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| LEVEL_NAME | VARCHAR2(128) | Unique within a dimension |
| NUM_COLUMNS | NUMBER | Number of columns in the level definition |
| DETAILOBJ_OWNER | VARCHAR2(128) | Owner of the detail object that the keys of this level come from |
| DETAILOBJ_NAME | VARCHAR2(128) | Name of the table that the keys of this level come from |
| SKIP_WHEN_NULL | VARCHAR2(1) | Indicates whether the level is declared with the SKIP WHEN NULL clause ( Y ) or not ( N ) |

## Usage Notes

Related Views DBA_DIM_LEVELS describes all dimension levels in the database. USER_DIM_LEVELS describes the levels of all dimensions owned by the current user. See Also: " DBA_DIM_LEVELS " " USER_DIM_LEVELS " See Also: " DBA_DIM_LEVELS " " USER_DIM_LEVELS "