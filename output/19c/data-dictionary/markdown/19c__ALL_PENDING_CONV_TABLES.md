---
id: 19c__ALL_PENDING_CONV_TABLES
name: ALL_PENDING_CONV_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_PENDING_CONV_TABLES.html
---

# ALL_PENDING_CONV_TABLES

ALL_PENDING_CONV_TABLES describes the pending conversion tables (tables which are not upgraded to the latest type version) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_PENDING_CONV_TABLES describes all pending conversion tables in the database. USER_PENDING_CONV_TABLES describes the pending conversion tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_PENDING_CONV_TABLES " " USER_PENDING_CONV_TABLES " See Also: " DBA_PENDING_CONV_TABLES " " USER_PENDING_CONV_TABLES "