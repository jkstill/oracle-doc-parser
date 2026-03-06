---
id: 19c__ALL_CUBE_DIMENSIONALITY
name: ALL_CUBE_DIMENSIONALITY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_DIMENSIONALITY.html
---

# ALL_CUBE_DIMENSIONALITY

ALL_CUBE_DIMENSIONALITY describes the dimension order for the OLAP cubes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cube |
| CUBE_NAME | VARCHAR2(128) | Name of a cube, such as UNITS_CUBE |
| DIMENSION_NAME | VARCHAR2(128) | Name of a dimension of the cube, such as PRODUCT |
| DIMENSIONALITY_NAME | VARCHAR2(200) | The name of a dimensionality of the cube. For example, a cube dimensioned by the PRODUCT dimension can have a product dimension named PRODUCT_DIM . |
| DIMENSIONALITY_ID | NUMBER | ID of the cube dimensionality |
| ORDER_NUM | NUMBER | Order number of the dimension in the cube |
| IS_SPARSE | NUMBER | Indicates whether the dimension is sparse in the cube ( 1 ) or not sparse ( 0 ) |
| ET_ATTR_PREFIX | VARCHAR2(200) | Specifies the prefix that will be added to the column names in the Materialized Views to ensure uniqueness. If the user does not specify an ET_ATTR_PREFIX for any dimensions in a cube, then they default in the pattern D1_ , D2_ , and so on. |

## Usage Notes

Related Views DBA_CUBE_DIMENSIONALITY describes the dimension order for all OLAP cubes in the database. USER_CUBE_DIMENSIONALITY describes the dimension order for the OLAP cubes owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_DIMENSIONALITY " " USER_CUBE_DIMENSIONALITY " See Also: " DBA_CUBE_DIMENSIONALITY " " USER_CUBE_DIMENSIONALITY "