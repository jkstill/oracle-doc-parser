---
id: 19c__ALL_APPLY_TABLE_COLUMNS
name: ALL_APPLY_TABLE_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_APPLY_TABLE_COLUMNS.html
---

# ALL_APPLY_TABLE_COLUMNS

ALL_APPLY_TABLE_COLUMNS displays, for the tables accessible to the current user, information about the nonkey table columns for which apply process conflict detection has been stopped for update and delete operations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the table |
| OBJECT_NAME | VARCHAR2(128) | Name of the table |
| COLUMN_NAME | VARCHAR2(4000) | Name of the column |
| COMPARE_OLD_ON_DELETE | VARCHAR2(3) | Indicates whether to Compare the old value of the column on deletes ( YES ) or not ( NO ) |
| COMPARE_OLD_ON_UPDATE | VARCHAR2(3) | Indicates whether to Compare the old value of the column on updates ( YES ) or not ( NO ) |
| APPLY_DATABASE_LINK | VARCHAR2(128) | For remote tables, name of the database link pointing to the remote database |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Conflict detection for nonkey columns can be stopped using the DBMS_APPLY_ADM.COMPARE_OLD_VALUES procedure. Related View DBA_APPLY_TABLE_COLUMNS displays, for all tables in the database, information about the nonkey table columns for which apply process conflict detection has been stopped for update and delete operations. See Also: " DBA_APPLY_TABLE_COLUMNS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLY_ADM.COMPARE_OLD_VALUES procedure