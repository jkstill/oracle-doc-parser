---
id: 19c__ALL_CUBE_HIERARCHIES
name: ALL_CUBE_HIERARCHIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_HIERARCHIES.html
---

# ALL_CUBE_HIERARCHIES

ALL_CUBE_HIERARCHIES describes the OLAP dimension hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of a dimension, such as TIME |
| HIERARCHY_NAME | VARCHAR2(128) | Name of a hierarchy for the dimension, such as CALENDAR |
| HIERARCHY_ID | NUMBER | ID of the hierarchy |
| HIERARCHY_TYPE | VARCHAR2(5) | Type of the hierarchy: LEVEL VALUE |
| DESCRIPTION | NVARCHAR2(300) | Description of the hierarchy in the session language |
| IS_RAGGED | NUMBER | Indicates whether ragged hierarchies are permitted in subsequent builds. User dimensions that are enabled for materialized views and Time dimensions are set to 0 . Builds then check the data for ragged hierarchies and fail if one is detected. When User dimensions are set to 1 , the builds do not check for ragged hierarchies. |
| IS_SKIP_LEVEL | NUMBER | Indicates whether skip-level hierarchies are permitted in subsequent builds. User dimensions that are enabled for materialized views and Time dimensions are set to 0 . Builds then check the data for skip-level hierarchies and fail if one is detected. When User dimensions are set to 1 , the builds do not check for skip-level hierarchies. |
| REFRESH_MVIEW_NAME | VARCHAR2(200) | Name of the Refresh Materialized View associated with the hierarchy |
| CUSTOM_ORDER | CLOB | The textual representation of the sort orderby clause used to load dimension members of the hierarchy into the AW |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CUBE_HIERARCHIES describes all OLAP dimension hierarchies in the database. USER_CUBE_HIERARCHIES describes the OLAP dimension hierarchies owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_HIERARCHIES " " USER_CUBE_HIERARCHIES " See Also: " DBA_CUBE_HIERARCHIES " " USER_CUBE_HIERARCHIES "