---
id: 19c__ALL_METADATA_PROPERTIES
name: ALL_METADATA_PROPERTIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_METADATA_PROPERTIES.html
---

# ALL_METADATA_PROPERTIES

ALL_METADATA_PROPERTIES describes OLAP metadata properties in the database that are accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the OLAP metadata property |
| OWNING_OBJECT_ID | NUMBER | Dictionary ID of the OLAP metadata property owner |
| OWNING_TYPE | VARCHAR2(23) | Owning type of the OLAP metadata property |
| PROPERTY_ID | NUMBER | Dictionary Id of the OLAP metadata property |
| PROPERTY_KEY | VARCHAR2(128) | Key of the OLAP metadata property |
| PROPERTY_VALUE | CLOB | Value of the OLAP metadata property |
| PROPERTY_ORDER | NUMBER | Order number of the OLAP metadata property |

## Usage Notes

Related Views DBA_METADATA_PROPERTIES describes OLAP metadata properties in the database. USER_METADATA_PROPERTIES describes OLAP metadata properties in the current user's schema. This view does not display the OWNER column. See Also: " DBA_METADATA_PROPERTIES " " USER_METADATA_PROPERTIES " See Also: " DBA_METADATA_PROPERTIES " " USER_METADATA_PROPERTIES "