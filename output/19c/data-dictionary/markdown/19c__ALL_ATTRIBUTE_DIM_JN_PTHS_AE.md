---
id: 19c__ALL_ATTRIBUTE_DIM_JN_PTHS_AE
name: ALL_ATTRIBUTE_DIM_JN_PTHS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_JN_PTHS_AE.html
---

# ALL_ATTRIBUTE_DIM_JN_PTHS_AE

ALL_ATTRIBUTE_DIM_JN_PTHS_AE describes the join paths for the attribute dimensions (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| JOIN_PATH_NAME | VARCHAR2(128) | Name of the join path |
| ON_CONDITION | VARCHAR2(4000) | Join condition specified in the ON clause |
| ORDER_NUM | NUMBER | Order of the classification in the list of classifications associated with the attribute dimension |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the attribute dimension is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ATTRIBUTE_DIM_JN_PTHS_AE describes the join paths for all attribute dimensions (across all editions) in the database. USER_ATTRIBUTE_DIM_JN_PTHS_AE describes the join paths for the attribute dimensions (across all editions) owned by the current user. Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_JN_PTHS_AE " " USER_ATTRIBUTE_DIM_JN_PTHS_AE " Note: This view is available starting with Oracle Database release 19c, version 19.13. See Also: " DBA_ATTRIBUTE_DIM_JN_PTHS_AE " " USER_ATTRIBUTE_DIM_JN_PTHS_AE "