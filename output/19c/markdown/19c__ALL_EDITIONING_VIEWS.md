---
id: 19c__ALL_EDITIONING_VIEWS
name: ALL_EDITIONING_VIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_EDITIONING_VIEWS.html
---

# ALL_EDITIONING_VIEWS

ALL_EDITIONING_VIEWS describes the editioning views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of an editioning view |
| VIEW_NAME | VARCHAR2(128) | Name of an editioning view |
| TABLE_NAME | VARCHAR2(128) | Name of an editioning view's base table |

## Usage Notes

Related Views DBA_EDITIONING_VIEWS describes all editioning views in the database. USER_EDITIONING_VIEWS describes the editioning views owned by the current user. This view does not display the OWNER column. See Also: " DBA_EDITIONING_VIEWS " " USER_EDITIONING_VIEWS " See Also: " DBA_EDITIONING_VIEWS " " USER_EDITIONING_VIEWS "