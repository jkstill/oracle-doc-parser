---
id: 19c__ALL_LOB_TEMPLATES
name: ALL_LOB_TEMPLATES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_LOB_TEMPLATES.html
---

# ALL_LOB_TEMPLATES

ALL_LOB_TEMPLATES describes the LOB subpartition templates accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USER_NAME | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| LOB_COL_NAME | VARCHAR2(4000) | Name of the LOB column |
| SUBPARTITION_NAME | VARCHAR2(132) | Name of the subpartition |
| LOB_SEGMENT_NAME | VARCHAR2(132) | Name of the LOB segment |
| TABLESPACE_NAME | VARCHAR2(30) | Tablespace name of the subpartition |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_LOB_TEMPLATES describes all LOB subpartition templates in the database. USER_LOB_TEMPLATES describes the LOB subpartition templates owned by the current user. This view does not display the USER_NAME column. See Also: " DBA_LOB_TEMPLATES " " USER_LOB_TEMPLATES " See Also: " DBA_LOB_TEMPLATES " " USER_LOB_TEMPLATES "