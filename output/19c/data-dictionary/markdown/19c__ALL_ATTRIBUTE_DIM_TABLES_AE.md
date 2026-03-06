---
id: 19c__ALL_ATTRIBUTE_DIM_TABLES_AE
name: ALL_ATTRIBUTE_DIM_TABLES_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_TABLES_AE.html
---

# ALL_ATTRIBUTE_DIM_TABLES_AE

ALL_ATTRIBUTE_DIM_TABLES_AE describes the tables used by the attribute dimensions (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of table used by the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| TABLE_OWNER | VARCHAR2(128) | Owner of the table or view used by the attribute dimension |
| TABLE_NAME | VARCHAR2(128) | Name of the table or view used by the attribute dimension |
| TABLE_ALIAS | VARCHAR2(128) | Alias specified for the table or view; if not specified, the name of the table or view |
| ORDER_NUM | NUMBER | Order of the table in the list of tables in the USING clause |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the attribute dimension is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ATTRIBUTE_DIM_TABLES_AE describes the tables used by all attribute dimensions (across all editions) in the database. USER_ATTRIBUTE_DIM_TABLES_AE describes the tables used by the attribute dimensions (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_TABLES_AE " " USER_ATTRIBUTE_DIM_TABLES_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_TABLES_AE " " USER_ATTRIBUTE_DIM_TABLES_AE "