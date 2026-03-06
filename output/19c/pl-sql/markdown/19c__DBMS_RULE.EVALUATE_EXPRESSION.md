---
id: 19c__DBMS_RULE.EVALUATE_EXPRESSION
name: DBMS_RULE.EVALUATE_EXPRESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.EVALUATE_EXPRESSION

This procedure allows user to evaluate an expression under the logged in user in a session.

## Syntax

```sql
DBMS_RULE.EVALUATE_EXPRESSION(
   rule_expression         IN         VARCHAR2,
   table_aliases           IN         SYS.RE$TABLE_ALIAS_LIST:= NULL,
   variable_types          IN         SYS.RE$VARIABLE_TYPE_LIST:= NULL,
   table_values            IN         SYS.RE$TABLE_VALUE_LIST:= NULL,
   column_values           IN         SYS.RE$COLUMN_VALUE_LIST:=NULL,
   variable_values         IN         SYS.RE$VARIABLE_VALUE_LIST:=NULL,
   attribute_values        IN         SYS.RE$ATTRIBUTE_VALUE_LIST:=NULL,
   cache                   IN         BOOLEAN DEFAULT FALSE,
   result_val              OUT        BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_expression | VARCHAR2 | IN | Contains an expression string. |
| table_alias |  |  | Contains alias of tables referred in the expression string. |
| variable_types | SYS.RE$VARIABLE_TYPE_LIST | IN | Contains type definitions of variables used in expression. |
| table_values | SYS.RE$TABLE_VALUE_LIST | IN | Contains ROWID of table row for expression evaluation. |
| column_values | SYS.RE$COLUMN_VALUE_LIST | IN | Contains values of columns referred in the expression. |
| variable_values | SYS.RE$VARIABLE_VALUE_LIST | IN | Contains values of variables referred in the expression. |
| attribute_values | SYS.RE$ATTRIBUTE_VALUE_LIST | IN | Contains values of attributes referred in the expression. |
| cache | BOOLEAN | IN | If TRUE , Result Cache will be created. |
| result_val | BOOLEAN) | OUT | Result of the evaluation. |

## Usage Notes

Any re-execute of the same expression with same table alias and variable type will result in reusing the same compiled context. With fixed compile cache size, its possible of aging.... Syntax DBMS_RULE.EVALUATE_EXPRESSION( rule_expression IN VARCHAR2, table_aliases IN SYS.RE$TABLE_ALIAS_LIST:= NULL, variable_types IN SYS.RE$VARIABLE_TYPE_LIST:= NULL, table_values IN SYS.RE$TABLE_VALUE_LIST:= NULL, column_values IN SYS.RE$COLUMN_VALUE_LIST:=NULL, variable_values IN SYS.RE$VARIABLE_VALUE_LIST:=NULL, attribute_values IN SYS.RE$ATTRIBUTE_VALUE_LIST:=NULL, cache IN BOOLEAN DEFAULT FALSE, result_val OUT BOOLEAN); Parameters Table 149-4 EVALUATE_EXPRESSION Procedure Parameters Parameter Description rule_expression Contains an expression string. table_alias Contains alias of tables referred in the expression string. variable_types Contains type definitions of variables used in expression. table_values Contains ROWID of table row for expression evaluation. column_values Contains values of columns referred in the expression. variable_values Contains values of variables referred in the expression. attribute_values Contains values of attributes referred in the expression. cache If TRUE , Result Cache will be created. result_val Result of the evaluation.