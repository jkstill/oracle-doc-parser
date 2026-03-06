---
id: 19c__ALL_UPDATABLE_COLUMNS
name: ALL_UPDATABLE_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_UPDATABLE_COLUMNS.html
---

# ALL_UPDATABLE_COLUMNS

ALL_UPDATABLE_COLUMNS describes all columns in a join view that are updatable by the current user, subject to appropriate privileges.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| COLUMN_NAME | VARCHAR2(128) | Column name |
| UPDATABLE | VARCHAR2(3) | Indicates whether the column is updatable ( YES ) or not ( NO ) |
| INSERTABLE | VARCHAR2(3) | Indicates whether the column is insertable ( YES ) or not ( NO ) |
| DELETABLE | VARCHAR2(3) | Indicates whether the column is deletable ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_UPDATABLE_COLUMNS describes all columns in a join view that are updatable by the database administrator, subject to appropriate privileges. USER_UPDATABLE_COLUMNS describes all columns owned by the current user that are in a join view and are updatable by the current user, subject to appropriate privileges. See Also: " DBA_UPDATABLE_COLUMNS " " USER_UPDATABLE_COLUMNS " Oracle Database Concepts for information on updatable join views See Also: " DBA_UPDATABLE_COLUMNS " " USER_UPDATABLE_COLUMNS " Oracle Database Concepts for information on updatable join views