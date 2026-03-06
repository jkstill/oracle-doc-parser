---
id: 19c__ALL_HIER_CLASS
name: ALL_HIER_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIER_CLASS.html
---

# ALL_HIER_CLASS

ALL_HIER_CLASS describes the classifications of the hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| CLASSIFICATION | VARCHAR2(128) | Classification associated with the hierarchy |
| VALUE | CLOB | Value of the classification or NULL if not specified |
| LANGUAGE | VARCHAR2(64) | NLS_LANGUAGE value associated with the classification or NULL if not specified |
| ORDER_NUM | NUMBER | Order of the classification in the list of classifications associated with the hierarchy |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Related Views DBA_HIER_CLASS describes the classifications of all hierarchies in the database. USER_HIER_CLASS describes the classifications of the hierarchies owned by the current user. This view does not display the OWNER column. See Also: " DBA_HIER_CLASS " " USER_HIER_CLASS " See Also: " DBA_HIER_CLASS " " USER_HIER_CLASS "