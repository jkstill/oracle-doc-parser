---
id: 19c__ALL_APPLY_CHANGE_HANDLERS
name: ALL_APPLY_CHANGE_HANDLERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_CHANGE_HANDLERS.html
---

# ALL_APPLY_CHANGE_HANDLERS

ALL_APPLY_CHANGE_HANDLERS displays information about the change handlers on the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CHANGE_TABLE_OWNER | VARCHAR2(128) | Owner of the change table |
| CHANGE_TABLE_NAME | VARCHAR2(128) | Name of the change table |
| SOURCE_TABLE_OWNER | VARCHAR2(128) | Owner of the source table |
| SOURCE_TABLE_NAME | VARCHAR2(128) | Name of the source table |
| HANDLER_NAME | VARCHAR2(128) | Name of the statement-based change handler |
| CAPTURE_VALUES | VARCHAR2(3) | Indicates whether to capture the old ( OLD ), new ( NEW ), or both ( * ) values |
| APPLY_NAME | VARCHAR2(128) | Name of the apply process |
| OPERATION_NAME | VARCHAR2(10) | Name of the DML operation to which the DML handler is set: DEFAULT INSERT UPDATE DELETE LOB_UPDATE |
| CREATION_TIME | TIMESTAMP(6) | Change handler creation time |
| MODIFICATION_TIME | TIMESTAMP(6) | Change handler modification time |

## Usage Notes

Related View DBA_APPLY_CHANGE_HANDLERS displays information about the change handlers on all tables in the database. See Also: " DBA_APPLY_CHANGE_HANDLERS " See Also: " DBA_APPLY_CHANGE_HANDLERS "