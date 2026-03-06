---
id: 19c__ALL_EVALUATION_CONTEXT_TABLES
name: ALL_EVALUATION_CONTEXT_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_EVALUATION_CONTEXT_TABLES.html
---

# ALL_EVALUATION_CONTEXT_TABLES

ALL_EVALUATION_CONTEXT_TABLES describes the tables in the rule evaluation contexts accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVALUATION_CONTEXT_OWNER | VARCHAR2(128) | Owner of the evaluation context |
| EVALUATION_CONTEXT_NAME | VARCHAR2(128) | Name of the evaluation context |
| TABLE_ALIAS | VARCHAR2(128) | Alias for a table in the evaluation context |
| TABLE_NAME | VARCHAR2(4000) | Name of the table referred to by the table alias |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_EVALUATION_CONTEXT_TABLES describes the tables in all rule evaluation contexts in the database. USER_EVALUATION_CONTEXT_TABLES describes the tables in the rule evaluation contexts owned by the current user. This view does not display the EVALUATION_CONTEXT_OWNER column. See Also: " DBA_EVALUATION_CONTEXT_TABLES " " USER_EVALUATION_CONTEXT_TABLES " See Also: " DBA_EVALUATION_CONTEXT_TABLES " " USER_EVALUATION_CONTEXT_TABLES "