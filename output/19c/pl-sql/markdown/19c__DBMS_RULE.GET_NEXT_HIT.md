---
id: 19c__DBMS_RULE.GET_NEXT_HIT
name: DBMS_RULE.GET_NEXT_HIT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.GET_NEXT_HIT

This function returns the next rule that evaluated to TRUE from a true rules iterator, or returns the next rule that evaluated to MAYBE from a maybe rules iterator. The function returns NULL if there are no more rules that evaluated to TRUE or MAYBE .

## Syntax

```sql
DBMS_RULE.GET_NEXT_HIT(
   iterator  IN  BINARY_INTEGER)
 RETURN SYS.RE$RULE_HIT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| iterator | BINARY_INTEGER) | IN | The iterator from which the rule that evaluated to TRUE or MAYBE is retrieved |

**Returns:** `SYS.RE$RULE_HIT`

## Usage Notes

Syntax DBMS_RULE.GET_NEXT_HIT( iterator IN BINARY_INTEGER) RETURN SYS.RE$RULE_HIT; Parameter Table 149-8 GET_NEXT_HIT Function Parameter Parameter Description iterator The iterator from which the rule that evaluated to TRUE or MAYBE is retrieved Usage Notes This procedure requires an open iterator that was returned by an earlier call to DBMS_RULE.EVALUATE in the same session. The user who runs this procedure does not require any privileges on the rule set being evaluated. When an iterator returns NULL , it is closed automatically. If an open iterator is no longer needed, then use the CLOSE_ITERATOR procedure in the DBMS_RULE package to close it. Note: This function raises an error if the rule set being evaluated was modified after the call to the DBMS_RULE.EVALUATE procedure that returned the iterator. Modifications to a rule set include added rules to the rule set, changing existing rules in the rule set, dropping rules from the rule set, and dropping the rule set. See Also: Rule TYPEs for more information about the types used with the DBMS_RULE package EVALUATE Procedure CLOSE_ITERATOR Procedure Note: This function raises an error if the rule set being evaluated was modified after the call to the DBMS_RULE.EVALUATE procedure that returned the iterator. Modifications to a rule set include added rules to the rule set, changing existing rules in the rule set, dropping rules from the rule set, and dropping the rule set. See Also: Rule TYPEs for more information about the types used with the DBMS_RULE package EVALUATE Procedure CLOSE_ITERATOR Procedure