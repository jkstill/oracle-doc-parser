---
id: 19c__DBMS_RULE.GET_NEXT_RESULT
name: DBMS_RULE.GET_NEXT_RESULT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.GET_NEXT_RESULT

This function iterates over result from the expression given in RESULT_VAL_ITERATOR . It returns the expression at iterator evaluated to TRUE or FALSE .

## Syntax

```sql
DBMS_RULE.GET_NEXT_RESULT (
 result_val_iterator_id    IN   BINARY_INTEGER)
 RETURN  BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| result_val_iterator_id | BINARY_INTEGER) | IN | Iterator returned from EVALUATE_EXPRESSION_ITERATOR |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_RULE.GET_NEXT_RESULT ( result_val_iterator_id IN BINARY_INTEGER) RETURN BOOLEAN; Parameter Table 149-9 GET_NEXT_RESULT Function Parameter Parameter Description result_val_iterator_id Iterator returned from EVALUATE_EXPRESSION_ITERATOR