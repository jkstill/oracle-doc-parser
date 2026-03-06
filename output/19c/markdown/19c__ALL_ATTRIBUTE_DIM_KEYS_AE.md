---
id: 19c__ALL_ATTRIBUTE_DIM_KEYS_AE
name: ALL_ATTRIBUTE_DIM_KEYS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_KEYS_AE.html
---

# ALL_ATTRIBUTE_DIM_KEYS_AE

ALL_ATTRIBUTE_DIM_KEYS_AE describes the keys of the attribute dimensions (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| LEVEL_NAME | VARCHAR2(128) | Name of the level of the key |
| IS_ALTERNATE | VARCHAR2(1) | Indicates whether the attribute dimension key is an alternate key ( Y ) or not ( N ) |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the key attribute |
| ATTR_ORDER_NUM | NUMBER | Order of the attribute in the list of attributes comprising the key |
| KEY_ORDER_NUM | NUMBER | Order of the key in the list of keys (if alternate keys are specified) |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the attribute dimension is defined |

## Usage Notes

Related Views DBA_ATTRIBUTE_DIM_KEYS_AE describes the keys of all attribute dimensions (across all editions) in the database. USER_ATTRIBUTE_DIM_KEYS_AE describes the keys of the attribute dimensions (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_KEYS_AE " " USER_ATTRIBUTE_DIM_KEYS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_KEYS_AE " " USER_ATTRIBUTE_DIM_KEYS_AE "