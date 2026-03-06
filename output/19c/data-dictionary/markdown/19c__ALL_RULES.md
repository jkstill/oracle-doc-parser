---
id: 19c__ALL_RULES
name: ALL_RULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_RULES.html
---

# ALL_RULES

ALL_RULES describes the rules accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| RULE_CONDITION | CLOB | Expressions and operators that constitute the rule condition |
| RULE_EVALUATION_CONTEXT_OWNER | VARCHAR2(128) | Owner of the evaluation context associated with the rule, if any |
| RULE_EVALUATION_CONTEXT_NAME | VARCHAR2(128) | Name of the evaluation context associated with the rule, if any |
| RULE_ACTION_CONTEXT | RE$NV_LIST | Action context associated with the rule, if any |
| RULE_COMMENT | VARCHAR2(4000) | Comment specified with the rule, if any |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_RULES describes all rules in the database. USER_RULES describes the rules owned by the current user. This view does not display the RULE_OWNER column. See Also: " DBA_RULES " " USER_RULES " See Also: " DBA_RULES " " USER_RULES "