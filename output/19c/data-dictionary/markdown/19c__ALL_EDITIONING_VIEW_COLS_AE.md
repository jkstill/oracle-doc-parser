---
id: 19c__ALL_EDITIONING_VIEW_COLS_AE
name: ALL_EDITIONING_VIEW_COLS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_EDITIONING_VIEW_COLS_AE.html
---

# ALL_EDITIONING_VIEW_COLS_AE

ALL_EDITIONING_VIEW_COLS_AE describes the relationship between the columns of the editioning views (across all editions) accessible to the current user and the table columns to which they map.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of an editioning view |
| VIEW_NAME | VARCHAR2(128) | Name of an editioning view |
| VIEW_COLUMN_ID | NUMBER | Column number within the editioning view |
| VIEW_COLUMN_NAME | VARCHAR2(128) | Name of the column in the editioning view |
| TABLE_COLUMN_ID | NUMBER | Column number of a table column to which this editioning view column maps |
| TABLE_COLUMN_NAME | VARCHAR2(128) | Name of a table column to which this editioning view column maps |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the editioning view is defined |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_EDITIONING_VIEW_COLS_AE describes the relationship between the columns of all editioning views (across all editions) in the database and the table columns to which they map. USER_EDITIONING_VIEW_COLS_AE describes the relationship between the columns of the editioning views (across all editions) owned by the current user and the table columns to which they map. This view does not display the OWNER column. See Also: " DBA_EDITIONING_VIEW_COLS_AE " " USER_EDITIONING_VIEW_COLS_AE " See Also: " DBA_EDITIONING_VIEW_COLS_AE " " USER_EDITIONING_VIEW_COLS_AE "