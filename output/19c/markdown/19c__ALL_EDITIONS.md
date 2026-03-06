---
id: 19c__ALL_EDITIONS
name: ALL_EDITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_EDITIONS.html
---

# ALL_EDITIONS

ALL_EDITIONS describes the editions accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EDITION_NAME | VARCHAR2(128) | Name of the edition |
| PARENT_EDITION_NAME | VARCHAR2(128) | Name of the parent edition for this edition |
| USABLE | VARCHAR2(3) | Indicates whether the edition is usable ( YES ) or unusable ( NO ) |

## Usage Notes

Related View DBA_EDITIONS describes all editions in the database. See Also: " DBA_EDITIONS " Oracle Database Development Guide for more information about editions See Also: " DBA_EDITIONS " Oracle Database Development Guide for more information about editions