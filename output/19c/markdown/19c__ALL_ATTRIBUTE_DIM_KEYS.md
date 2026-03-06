---
id: 19c__ALL_ATTRIBUTE_DIM_KEYS
name: ALL_ATTRIBUTE_DIM_KEYS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_KEYS.html
---

# ALL_ATTRIBUTE_DIM_KEYS

ALL_ATTRIBUTE_DIM_KEYS describes the keys of the attribute dimensions accessible to the current user.

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

## Usage Notes

Related Views DBA_ATTRIBUTE_DIM_KEYS describes the keys of all attribute dimensions in the database. USER_ATTRIBUTE_DIM_KEYS describes the keys of the attribute dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_ATTRIBUTE_DIM_KEYS " " USER_ATTRIBUTE_DIM_KEYS " See Also: " DBA_ATTRIBUTE_DIM_KEYS " " USER_ATTRIBUTE_DIM_KEYS "