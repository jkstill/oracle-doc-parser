---
id: 19c__ALL_OPERATORS
name: ALL_OPERATORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_OPERATORS.html
---

# ALL_OPERATORS

ALL_OPERATORS describes the operators accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the operator |
| OPERATOR_NAME | VARCHAR2(128) | Name of the operator |
| NUMBER_OF_BINDS | NUMBER | Number of bindings associated with the operator |

## Usage Notes

Related Views DBA_OPERATORS describes all operators in the database. USER_OPERATORS describes the operators owned by the current user. See Also: " DBA_OPERATORS " " USER_OPERATORS " See Also: " DBA_OPERATORS " " USER_OPERATORS "