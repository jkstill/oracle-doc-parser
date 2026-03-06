---
id: 19c__ALL_OPERATOR_COMMENTS
name: ALL_OPERATOR_COMMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_OPERATOR_COMMENTS.html
---

# ALL_OPERATOR_COMMENTS

ALL_OPERATOR_COMMENTS displays comments for the user-defined operators accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the user-defined operator |
| OPERATOR_NAME | VARCHAR2(128) | Name of the user-defined operator |
| COMMENTS | VARCHAR2(4000) | Comment for the user-defined operator |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_OPERATOR_COMMENTS displays comments for all user-defined operators in the database. USER_OPERATOR_COMMENTS displays comments for the user-defined operators owned by the current user. See Also: " DBA_OPERATOR_COMMENTS " " USER_OPERATOR_COMMENTS " See Also: " DBA_OPERATOR_COMMENTS " " USER_OPERATOR_COMMENTS "