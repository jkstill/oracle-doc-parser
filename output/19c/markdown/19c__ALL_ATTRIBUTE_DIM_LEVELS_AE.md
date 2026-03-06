---
id: 19c__ALL_ATTRIBUTE_DIM_LEVELS_AE
name: ALL_ATTRIBUTE_DIM_LEVELS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_LEVELS_AE.html
---

# ALL_ATTRIBUTE_DIM_LEVELS_AE

ALL_ATTRIBUTE_DIM_LEVELS_AE describes the levels of the attribute dimensions (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| LEVEL_NAME | VARCHAR2(128) | Name of the attribute dimension level |
| SKIP_WHEN_NULL | VARCHAR2(1) | Indicates whether to skip the level when the key is NULL; the value can be Y or N . |
| LEVEL_TYPE | VARCHAR2(10) | Type of attribute dimension level |
| MEMBER_NAME_EXPR | CLOB | Expression representing the level member name |
| MEMBER_CAPTION_EXPR | CLOB | Expression representing the level member caption, or NULL if not specified |
| MEMBER_DESCRIPTION_EXPR | CLOB | Expression representing the level member description, or NULL if not specified |
| ORDER_NUM | NUMBER | Order of the level in the list of attribute dimension levels |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the attribute dimension is defined |

## Usage Notes

Related Views DBA_ATTRIBUTE_DIM_LEVELS_AE describes the levels of all attribute dimensions (across all editions) in the database. USER_ATTRIBUTE_DIM_LEVELS_AE describes the levels of the attribute dimensions (across all editions) owned by the current user. This view does not display the OWNER column. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_LEVELS_AE " " USER_ATTRIBUTE_DIM_LEVELS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_LEVELS_AE " " USER_ATTRIBUTE_DIM_LEVELS_AE "