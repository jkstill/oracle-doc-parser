---
id: 19c__ALL_TRANSFORMATIONS
name: ALL_TRANSFORMATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_TRANSFORMATIONS.html
---

# ALL_TRANSFORMATIONS

ALL_TRANSFORMATIONS displays information about all transformations accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TRANSFORMATION_ID | NUMBER | Unique identifier for the transformation |
| OWNER | VARCHAR2(128) | Owning user of the transformation |
| NAME | VARCHAR2(128) | Transformation name |
| FROM_TYPE | VARCHAR2(128) | Source type name |
| TO_TYPE | VARCHAR2(256) | Target type name |

## Usage Notes

These transformations can be specified with Advanced Queuing operations such as enqueue, dequeue, and subscribe to automatically integrate transformations in AQ messaging. Related Views DBA_TRANSFORMATIONS displays information about all transformations in the database. USER_TRANSFORMATIONS displays information about transformations owned by the current user. This view does not display the OWNER column. See Also: " DBA_TRANSFORMATIONS " " USER_TRANSFORMATIONS " See Also: " DBA_TRANSFORMATIONS " " USER_TRANSFORMATIONS "