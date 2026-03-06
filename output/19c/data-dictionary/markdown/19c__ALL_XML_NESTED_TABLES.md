---
id: 19c__ALL_XML_NESTED_TABLES
name: ALL_XML_NESTED_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_XML_NESTED_TABLES.html
---

# ALL_XML_NESTED_TABLES

ALL_XML_NESTED_TABLES describes all the tables and their corresponding nested tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the table |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| NESTED_TABLE_NAME | VARCHAR2(128) | Name of the nested table |
| PARENT_COLUMN_NAME | VARCHAR2(4000) | Name of the parent XML column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_XML_NESTED_TABLES describes all the tables and their corresponding nested tables in the database. USER_XML_NESTED_TABLES describes all the tables and their corresponding nested tables owned by the current user. This view does not display the OWNER column. See Also: " DBA_XML_NESTED_TABLES " " USER_XML_NESTED_TABLES " See Also: " DBA_XML_NESTED_TABLES " " USER_XML_NESTED_TABLES "