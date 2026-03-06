---
id: 19c__DBMS_RULE.CLOSE_ITERATOR
name: DBMS_RULE.CLOSE_ITERATOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.CLOSE_ITERATOR

This procedure closes an open iterator.

## Syntax

```sql
DBMS_RULE.CLOSE_ITERATOR(
   iterator  IN  BINARY_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| iterator | BINARY_INTEGER) | IN | Iterator to be closed |

## Usage Notes

Syntax DBMS_RULE.CLOSE_ITERATOR( iterator IN BINARY_INTEGER); Parameter Table 149-2 CLOSE_ITERATOR Procedure Parameter Parameter Description iterator Iterator to be closed Usage Notes This procedure requires an open iterator that was returned by an earlier call to DBMS_RULE.EVALUATE in the same session. The user who runs this procedure does not require any privileges on the rule set being evaluated. Closing an iterator frees resources, such as memory, associated with the iterator. Therefore, Oracle recommends that you close an iterator when it is no longer needed. See Also: EVALUATE Procedure See Also: EVALUATE Procedure