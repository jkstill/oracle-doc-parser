---
id: 19c__ALL_EDITIONING_VIEWS_AE
name: ALL_EDITIONING_VIEWS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_EDITIONING_VIEWS_AE.html
---

# ALL_EDITIONING_VIEWS_AE

ALL_EDITIONING_VIEWS_AE describes the editioning views (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of an editioning view |
| VIEW_NAME | VARCHAR2(128) | Name of an editioning view |
| TABLE_NAME | VARCHAR2(128) | Name of an editioning view's base table |
| EDITION_NAME | VARCHAR2(128) | Name of the application edition where the editioning view is defined |

## Usage Notes

Related Views DBA_EDITIONING_VIEWS_AE describes all editioning views (across all editions) in the database. USER_EDITIONING_VIEWS_AE describes the editioning views (across all editions) owned by the current user. This view does not display the OWNER column. See Also: " DBA_EDITIONING_VIEWS_AE " " USER_EDITIONING_VIEWS_AE " See Also: " DBA_EDITIONING_VIEWS_AE " " USER_EDITIONING_VIEWS_AE "