---
id: 19c__ALL_CONS_OBJ_COLUMNS
name: ALL_CONS_OBJ_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_CONS_OBJ_COLUMNS.html
---

# ALL_CONS_OBJ_COLUMNS

ALL_CONS_OBJ_COLUMNS displays information about the types that object columns (or attributes) or collection elements have been constrained to, in the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table containing the object column or attribute |
| COLUMN_NAME | VARCHAR2(4000) | Fully qualified name of the object column or attribute |
| CONS_TYPE_OWNER | VARCHAR2(128) | Owner of the type that the column (or element) is constrained to |
| CONS_TYPE_NAME | VARCHAR2(128) | Name of the type that the column (or element) is constrained to |
| CONS_TYPE_ONLY | VARCHAR2(15) | Indicates whether the column (or element) is constrained to ONLY type ( Y ) or not ( N ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CONS_OBJ_COLUMNS displays information about the types that object columns (or attributes) or collection elements have been constrained to, in all tables in the database. USER_CONS_OBJ_COLUMNS displays information about the types that object columns (or attributes) or collection elements have been constrained to, in the tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_CONS_OBJ_COLUMNS " " USER_CONS_OBJ_COLUMNS " See Also: " DBA_CONS_OBJ_COLUMNS " " USER_CONS_OBJ_COLUMNS "