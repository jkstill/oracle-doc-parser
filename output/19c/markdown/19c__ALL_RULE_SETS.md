---
id: 19c__ALL_RULE_SETS
name: ALL_RULE_SETS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_RULE_SETS.html
---

# ALL_RULE_SETS

ALL_RULE_SETS describes the rule sets accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_SET_OWNER | VARCHAR2(128) | Owner of the rule set |
| RULE_SET_NAME | VARCHAR2(128) | Name of the rule set |
| RULE_SET_EVAL_CONTEXT_OWNER | VARCHAR2(128) | Owner of the evaluation context associated with the rule set, if any |
| RULE_SET_EVAL_CONTEXT_NAME | VARCHAR2(128) | Name of the evaluation context associated with the rule set, if any |
| RULE_SET_COMMENT | VARCHAR2(4000) | Comment specified with the rule set, if any |

## Usage Notes

Related Views DBA_RULE_SETS describes all rule sets in the database. USER_RULE_SETS describes the rule sets owned by the current user. This view does not display the RULE_SET_OWNER column. See Also: " DBA_RULE_SETS " " USER_RULE_SETS " See Also: " DBA_RULE_SETS " " USER_RULE_SETS "