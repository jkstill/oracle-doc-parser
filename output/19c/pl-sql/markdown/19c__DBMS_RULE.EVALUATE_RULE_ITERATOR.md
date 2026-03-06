---
id: 19c__DBMS_RULE.EVALUATE_RULE_ITERATOR
name: DBMS_RULE.EVALUATE_RULE_ITERATOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.EVALUATE_RULE_ITERATOR

This is an iterative interface. The client program is assumed to find the relevant datapoints and pass re$value_list into evaluation interface.

## Syntax

```sql
DBMS_RULE.EVALUATE_RULE_ITERATOR)
  rule_name            IN       VARCHAR2,
  event_context        IN       SYS.RE$NV_LIST DEFAULT NULL,
  values               IN       SYS.RE$VALUE_LIST,
  cache                IN       BOOLEAN DEFAULT FALSE,
  result_val_iter_id   OUT      BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | Name of the rule previously create using CREATE_RULE procedure. |
| event_context | SYS.RE$NV_LIST | IN | A list of name-value pairs that identify events that cause evaluation |
| values | SYS.RE$VALUE_LIST | IN | List of datapoint values for evaluation. |
| cache | BOOLEAN | IN | If TRUE , Result Cache will be created. |
| result_val_iter_id | BINARY_INTEGER) | OUT | Contains iterator for result of array of values sent using values |

## Usage Notes

Evaluation engine is expected to walk through this list and evaluate expression for each datapoint ( re$value_list ) element. User can use DBMS_RULE.GET_NEXT_RESULT procedure to iterate through the result list. Syntax DBMS_RULE.EVALUATE_RULE_ITERATOR) rule_name IN VARCHAR2, event_context IN SYS.RE$NV_LIST DEFAULT NULL, values IN SYS.RE$VALUE_LIST, cache IN BOOLEAN DEFAULT FALSE, result_val_iter_id OUT BINARY_INTEGER); Parameters Table 149-7 EVALUATE_RULE_ITERATOR Procedure Parameter Parameter Description rule_name Name of the rule previously create using CREATE_RULE procedure. event_context A list of name-value pairs that identify events that cause evaluation values List of datapoint values for evaluation. cache If TRUE , Result Cache will be created. result_val_iter_id Contains iterator for result of array of values sent using values