---
id: 19c__ALL_APPLY_EXECUTE
name: ALL_APPLY_EXECUTE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_EXECUTE.html
---

# ALL_APPLY_EXECUTE

ALL_APPLY_EXECUTE displays information about the apply execute actions for the rules visible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_OWNER | VARCHAR2(128) | Owner of the rule |
| RULE_NAME | VARCHAR2(128) | Name of the rule |
| EXECUTE_EVENT | VARCHAR2(2) | Indicates whether the event satisfying the rule is executed |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_APPLY_EXECUTE displays information about the apply execute actions for all rules in the database. See Also: " DBA_APPLY_EXECUTE " See Also: " DBA_APPLY_EXECUTE "