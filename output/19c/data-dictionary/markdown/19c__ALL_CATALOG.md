---
id: 19c__ALL_CATALOG
name: ALL_CATALOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [all]
source_file: ALL_CATALOG.html
---

# ALL_CATALOG

ALL_CATALOG displays the tables, clusters, views, synonyms, and sequences accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the TABLE , CLUSTER , VIEW , SYNONYM , SEQUENCE , or UNDEFINED |
| TABLE_NAME | VARCHAR2(128) | Name of the TABLE , CLUSTER , VIEW , SYNONYM , SEQUENCE , or UNDEFINED |
| TABLE_TYPE | VARCHAR2(11) | Type of the TABLE , CLUSTER , VIEW , SYNONYM , SEQUENCE , or UNDEFINED |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CATALOG displays all tables, clusters, views, synonyms, and sequences in the entire database. USER_CATALOG displays the tables, clusters, views, synonyms, and sequences in the current user's schema. This view does not display the OWNER column. See Also: " DBA_CATALOG " " USER_CATALOG " See Also: " DBA_CATALOG " " USER_CATALOG "