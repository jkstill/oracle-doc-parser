---
id: 19c__ALL_INDEXTYPE_OPERATORS
name: ALL_INDEXTYPE_OPERATORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [all]
source_file: ALL_INDEXTYPE_OPERATORS.html
---

# ALL_INDEXTYPE_OPERATORS

ALL_INDEXTYPE_OPERATORS lists all operators supported by indextypes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the indextype |
| INDEXTYPE_NAME | VARCHAR2(128) | Name of the indextype |
| OPERATOR_SCHEMA | VARCHAR2(128) | Name of the operator schema |
| OPERATOR_NAME | VARCHAR2(128) | Name of the operator for which the indextype is defined |
| BINDING# | NUMBER | Binding number associated with the operator |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_INDEXTYPE_OPERATORS lists all operators supported by indextypes in the database. USER_INDEXTYPE_OPERATORS lists all operators supported by indextypes owned by the current user. See Also: " DBA_INDEXTYPE_OPERATORS " " USER_INDEXTYPE_OPERATORS " See Also: " DBA_INDEXTYPE_OPERATORS " " USER_INDEXTYPE_OPERATORS "