---
id: 19c__ALL_UNUSED_COL_TABS
name: ALL_UNUSED_COL_TABS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_UNUSED_COL_TABS.html
---

# ALL_UNUSED_COL_TABS

ALL_UNUSED_COL_TABS describes the tables accessible to the current user that contain unused columns.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| COUNT | NUMBER | Number of unused columns |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_UNUSED_COL_TABS describes all tables in the database that contain unused columns. USER_UNUSED_COL_TABS describes the tables owned by the current user that contain unused columns. This view does not display the OWNER column. See Also: " DBA_UNUSED_COL_TABS " " USER_UNUSED_COL_TABS " See Also: " DBA_UNUSED_COL_TABS " " USER_UNUSED_COL_TABS "