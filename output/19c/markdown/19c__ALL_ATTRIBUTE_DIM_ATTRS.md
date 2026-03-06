---
id: 19c__ALL_ATTRIBUTE_DIM_ATTRS
name: ALL_ATTRIBUTE_DIM_ATTRS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_ATTRS.html
---

# ALL_ATTRIBUTE_DIM_ATTRS

ALL_ATTRIBUTE_DIM_ATTRS describes the attributes of the attribute dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the attribute dimension attribute |
| TABLE_ALIAS | VARCHAR2(128) | Alias of the table or view in the USING clause to which the column belongs |
| COLUMN_NAME | VARCHAR2(128) | Name of the column in the table or view on which the attribute is defined |
| ORDER_NUM | NUMBER | Order of the attribute in the list of attribute dimension attributes |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Related Views DBA_ATTRIBUTE_DIM_ATTRS describes the attributes of all attribute dimensions in the database. USER_ATTRIBUTE_DIM_ATTRS describes the attributes of the attribute dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_ATTRIBUTE_DIM_ATTRS " " USER_ATTRIBUTE_DIM_ATTRS " See Also: " DBA_ATTRIBUTE_DIM_ATTRS " " USER_ATTRIBUTE_DIM_ATTRS "