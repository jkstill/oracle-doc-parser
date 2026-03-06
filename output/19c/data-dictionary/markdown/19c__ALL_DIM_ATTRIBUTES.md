---
id: 19c__ALL_DIM_ATTRIBUTES
name: ALL_DIM_ATTRIBUTES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIM_ATTRIBUTES.html
---

# ALL_DIM_ATTRIBUTES

Related Views

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the dimension |
| DIMENSION_NAME | VARCHAR2(128) | Name of the dimension |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the attribute |
| LEVEL_NAME | VARCHAR2(128) | Name of the hierarchy level |
| COLUMN_NAME | VARCHAR2(128) | Dependent column name |
| INFERRED | CHAR(1) | Indicates whether the attribute is inferred from a JOIN KEY specification ( Y ) or not ( N ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_DIM_ATTRIBUTES describes all such dimension relationships in the database. USER_DIM_ATTRIBUTES describes all such dimension attributes in the current user's schema. See Also: " DBA_DIM_ATTRIBUTES " " USER_DIM_ATTRIBUTES " See Also: " DBA_DIM_ATTRIBUTES " " USER_DIM_ATTRIBUTES "