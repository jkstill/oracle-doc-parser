---
id: 19c__ALL_IND_EXPRESSIONS
name: ALL_IND_EXPRESSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_IND_EXPRESSIONS.html
---

# ALL_IND_EXPRESSIONS

ALL_IND_EXPRESSIONS describes the expressions of function-based indexes on tables accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_OWNER | VARCHAR2(128) | Owner of the index |
| INDEX_NAME | VARCHAR2(128) | Name of the index |
| TABLE_OWNER | VARCHAR2(128) | Owner of the table or cluster |
| TABLE_NAME | VARCHAR2(128) | Name of the table or cluster |
| COLUMN_EXPRESSION | LONG | Function-based index expression defining the column |
| COLUMN_POSITION | NUMBER | Position of the column or attribute within the index |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_IND_EXPRESSIONS describes the expressions of all function-based indexes in the database. USER_IND_EXPRESSIONS describes the expressions of function-based indexes on tables owned by the current user. This view does not display the INDEX_OWNER or TABLE_OWNER columns. See Also: " DBA_IND_EXPRESSIONS " " USER_IND_EXPRESSIONS " See Also: " DBA_IND_EXPRESSIONS " " USER_IND_EXPRESSIONS "