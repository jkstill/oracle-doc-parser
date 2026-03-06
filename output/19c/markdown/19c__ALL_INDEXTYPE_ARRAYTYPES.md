---
id: 19c__ALL_INDEXTYPE_ARRAYTYPES
name: ALL_INDEXTYPE_ARRAYTYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [all]
source_file: ALL_INDEXTYPE_ARRAYTYPES.html
---

# ALL_INDEXTYPE_ARRAYTYPES

ALL_INDEXTYPE_ARRAYTYPES displays information about the array types specified by the indextypes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the indextype |
| INDEXTYPE_NAME | VARCHAR2(128) | Name of the indextype |
| BASE_TYPE_SCHEMA | VARCHAR2(128) | Name of the base type schema |
| BASE_TYPE_NAME | VARCHAR2(128) | Name of the base type name |
| BASE_TYPE | VARCHAR2(30) | Datatype of the base type |
| ARRAY_TYPE_SCHEMA | VARCHAR2(128) | Name of the array type schema |
| ARRAY_TYPE_NAME | VARCHAR2(128) | Name of the array type name |

## Usage Notes

Related Views DBA_INDEXTYPE_ARRAYTYPES displays information about the array types specified by all indextypes in the database. USER_INDEXTYPE_ARRAYTYPES displays information about the array types specified by the indextypes owned by the current user. See Also: " DBA_INDEXTYPE_ARRAYTYPES " " USER_INDEXTYPE_ARRAYTYPES " See Also: " DBA_INDEXTYPE_ARRAYTYPES " " USER_INDEXTYPE_ARRAYTYPES "