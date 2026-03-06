---
id: 19c__ALL_CUBE_DIM_LEVELS
name: ALL_CUBE_DIM_LEVELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_DIM_LEVELS.html
---

# ALL_CUBE_DIM_LEVELS

ALL_CUBE_DIM_LEVELS describes the OLAP dimension levels accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a dimension, such as CUSTOMER |
| LEVEL_NAME | VARCHAR2(128) | Name of a level in the dimension, such as WAREHOUSE |
| LEVEL_ID | NUMBER | ID of the dimension level |
| DESCRIPTION | NVARCHAR2(300) | Description of the dimension level in the session language |

## Usage Notes

Related Views DBA_CUBE_DIM_LEVELS describes all OLAP dimension levels in the database. USER_CUBE_DIM_LEVELS describes the OLAP dimension levels owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_DIM_LEVELS " " USER_CUBE_DIM_LEVELS " See Also: " DBA_CUBE_DIM_LEVELS " " USER_CUBE_DIM_LEVELS "