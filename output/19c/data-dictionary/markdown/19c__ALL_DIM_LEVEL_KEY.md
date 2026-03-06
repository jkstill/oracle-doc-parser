---
id: 19c__ALL_DIM_LEVEL_KEY
name: ALL_DIM_LEVEL_KEY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIM_LEVEL_KEY.html
---

# ALL_DIM_LEVEL_KEY

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| LEVEL_NAME | VARCHAR2(128) | Name of the hierarchy level |
| KEY_POSITION | NUMBER | Ordinal position of the key column within the level |
| COLUMN_NAME | VARCHAR2(128) | Name of the key column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_DIM_LEVEL_KEY describes all columns of dimension levels in the database. USER_DIM_LEVEL_KEY describes all columns of dimension levels owned by the current user. See Also: " DBA_DIM_LEVEL_KEY " " USER_DIM_LEVEL_KEY " See Also: " DBA_DIM_LEVEL_KEY " " USER_DIM_LEVEL_KEY "