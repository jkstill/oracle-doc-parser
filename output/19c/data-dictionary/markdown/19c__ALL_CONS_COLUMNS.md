---
id: 19c__ALL_CONS_COLUMNS
name: ALL_CONS_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_CONS_COLUMNS.html
---

# ALL_CONS_COLUMNS

ALL_CONS_COLUMNS describes columns that are accessible to the current user and that are specified in constraints.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the constraint definition |
| CONSTRAINT_NAME | VARCHAR2(128) | Name of the constraint definition |
| TABLE_NAME | VARCHAR2(128) | Name of the table with the constraint definition |
| COLUMN_NAME | VARCHAR2(4000) | Name of the column or attribute of the object type column specified in the constraint definition Note: If you create a constraint on a user-defined REF column, the system creates the constraint on the attributes that make up the REF column. Therefore, the column names displayed in this view are the attribute names, with the REF column name as a prefix, in the following form: "REF_name"."attribute" |
| POSITION | NUMBER | Original position of the column or attribute in the definition of the object |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CONS_COLUMNS describes all columns in the database that are specified in constraints. USER_CONS_COLUMNS describes columns that are owned by the current user and that are specified in constraints. See Also: " DBA_CONS_COLUMNS " " USER_CONS_COLUMNS " See Also: " DBA_CONS_COLUMNS " " USER_CONS_COLUMNS "