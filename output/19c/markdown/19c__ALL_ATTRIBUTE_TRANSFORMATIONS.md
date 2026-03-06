---
id: 19c__ALL_ATTRIBUTE_TRANSFORMATIONS
name: ALL_ATTRIBUTE_TRANSFORMATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ATTRIBUTE_TRANSFORMATIONS.html
---

# ALL_ATTRIBUTE_TRANSFORMATIONS

ALL_ATTRIBUTE_TRANSFORMATIONS describes the transformation functions for the transformations accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TRANSFORMATION_ID | NUMBER | Unique identifier for the transformation |
| OWNER | VARCHAR2(128) | Owning user of the transformation |
| NAME | VARCHAR2(128) | Transformation name |
| FROM_TYPE | VARCHAR2(257) | Source type name |
| TO_TYPE | VARCHAR2(385) | Target type name |
| ATTRIBUTE | NUMBER | Target type attribute number |
| ATTRIBUTE_TRANSFORMATION | VARCHAR2(4000) | Transformation function for the attribute |

## Usage Notes

Related Views DBA_ATTRIBUTE_TRANSFORMATIONS describes the transformation functions for all transformations in the database. USER_ATTRIBUTE_TRANSFORMATIONS describes the transformation functions for the transformations owned by the current user. This view does not display the OWNER column. See Also: " DBA_ATTRIBUTE_TRANSFORMATIONS " " USER_ATTRIBUTE_TRANSFORMATIONS " See Also: " DBA_ATTRIBUTE_TRANSFORMATIONS " " USER_ATTRIBUTE_TRANSFORMATIONS "