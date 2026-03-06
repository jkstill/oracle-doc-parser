---
id: 19c__ALL_COL_COMMENTS
name: ALL_COL_COMMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_COL_COMMENTS.html
---

# ALL_COL_COMMENTS

ALL_COL_COMMENTS displays comments on the columns of the tables and views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the object |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| COMMENTS | VARCHAR2(4000) | Comment on the column |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs n : This value is used for rows containing data that originate in the container with the ID n ( n =1 if the data originates in root) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_COL_COMMENTS displays comments on the columns of all tables and views in the database. USER_COL_COMMENTS displays comments on the columns of the tables and views owned by the current user. This view does not display the OWNER column. See Also: " DBA_COL_COMMENTS " " USER_COL_COMMENTS " See Also: " DBA_COL_COMMENTS " " USER_COL_COMMENTS "