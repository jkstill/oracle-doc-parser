---
id: 19c__ALL_REFS
name: ALL_REFS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_REFS.html
---

# ALL_REFS

ALL_REFS describes the REF columns and REF attributes in object type columns accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| COLUMN_NAME | VARCHAR2(4000) | Name of the REF column or attribute. If it is not a top-level attribute, the value of COLUMN_NAME should be a path name starting with the column name. |
| WITH_ROWID | VARCHAR2(3) | Indicates whether the REF value is stored with ROWID ( YES ) or not ( NO ) |
| IS_SCOPED | VARCHAR2(3) | Indicates whether the REF column is scoped ( YES ) or not ( NO ) |
| SCOPE_TABLE_OWNER | VARCHAR2(128) | Owner of the scope table, if it exists and is accessible by the user |
| SCOPE_TABLE_NAME | VARCHAR2(128) | Name of the scope table, if it exists and is accessible by the user |
| OBJECT_ID_TYPE | VARCHAR2(33) | Indicates whether the object ID (OID) is USER-DEFINED or SYSTEM GENERATED |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_REFS describes all REF columns and REF attributes in the database. USER_REFS describes the REF columns and REF attributes in object type columns owned by the current user. This view does not display the OWNER column. See Also: " DBA_REFS " " USER_REFS " See Also: " DBA_REFS " " USER_REFS "