---
id: 19c__ALL_ATTRIBUTE_DIM_ORDER_ATTRS
name: ALL_ATTRIBUTE_DIM_ORDER_ATTRS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_DIM_ORDER_ATTRS.html
---

# ALL_ATTRIBUTE_DIM_ORDER_ATTRS

ALL_ATTRIBUTE_DIM_ORDER_ATTRS describes the order attributes of the attribute dimensions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the attribute dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension |
| LEVEL_NAME | VARCHAR2(128) | Name of the level to order or the name of the level that has the ORDER BY clause |
| AGG_FUNC | VARCHAR2(3) | Aggregation function of the ORDER BY clause: MIN MAX |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the order attribute |
| ORDER_NUM | NUMBER | Order number of the attribute in the list of order attributes |
| CRITERIA | VARCHAR2(4) | Criteria of the ordering, either ascending or descending: ASC DESC |
| NULLS_POSITION | VARCHAR2(5) | Position of ORDER BY values in the orderings: FIRST LAST |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ATTRIBUTE_DIM_ORDER_ATTRS describes the order attributes of all attribute dimensions in the database. USER_ATTRIBUTE_DIM_ORDER_ATTRS describes the order attributes of the attribute dimensions owned by the current user. This view does not display the OWNER column. See Also: " DBA_ATTRIBUTE_DIM_ORDER_ATTRS " " USER_ATTRIBUTE_DIM_ORDER_ATTRS " See Also: " DBA_ATTRIBUTE_DIM_ORDER_ATTRS " " USER_ATTRIBUTE_DIM_ORDER_ATTRS "