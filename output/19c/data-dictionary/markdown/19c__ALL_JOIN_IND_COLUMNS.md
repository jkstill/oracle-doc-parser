---
id: 19c__ALL_JOIN_IND_COLUMNS
name: ALL_JOIN_IND_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_JOIN_IND_COLUMNS.html
---

# ALL_JOIN_IND_COLUMNS

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_OWNER | VARCHAR2(128) | Owner of the bitmap join index |
| INDEX_NAME | VARCHAR2(128) | Name of the bitmap join index |
| INNER_TABLE_OWNER | VARCHAR2(128) | Owner of the fact table |
| INNER_TABLE_NAME | VARCHAR2(128) | Name of the fact table |
| INNER_TABLE_COLUMN | VARCHAR2(128) | Name of the fact table join column |
| OUTER_TABLE_OWNER | VARCHAR2(128) | Owner of the dimension table |
| OUTER_TABLE_NAME | VARCHAR2(128) | Name of the dimension table |
| OUTER_TABLE_COLUMN | VARCHAR2(128) | Name of the dimension table join column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_JOIN_IND_COLUMNS describes all join conditions in the database. USER_JOIN_IND_COLUMNS describes the join conditions owned by the current user. This view does not display the INDEX_OWNER column. See Also: " DBA_JOIN_IND_COLUMNS " " USER_JOIN_IND_COLUMNS " See Also: " DBA_JOIN_IND_COLUMNS " " USER_JOIN_IND_COLUMNS "