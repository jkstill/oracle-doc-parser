---
id: 19c__ALL_CAPTURE_EXTRA_ATTRIBUTES
name: ALL_CAPTURE_EXTRA_ATTRIBUTES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CAPTURE_EXTRA_ATTRIBUTES.html
---

# ALL_CAPTURE_EXTRA_ATTRIBUTES

ALL_CAPTURE_EXTRA_ATTRIBUTES displays information about the extra attributes for the capture processes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE_NAME | VARCHAR2(128) | Name of the capture process |
| ATTRIBUTE_NAME | VARCHAR2(128) | Name of the extra attribute |
| INCLUDE | VARCHAR2(3) | Indicates whether the extra attribute is included ( YES ) or not ( NO ) |
| ROW_ATTRIBUTE | VARCHAR2(3) | Indicates whether the extra attribute is a row LCR attribute ( YES ) or not ( NO ) |
| DDL_ATTRIBUTE | VARCHAR2(3) | Indicates whether the extra attribute is a DDL LCR attribute ( YES ) or not ( NO ) |

## Usage Notes

Related View DBA_CAPTURE_EXTRA_ATTRIBUTES displays information about the extra attributes for all capture processes in the database. See Also: " DBA_CAPTURE_EXTRA_ATTRIBUTES " See Also: " DBA_CAPTURE_EXTRA_ATTRIBUTES "