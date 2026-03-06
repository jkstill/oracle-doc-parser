---
id: 19c__ALL_HIER_HIER_ATTRIBUTES_AE
name: ALL_HIER_HIER_ATTRIBUTES_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIER_HIER_ATTRIBUTES_AE.html
---

# ALL_HIER_HIER_ATTRIBUTES_AE

ALL_HIER_HIER_ATTRIBUTES_AE describes the hierarchical attributes of the hierarchies (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| HIER_ATTR_NAME | VARCHAR2(128) | Name of the hierarchical attribute |
| EXPRESSION | CLOB | The expression defining the hierarchical attribute value |
| ORDER_NUM | NUMBER | Order of the hierarchical attribute in the list of hierarchical attributes |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the hierarchy is defined |

## Usage Notes

Related Views DBA_HIER_HIER_ATTRIBUTES_AE describes the hierarchical attributes of all hierarchies (across all editions) in the database. USER_HIER_HIER_ATTRIBUTES_AE describes the hierarchical attributes of the hierarchies (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_HIER_HIER_ATTRIBUTES_AE " " USER_HIER_HIER_ATTRIBUTES_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_HIER_HIER_ATTRIBUTES_AE " " USER_HIER_HIER_ATTRIBUTES_AE "