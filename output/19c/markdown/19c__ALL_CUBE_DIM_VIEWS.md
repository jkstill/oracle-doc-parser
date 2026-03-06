---
id: 19c__ALL_CUBE_DIM_VIEWS
name: ALL_CUBE_DIM_VIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_CUBE_DIM_VIEWS.html
---

# ALL_CUBE_DIM_VIEWS

ALL_CUBE_DIM_VIEWS describes the relational views of the OLAP dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a cube dimension, such as PRODUCT |
| VIEW_NAME | VARCHAR2(128) | Name of a view of the cube dimension, such as PRODUCT_VIEW |

## Usage Notes

Related Views DBA_CUBE_DIM_VIEWS describes the relational views of all OLAP dimensions in the database. USER_CUBE_DIM_VIEWS describes the relational views of the OLAP dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_DIM_VIEWS " " USER_CUBE_DIM_VIEWS " See Also: " DBA_CUBE_DIM_VIEWS " " USER_CUBE_DIM_VIEWS "