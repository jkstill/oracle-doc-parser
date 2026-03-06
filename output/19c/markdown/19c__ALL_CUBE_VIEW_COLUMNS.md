---
id: 19c__ALL_CUBE_VIEW_COLUMNS
name: ALL_CUBE_VIEW_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_CUBE_VIEW_COLUMNS.html
---

# ALL_CUBE_VIEW_COLUMNS

ALL_CUBE_VIEW_COLUMNS describes the columns of the relational views of the OLAP cubes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube |
| CUBE_NAME | VARCHAR2(128) | Name of a cube, such as UNITS_CUBE |
| VIEW_NAME | VARCHAR2(128) | Name of a view of the cube, such as PRODUCT_VIEW |
| COLUMN_NAME | VARCHAR2(128) | Name of a column in the view, such as DIM_KEY or LEVEL_NAME |
| COLUMN_TYPE | VARCHAR2(7) | Type of the column: MEASURE KEY |
| OBJECT_NAME | VARCHAR2(128) | Name of the measure or dimension represented in the column |

## Usage Notes

Related Views DBA_CUBE_VIEW_COLUMNS describes the columns of relational views of all OLAP cubes in the database. USER_CUBE_VIEW_COLUMNS describes the columns of relational views of OLAP cubes owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_VIEW_COLUMNS " " USER_CUBE_VIEW_COLUMNS " See Also: " DBA_CUBE_VIEW_COLUMNS " " USER_CUBE_VIEW_COLUMNS "