---
id: 19c__ALL_HIER_LEVEL_ID_ATTRS_AE
name: ALL_HIER_LEVEL_ID_ATTRS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIER_LEVEL_ID_ATTRS_AE.html
---

# ALL_HIER_LEVEL_ID_ATTRS_AE

ALL_HIER_LEVEL_ID_ATTRS_AE describes the attributes that uniquely identify members of the levels of the hierarchies (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| LEVEL_NAME | VARCHAR2(128) | Name of hierarchy level |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the unique identifier attribute |
| ORDER_NUM | NUMBER | Order of the level in the list of unique identifier attributes for the level |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the hierarchy is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_HIER_LEVEL_ID_ATTRS_AE describes the attributes that uniquely identify members of the levels of all hierarchies (across all editions) in the database. USER_HIER_LEVEL_ID_ATTRS_AE describes the attributes that uniquely identify members of the levels of the hierarchies (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_HIER_LEVEL_ID_ATTRS_AE " " USER_HIER_LEVEL_ID_ATTRS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_HIER_LEVEL_ID_ATTRS_AE " " USER_HIER_LEVEL_ID_ATTRS_AE "