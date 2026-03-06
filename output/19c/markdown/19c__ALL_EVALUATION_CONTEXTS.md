---
id: 19c__ALL_EVALUATION_CONTEXTS
name: ALL_EVALUATION_CONTEXTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_EVALUATION_CONTEXTS.html
---

# ALL_EVALUATION_CONTEXTS

ALL_EVALUATION_CONTEXTS describes the rule evaluation contexts accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVALUATION_CONTEXT_OWNER | VARCHAR2(128) | Owner of the evaluation context |
| EVALUATION_CONTEXT_NAME | VARCHAR2(128) | Name of the evaluation context |
| EVALUATION_FUNCTION | VARCHAR2(4000) | Evaluation function associated with the evaluation context, if any |
| EVALUATION_CONTEXT_COMMENT | VARCHAR2(4000) | Comment specified with the evaluation context, if any |

## Usage Notes

Related Views DBA_EVALUATION_CONTEXTS describes all rule evaluation contexts in the database. USER_EVALUATION_CONTEXTS describes the rule evaluation contexts owned by the current user. This view does not display the EVALUATION_CONTEXT_OWNER column. See Also: " DBA_EVALUATION_CONTEXTS " " USER_EVALUATION_CONTEXTS " See Also: " DBA_EVALUATION_CONTEXTS " " USER_EVALUATION_CONTEXTS "