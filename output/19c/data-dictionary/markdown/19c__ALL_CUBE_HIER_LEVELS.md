---
id: 19c__ALL_CUBE_HIER_LEVELS
name: ALL_CUBE_HIER_LEVELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_HIER_LEVELS.html
---

# ALL_CUBE_HIER_LEVELS

ALL_CUBE_HIER_LEVELS describes the hierarchy levels for the OLAP cube dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a cube dimension, such as TIME |
| HIERARCHY_NAME | VARCHAR2(128) | Name of a hierarchy for the dimension, such as CALENDAR |
| LEVEL_NAME | VARCHAR2(128) | Name of the dimension level, such as MONTH |
| HIERARCHY_LEVEL_ID | NUMBER | ID of the hierarchy level |
| ORDER_NUM | NUMBER | Order number of the level within the hierarchy; 0 is the top level |
| DESCRIPTION | NVARCHAR2(300) | Description of the level in the session language |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CUBE_HIER_LEVELS describes the hierarchy levels for all OLAP cube dimensions in the database. USER_CUBE_HIER_LEVELS describes the hierarchy levels for the OLAP cube dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_HIER_LEVELS " " USER_CUBE_HIER_LEVELS " See Also: " DBA_CUBE_HIER_LEVELS " " USER_CUBE_HIER_LEVELS "