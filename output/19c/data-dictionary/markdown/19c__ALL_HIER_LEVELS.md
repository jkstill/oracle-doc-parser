---
id: 19c__ALL_HIER_LEVELS
name: ALL_HIER_LEVELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIER_LEVELS.html
---

# ALL_HIER_LEVELS

ALL_HIER_LEVELS describes the levels of the hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| LEVEL_NAME | VARCHAR2(128) | Name of hierarchy level |
| ORDER_NUM | NUMBER | Order of the level in the list of hierarchy levels |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_HIER_LEVELS describes the levels of all hierarchies in the database. USER_HIER_LEVELS describes the levels of the hierarchies owned by the current user. This view does not display the OWNER column. See Also: " DBA_HIER_LEVELS " " USER_HIER_LEVELS " See Also: " DBA_HIER_LEVELS " " USER_HIER_LEVELS "