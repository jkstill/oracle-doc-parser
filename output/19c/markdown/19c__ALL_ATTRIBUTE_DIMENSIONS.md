---
id: 19c__ALL_ATTRIBUTE_DIMENSIONS
name: ALL_ATTRIBUTE_DIMENSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIMENSIONS.html
---

# ALL_ATTRIBUTE_DIMENSIONS

ALL_ATTRIBUTE_DIMENSIONS describes the attribute dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| DIMENSION_TYPE | VARCHAR2(8) | Type of the attribute dimension: TIME STANDARD |
| ALL_MEMBER_NAME | CLOB) | An expression for the name of the ALL member for the attribute dimension |
| ALL_MEMBER_CAPTION | CLOB | An expression for the caption for the ALL member of the attribute dimension, or NULL if not specified |
| ALL_MEMBER_DESCRIPTION | CLOB | An expression for the description for the ALL member of the attribute dimension |
| COMPILE_STATE | VARCHAR2(7) | Compile status of the attribute dimension: VALID INVALID |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Related Views DBA_ATTRIBUTE_DIMENSIONS describes all attribute dimensions in the database. USER_ATTRIBUTE_DIMENSIONS describes the attribute dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_ATTRIBUTE_DIMENSIONS " " USER_ATTRIBUTE_DIMENSIONS " See Also: " DBA_ATTRIBUTE_DIMENSIONS " " USER_ATTRIBUTE_DIMENSIONS "