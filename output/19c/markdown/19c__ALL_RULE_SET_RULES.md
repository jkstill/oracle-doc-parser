---
id: 19c__ALL_RULE_SET_RULES
name: ALL_RULE_SET_RULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_RULE_SET_RULES.html
---

# ALL_RULE_SET_RULES

ALL_RULE_SET_RULES describes the rules in the rule sets accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the rule set |
| RULE_SET_NAME | VARCHAR2(128) | Name of the rule set |
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| RULE_SET_RULE_ENABLED | VARCHAR2(8) | Indicates whether the rule is enabled in the rule set ( ENABLED ) or not ( DISABLED ) |
| RULE_SET_RULE_EVAL_CTX_OWNER | VARCHAR2(128) | Owner of the evaluation context specified when the rule was added to the rule set, if any |
| RULE_SET_RULE_EVAL_CTX_NAME | VARCHAR2(128) | Name of the evaluation context specified when the rule was added to the rule set, if any |
| RULE_SET_RULE_COMMENT | VARCHAR2(4000) | Comment specified when the rule was added to the rule set, if any |

## Usage Notes

Related Views DBA_RULE_SET_RULES describes the rules in all rule sets in the database. USER_RULE_SET_RULES describes the rules in the rule sets owned by the current user. This view does not display the RULE_SET_OWNER column. See Also: " DBA_RULE_SET_RULES " " USER_RULE_SET_RULES " See Also: " DBA_RULE_SET_RULES " " USER_RULE_SET_RULES "