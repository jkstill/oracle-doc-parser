---
id: 19c__ALL_SYNC_CAPTURE_TABLES
name: ALL_SYNC_CAPTURE_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_SYNC_CAPTURE_TABLES.html
---

# ALL_SYNC_CAPTURE_TABLES

ALL_SYNC_CAPTURE_TABLES displays information about the tables accessible to the current user that are captured by synchronous captures.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the synchronous capture table |
| TABLE_NAME | VARCHAR2(128) | Name of the synchronous capture table |
| ENABLED | VARCHAR2(3) | Indicates whether synchronous capture is enabled for the table ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_SYNC_CAPTURE_TABLES displays information about all tables in the database that are captured by synchronous captures. See Also: " DBA_SYNC_CAPTURE_TABLES " See Also: " DBA_SYNC_CAPTURE_TABLES "