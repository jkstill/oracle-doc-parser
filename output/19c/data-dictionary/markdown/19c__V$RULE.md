---
id: 19c__V$RULE
name: V$RULE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RULE.html
---

# V$RULE

V$RULE displays rule statistics. This view has a row for every rule loaded into shared memory.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RULE_SET_OBJECT_ID | NUMBER |  |
| EVALUATION_CONTEXT_OBJECT_ID | NUMBER |  |
| RULE_OWNER | VARCHAR2(128) |  |
| RULE_NAME | VARCHAR2(128) |  |
| RULE_CONDITION | VARCHAR2(200) |  |
| TRUE_HITS | NUMBER |  |
| MAYBE_HITS | NUMBER |  |
| SQL_EVALUATIONS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content