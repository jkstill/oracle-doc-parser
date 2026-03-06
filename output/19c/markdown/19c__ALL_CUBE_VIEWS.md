---
id: 19c__ALL_CUBE_VIEWS
name: ALL_CUBE_VIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_CUBE_VIEWS.html
---

# ALL_CUBE_VIEWS

ALL_CUBE_VIEWS describes the relational views of the OLAP cubes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube |
| CUBE_NAME | VARCHAR2(128) | Name of a cube, such as UNITS_CUBE |
| VIEW_NAME | VARCHAR2(128) | Name of a view of the cube, such as UNITS_CUBE_VIEW |

## Usage Notes

Related Views DBA_CUBE_VIEWS describes the relational views of all OLAP cubes in the database. USER_CUBE_VIEWS describes the relational views of the OLAP cubes owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_VIEWS " " USER_CUBE_VIEWS " See Also: " DBA_CUBE_VIEWS " " USER_CUBE_VIEWS "