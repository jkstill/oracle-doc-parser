---
id: 19c__ALL_APPLY_CONFLICT_COLUMNS
name: ALL_APPLY_CONFLICT_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_APPLY_CONFLICT_COLUMNS.html
---

# ALL_APPLY_CONFLICT_COLUMNS

ALL_APPLY_CONFLICT_COLUMNS displays information about the conflict handlers on the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object on which the update conflict handler is defined |
| OBJECT_NAME | VARCHAR2(128) | Name of the object on which the update conflict handler is defined |
| METHOD_NAME | VARCHAR2(92) | Name of the update conflict handler used to resolve conflicts |
| RESOLUTION_COLUMN | VARCHAR2(4000) | Name of the column used to resolve conflicts |
| COLUMN_NAME | VARCHAR2(128) | Name of a column in the column list for the update conflict handler |
| APPLY_DATABASE_LINK | VARCHAR2(128) | Database link to which changes are applied. If null, then changes are applied to the local database. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_APPLY_CONFLICT_COLUMNS displays information about the conflict handlers on all tables in the database. See Also: " DBA_APPLY_CONFLICT_COLUMNS " See Also: " DBA_APPLY_CONFLICT_COLUMNS "