---
id: 19c__ALL_HIER_HIER_ATTR_CLASS
name: ALL_HIER_HIER_ATTR_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIER_HIER_ATTR_CLASS.html
---

# ALL_HIER_HIER_ATTR_CLASS

ALL_HIER_HIER_ATTR_CLASS describes the classifications of the hierarchical attributes of the hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| HIER_ATTR_NAME | VARCHAR2(128) | Name of the hierarchical attribute |
| CLASSIFICATION | VARCHAR2(128) | Classification associated with the hierarchical attribute |
| VALUE | CLOB | Value associated with the classification or NULL if not specified |
| LANGUAGE | VARCHAR2(64) | NLS_LANGUAGE value associated with the classification or NULL if not specified |
| ORDER_NUM | NUMBER | Order of the classification in the list of classifications associated with the hierarchical attribute |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Related Views DBA_HIER_HIER_ATTR_CLASS describes the classifications of the hierarchical attributes of all hierarchies in the database. USER_HIER_HIER_ATTR_CLASS describes the classifications of the hierarchical attributes of the hierarchies owned by the current user. This view does not display the OWNER column. See Also: " DBA_HIER_HIER_ATTR_CLASS " " USER_HIER_HIER_ATTR_CLASS " See Also: " DBA_HIER_HIER_ATTR_CLASS " " USER_HIER_HIER_ATTR_CLASS "