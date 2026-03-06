---
id: 19c__ALL_SYNC_CAPTURE_PREPARED_TABS
name: ALL_SYNC_CAPTURE_PREPARED_TABS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SYNC_CAPTURE_PREPARED_TABS.html
---

# ALL_SYNC_CAPTURE_PREPARED_TABS

ALL_SYNC_CAPTURE_PREPARED_TABS displays information about the tables accessible to the current user that are prepared for synchronous capture instantiation.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the table prepared for synchronous capture instantiation |
| TABLE_NAME | VARCHAR2(128) | Name of the table prepared for synchronous capture instantiation |
| SCN | NUMBER | SCN from which changes can be captured |
| TIMESTAMP | DATE | Time at which the table was ready to be instantiated |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_SYNC_CAPTURE_PREPARED_TABS displays information about all tables in the database that are prepared for synchronous capture instantiation. See Also: " DBA_SYNC_CAPTURE_PREPARED_TABS " See Also: " DBA_SYNC_CAPTURE_PREPARED_TABS "