---
id: 19c__ALL_PARTIAL_DROP_TABS
name: ALL_PARTIAL_DROP_TABS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_PARTIAL_DROP_TABS.html
---

# ALL_PARTIAL_DROP_TABS

DBA_PARTIAL_DROP_TABS describes all tables in the database that have partially completed DROP COLUMN operations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the table |

## Usage Notes

Related Views DBA_PARTIAL_DROP_TABS describes all tables in the database that have partially completed DROP COLUMN operations. USER_PARTIAL_DROP_TABS describes tables in the schema of the current user that have partially completed DROP COLUMN operations. This view does not display the OWNER column. See Also: " DBA_PARTIAL_DROP_TABS " " USER_PARTIAL_DROP_TABS " See Also: " DBA_PARTIAL_DROP_TABS " " USER_PARTIAL_DROP_TABS "