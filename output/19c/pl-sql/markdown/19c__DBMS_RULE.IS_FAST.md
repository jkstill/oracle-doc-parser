---
id: 19c__DBMS_RULE.IS_FAST
name: DBMS_RULE.IS_FAST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.IS_FAST

Given an expression, of either rule or Independent Expression, this procedure will return TRUE if the expression can be evaluated as fast. An expression can be evaluated as fast if the engine does not need to run any internal SQL and does not need to go to PL/SQL layer in case there are any PL/SQL functions referred.

## Syntax

```sql
DBMS_RULE.IS_FAST(
   expression            IN       VARCHAR2,
   table_aliases         IN       SYS.RE$TABLE_ALIAS_LIST:= NULL,
   variable_types        IN       SYS.RE$VARIABLE_TYPE_LIST:= NULL,
   result_val            OUT      BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| expression | VARCHAR2 | IN | Expression to check |
| table_aliases | SYS.RE$TABLE_ALIAS_LIST | IN | Alias of tables referred in the above expression string |
| variable_types | SYS.RE$VARIABLE_TYPE_LIST | IN | Type definitions of variables used in expression |
| result_val | BOOLEAN) | OUT | If the expression can be evaluated as fast |

## Usage Notes

Syntax DBMS_RULE.IS_FAST( expression IN VARCHAR2, table_aliases IN SYS.RE$TABLE_ALIAS_LIST:= NULL, variable_types IN SYS.RE$VARIABLE_TYPE_LIST:= NULL, result_val OUT BOOLEAN); Parameter Table 149-10 IS_FAST Procedure Parameter Parameter Description expression Expression to check table_aliases Alias of tables referred in the above expression string variable_types Type definitions of variables used in expression result_val If the expression can be evaluated as fast