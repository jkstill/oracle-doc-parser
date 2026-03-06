---
id: 19c__DBMS_RULE.EVALUATE_EXPRESSION_ITERATOR
name: DBMS_RULE.EVALUATE_EXPRESSION_ITERATOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RULE
tags: [dbms_rule]
source_file: DBMS_RULE.html
---

# DBMS_RULE.EVALUATE_EXPRESSION_ITERATOR

This is an user visible interface. Because PL/SQL based callbacks can be expensive, we provide an array based approach. The client program is assumed to find the relevant datapoints and pass re$value_list into evaluation interface. The expression evaluation engine is expected to walk through this list and evaluate expression for each datapoint ( re$value_list ) element.

## Syntax

```sql
DBMS_RULE.EVALUATE_EXPRESSION_ITERATOR(
       rule_expression        IN              varchar2,
       table_aliases          IN              sys.re$table_alias_list:= NULL,
       variable_types         IN              sys.re$variable_type_list:= NULL,
       values                 IN              sys.re$value_list,
       cache                  IN              boolean DEFAULT FALSE,
       result_val_iter_id     OUT             BINARY_INTEGER)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rule_expression | varchar2 | IN | Contains an expression string. |
| table_alias |  |  | Alias of tables referred in the above expression string. |
| variable_types | sys.re$variable_type_list | IN | Type definitions of variables used in expression. |
| values | sys.re$value_list | IN | List of datapoint values for evaluation. |
| cache | boolean | IN | If TRUE , Result Cache will be created. |
| result_val_iter_id | BINARY_INTEGER) | OUT | Contains iterator for result of array of values sent using value . |

## Usage Notes

Syntax DBMS_RULE.EVALUATE_EXPRESSION_ITERATOR( rule_expression IN varchar2, table_aliases IN sys.re$table_alias_list:= NULL, variable_types IN sys.re$variable_type_list:= NULL, values IN sys.re$value_list, cache IN boolean DEFAULT FALSE, result_val_iter_id OUT BINARY_INTEGER) Parameters Table 149-5 EVALUATE_EXPRESSION_ITERATOR Procedure Parameter Parameter Description rule_expression Contains an expression string. table_alias Alias of tables referred in the above expression string. variable_types Type definitions of variables used in expression. values List of datapoint values for evaluation. cache If TRUE , Result Cache will be created. result_val_iter_id Contains iterator for result of array of values sent using value .