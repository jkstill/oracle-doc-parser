---
id: 19c__ALL_DIMENSIONS
name: ALL_DIMENSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIMENSIONS.html
---

# ALL_DIMENSIONS

ALL_DIMENSIONS describes the dimension objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| INVALID | VARCHAR2(1) | Indicates whether the dimension is invalid ( Y ) or valid ( N ) |
| COMPILE_STATE | VARCHAR2(13) | Compile status of the dimension: INVALID NEEDS_COMPILE ERROR |
| REVISION | NUMBER | Dimension revision level |

## Usage Notes

Related Views DBA_DIMENSIONS describes all dimensions in the database. USER_DIMENSIONS describes the dimensions in the current user's schema. See Also: " DBA_DIMENSIONS " " USER_DIMENSIONS " See Also: " DBA_DIMENSIONS " " USER_DIMENSIONS "