---
id: 19c__ALL_APPLY_KEY_COLUMNS
name: ALL_APPLY_KEY_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_APPLY_KEY_COLUMNS.html
---

# ALL_APPLY_KEY_COLUMNS

Related View

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object on which substitute key columns are set |
| OBJECT_NAME | VARCHAR2(128) | Name of the object on which substitute key columns are set |
| COLUMN_NAME | VARCHAR2(128) | Column name of a column specified as a substitute key column |
| APPLY_DATABASE_LINK | VARCHAR2(128) | Database link to which changes are applied. If null, then changes are applied to the local database. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_APPLY_KEY_COLUMNS displays information about the substitute key columns for all tables in the database. See Also: " DBA_APPLY_KEY_COLUMNS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLY_ADM.SET_KEY_COLUMNS procedure See Also: " DBA_APPLY_KEY_COLUMNS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_APPLY_ADM.SET_KEY_COLUMNS procedure