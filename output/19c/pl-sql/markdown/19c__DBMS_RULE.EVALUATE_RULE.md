---
id: 19c__DBMS_RULE.EVALUATE_RULE
name: DBMS_RULE.EVALUATE_RULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.EVALUATE_RULE

The Rule Evaluation API expects that CREATE_RULE procedure has been called with an legitimate EVALUATION_CONTEXT prior. This API will evaluate the condition defined in the Rule.

## Syntax

```sql
DBMS_RULE.EVALUATE_RULE( 
  rule_name            IN   VARCHAR2,
  event_context        IN   SYS.RE$NV_LIST               DEFAULT NULL,
  table_values         IN   SYS.RE$TABLE_VALUE_LIST      DEFAULT NULL,
  column_values        IN   SYS.RE$COLUMN_VALUE_LIST     DEFAULT NULL,
  variable_values      IN   SYS.RE$VARIABLE_VALUE_LIST   DEFAULT NULL,
  attribute_values     IN   SYS.RE$ATTRIBUTE_VALUE_LIST  DEFAULT NULL,
  cache                IN   BOOLEAN DEFAULT FALSE,
  result_val           OUT  BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_name | VARCHAR2 | IN | Name of the rule previously create using CREATE_RULE procedure. |
| event_context | SYS.RE$NV_LIST | IN | A list of name-value pairs that identify events that cause evaluation. |
| table_values | SYS.RE$TABLE_VALUE_LIST | IN | ROWID of table row for expression evaluation. |
| column_values | SYS.RE$COLUMN_VALUE_LIST | IN | Values of columns referred in the expression |
| variable_values | SYS.RE$VARIABLE_VALUE_LIST | IN | Values of variables referred in expression |
| attribute_values | SYS.RE$ATTRIBUTE_VALUE_LIST | IN | Values of attributes referred in expression |
| cache | BOOLEAN | IN | If TRUE , Result Cache will be created. |
| result_val | BOOLEAN) | OUT | Result of the evaluation |

## Usage Notes

Syntax DBMS_RULE.EVALUATE_RULE( rule_name IN VARCHAR2, event_context IN SYS.RE$NV_LIST DEFAULT NULL, table_values IN SYS.RE$TABLE_VALUE_LIST DEFAULT NULL, column_values IN SYS.RE$COLUMN_VALUE_LIST DEFAULT NULL, variable_values IN SYS.RE$VARIABLE_VALUE_LIST DEFAULT NULL, attribute_values IN SYS.RE$ATTRIBUTE_VALUE_LIST DEFAULT NULL, cache IN BOOLEAN DEFAULT FALSE, result_val OUT BOOLEAN); Parameters Table 149-6 EVALUATE_RULE Procedure Parameter Parameter Description rule_name Name of the rule previously create using CREATE_RULE procedure. event_context A list of name-value pairs that identify events that cause evaluation. table_values ROWID of table row for expression evaluation. column_values Values of columns referred in the expression variable_values Values of variables referred in expression attribute_values Values of attributes referred in expression cache If TRUE , Result Cache will be created. result_val Result of the evaluation