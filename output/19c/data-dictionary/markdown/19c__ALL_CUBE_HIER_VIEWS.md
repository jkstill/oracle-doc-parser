---
id: 19c__ALL_CUBE_HIER_VIEWS
name: ALL_CUBE_HIER_VIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_CUBE_HIER_VIEWS.html
---

# ALL_CUBE_HIER_VIEWS

ALL_CUBE_HIER_VIEWS describes the hierarchies for the OLAP cube dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a cube dimension, such as TIME |
| HIERARCHY_NAME | VARCHAR2(128) | Name of a hierarchy for the cube dimension, such as CALENDAR |
| VIEW_NAME | VARCHAR2(128) | Name of a view of the hierarchy, such as TIME_CALENDAR_VIEW |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CUBE_HIER_VIEWS describes the hierarchies for all OLAP cube dimensions in the database. USER_CUBE_HIER_VIEWS describes the hierarchies for the OLAP cube dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_HIER_VIEWS " " USER_CUBE_HIER_VIEWS " See Also: " DBA_CUBE_HIER_VIEWS " " USER_CUBE_HIER_VIEWS "