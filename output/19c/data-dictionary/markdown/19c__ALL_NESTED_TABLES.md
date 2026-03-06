---
id: 19c__ALL_NESTED_TABLES
name: ALL_NESTED_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_NESTED_TABLES.html
---

# ALL_NESTED_TABLES

ALL_NESTED_TABLES describes the nested tables in tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the nested table |
| TABLE_NAME | VARCHAR2(128) | Name of the nested table |
| TABLE_TYPE_OWNER | VARCHAR2(128) | Owner of the type of which the nested table was created |
| TABLE_TYPE_NAME | VARCHAR2(128) | Name of the type of the nested table |
| PARENT_TABLE_NAME | VARCHAR2(128) | Name of the parent table containing the nested table |
| PARENT_TABLE_COLUMN | VARCHAR2(4000) | Column name of the parent table that corresponds to the nested table |
| STORAGE_SPEC | VARCHAR2(30) | Indicates whether storage for the nested table is USER_SPECIFIED or DEFAULT |
| RETURN_TYPE | VARCHAR2(20) | Return type of the varray column ( LOCATOR ) or ( VALUE ) |
| ELEMENT_SUBSTITUTABLE | VARCHAR2(25) | Indicates whether the nested table element is substitutable ( Y ) or not ( N ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_NESTED_TABLES describes all nested tables in the database. USER_NESTED_TABLES describes nested tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_NESTED_TABLES " " USER_NESTED_TABLES " See Also: " DBA_NESTED_TABLES " " USER_NESTED_TABLES "