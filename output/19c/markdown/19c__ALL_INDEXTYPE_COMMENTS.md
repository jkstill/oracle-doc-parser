---
id: 19c__ALL_INDEXTYPE_COMMENTS
name: ALL_INDEXTYPE_COMMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [all]
source_file: ALL_INDEXTYPE_COMMENTS.html
---

# ALL_INDEXTYPE_COMMENTS

ALL_INDEXTYPE_COMMENTS displays comments for the user-defined indextypes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the user-defined indextype |
| INDEXTYPE_NAME | VARCHAR2(128) | Name of the user-defined indextype |
| COMMENTS | VARCHAR2(4000) | Comment for the user-defined indextype |

## Usage Notes

Related Views DBA_INDEXTYPE_COMMENTS displays comments for all user-defined indextypes in the database. USER_INDEXTYPE_COMMENTS displays comments for the user-defined indextypes owned by the current user. See Also: " DBA_INDEXTYPE_COMMENTS " " USER_INDEXTYPE_COMMENTS " See Also: " DBA_INDEXTYPE_COMMENTS " " USER_INDEXTYPE_COMMENTS "