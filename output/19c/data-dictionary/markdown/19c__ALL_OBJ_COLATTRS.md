---
id: 19c__ALL_OBJ_COLATTRS
name: ALL_OBJ_COLATTRS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_OBJ_COLATTRS.html
---

# ALL_OBJ_COLATTRS

ALL_OBJ_COLATTRS describes object columns and attributes contained in the tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table containing the object column or attribute |
| COLUMN_NAME | VARCHAR2(4000) | Fully qualified name of the object column or attribute |
| SUBSTITUTABLE | VARCHAR2(15) | Indicates whether the column is substitutable ( Y ) or not ( N ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_OBJ_COLATTRS describes object columns and attributes contained in all tables in the database. USER_OBJ_COLATTRS describes object columns and attributes contained in the tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_OBJ_COLATTRS " " USER_OBJ_COLATTRS " See Also: " DBA_OBJ_COLATTRS " " USER_OBJ_COLATTRS "