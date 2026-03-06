---
id: 19c__DBMS_DATA_MINING.GET_ASSOCIATION_RULES
name: DBMS_DATA_MINING.GET_ASSOCIATION_RULES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_ASSOCIATION_RULES

The GET_ASSOCIATION_RULES function returns the rules produced by an Association model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide

## Syntax

```sql
DBMS_DATA_MINING.get_association_rules(
      model_name       IN VARCHAR2,
      topn             IN NUMBER DEFAULT NULL,
      rule_id          IN INTEGER DEFAULT NULL,
      min_confidence   IN NUMBER DEFAULT NULL,
      min_support      IN NUMBER DEFAULT NULL,
      max_rule_length  IN INTEGER DEFAULT NULL,
      min_rule_length  IN INTEGER DEFAULT NULL,
      sort_order       IN ORA_MINING_VARCHAR2_NT DEFAULT NULL,
      antecedent_items IN DM_ITEMS DEFAULT NULL,
      consequent_items IN DM_ITEMS DEFAULT NULL,
      min_lift         IN NUMBER DEFAULT NULL,
      partition_name   IN VARCHAR2 DEFAULT NULL)
  RETURN DM_Rules PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. This is the only required parameter of GET_ASSOCIATION_RULES . All other parameters specify optional filters on the rules to return. |
| topn | NUMBER | IN | Returns the n top rules ordered by confidence and then support, both descending. If you specify a sort order, then the top n rules are derived after the sort is performed. If topn is specified and no maximum or minimum rule length is specified, then the only columns allowed in the sort order are RULE_CONFIDENCE and RULE_SUPPORT . If topn is specified and a maximum or minimum rule length is specified, then RULE_CONFIDENCE , RULE_SUPPORT , and NUMBER_OF_ITEMS are allowed in the sort order. |
| rule_id | INTEGER | IN | Identifier of the rule to return. If you specify a value for rule_id , do not specify values for the other filtering parameters. |
| min_confidence | NUMBER | IN | Returns the rules with confidence greater than or equal to this number. |
| min_support | NUMBER | IN | Returns the rules with support greater than or equal to this number. |
| max_rule_length | INTEGER | IN | Returns the rules with a length less than or equal to this number. Rule length refers to the number of items in the rule (See NUMBER_OF_ITEMS in Table 47-72 ). For example, in the rule A=>B (if A, then B), the number of items is 2. If max_rule_length is specified, then the NUMBER_OF_ITEMS column is permitted in the sort order. |
| min_rule_length | INTEGER | IN | Returns the rules with a length greater than or equal to this number. See max_rule_length for a description of rule length. If min_rule_length is specified, then the NUMBER_OF_ITEMS column is permitted in the sort order. |
| sort_order | ORA_MINING_VARCHAR2_NT | IN | Sorts the rules by the values in one or more of the returned columns. Specify one or more column names, each followed by ASC for ascending order or DESC for descending order. (See Table 47-72 for the column names.) For example, to sort the result set in descending order first by the NUMBER_OF_ITEMS column, then by the RULE_CONFIDENCE column, you must specify: ORA_MINING_VARCHAR2_NT('NUMBER_OF_ITEMS DESC', 'RULE_CONFIDENCE DESC') If you specify topn , the results will vary depending on the sort order. By default, the results are sorted by Confidence in descending order, then by Support in descending order. |
| antecedent_items | DM_ITEMS | IN | Returns the rules with these items in the antecedent. |
| consequent_items | DM_ITEMS | IN | Returns the rules with this item in the consequent. |
| min_lift | NUMBER | IN | Returns the rules with lift greater than or equal to this number. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `DM_Rules`

## Usage Notes

You can specify filtering criteria to GET_ASSOCIATION_RULES to return a subset of the rules. Filtering criteria can improve the performance of the table function. If the number of rules is large, then the greatest performance improvement will result from specifying the topn parameter. Syntax DBMS_DATA_MINING.get_association_rules( model_name IN VARCHAR2, topn IN NUMBER DEFAULT NULL, rule_id IN INTEGER DEFAULT NULL, min_confidence IN NUMBER DEFAULT NULL, min_support IN NUMBER DEFAULT NULL, max_rule_length IN INTEGER DEFAULT NULL, min_rule_length IN INTEGER DEFAULT NULL, sort_order IN ORA_MINING_VARCHAR2_NT DEFAULT NULL, antecedent_items IN DM_ITEMS DEFAULT NULL, consequent_items IN DM_ITEMS DEFAULT NULL, min_lift IN NUMBER DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_Rules PIPELINED; Parameters Table 47-71 GET_ASSOCIATION_RULES Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. This is the only required parameter of GET_ASSOCIATION_RULES . All other parameters specify optional filters on the rules to return. topn Returns the n top rules ordered by confidence and then support, both descending. If you specify a sort order, then the top n rules are derived after the sort is performed. If topn is specified and no maximum or minimum rule length is specified, then the only columns allowed in the sort order are RULE_CONFIDENCE and RULE_SUPPORT . If topn is specified and a maximum or minimum rule length is specified, then RULE_CONFIDENCE , RULE_SUPPORT , and NUMBER_OF_ITEMS are allowed in the sort order. rule_id Identifier of the rule to return. If you specify a value for rule_id , do not specify values for the other filtering parameters. min_confidence Returns the rules with confidence greater than or equal to this number. min_support Returns the rules with support greater than or equal to this number. max_rule_length Returns the rules with a length less than or equal to this number. Rule length refers to the number of items in the rule (See NUMBER_OF_ITEMS in Table 47-72 ). For example, in the rule A=>B (if A, then B), the number of items is 2. If max_rule_length is specified, then the NUMBER_OF_ITEMS column is permitted in the sort order. min_rule_length Returns the rules with a length greater than or equal to this number. See max_rule_length for a description of rule length. If min_rule_length is specified, then the NUMBER_OF_ITEMS column is permitted in the sort order. sort_order Sorts the rules by the values in one or more of the returned columns. Specify one or more column names, each followed by ASC for ascending order or DESC for descending order. (See Table 47-72 for the column names.) For example, to sort the result set in descending order first by the NUMBER_OF_ITEMS column, then by the RULE_CONFIDENCE column, you must specify: ORA_MINING_VARCHAR2_NT('NUMBER_OF_ITEMS DESC', 'RULE_CONFIDENCE DESC') If you specify topn , the results will vary depending on the sort order. By default, the results are sorted by Confidence in descending order, then by Support in descending order. antecedent_items Returns the rules with these items in the antecedent. consequent_items Returns the rules with this item in the consequent. min_lift Returns the rules with lift greater than or equal to this number. partition_name Specifies a partition in a partitioned model. Return Values The object type returned by GET_ASSOCIATION_RULES is described in Table 47-72 . For descriptions of each field, see the Usage Notes. Table 47-72 GET_ASSOCIATION RULES Function Return Values Return Value Description DM_RULES A set of rows of type DM_RULE . The rows have the following columns: (rule_id INTEGER, antecedent DM_PREDICATES, consequent DM_PREDICATES, rule_support NUMBER, rule_confidence NUMBER, rule_lift NUMBER, antecedent_support NUMBER, consequent_support NUMBER, number_of_items INTEGER ) DM_PREDICATES The antecedent and consequent columns each return nested tables of type DM_PREDICATES . The rows, of type DM_PREDICATE , have the following columns: (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), conditional_operator CHAR(2)/*=,<>,<,>,<=,>=*/, attribute_num_value NUMBER, attribute_str_value VARCHAR2(4000), attribute_support NUMBER, attribute_confidence NUMBER) Usage Notes This table function pipes out rows of type DM_RULES . For information on Data Mining data types and piped output from table functions, see " Datatypes " . The columns returned by GET_ASSOCIATION_RULES are described as follows: Column in DM_RULES Description rule_id Unique identifier of the rule antecedent The independent condition in the rule. When this condition exists, the dependent condition in the consequent also exists. The condition is a combination of attribute values called a predicate ( DM_PREDICATE ). The predicate specifies a condition for each attribute. The condition may specify equality (=), inequality (<>), greater than (>), less than (<), greater than or equal to (>=), or less than or equal to (<=) a given value. Support and Confidence for each attribute condition in the antecedent is returned in the predicate. Support is the number of transactions that satisfy the antecedent. Confidence is the likelihood that a transaction will satisfy the antecedent. Note: The occurence of the attribute as a DM_PREDICATE indicates the presence of the item in the transaction. The actual value for attribute_num_value or attribute_str_value is meaningless. For example, the following predicate indicates that 'Mouse Pad' is present in the transaction even though the attribute value is NULL . DM_PREDICATE('PROD_NAME', 'Mouse Pad', '= ', NULL, NULL, NULL, NULL)) consequent The dependent condition in the rule. This condition exists when the antecedent exists. The consequent, like the antecedent, is a predicate ( DM_PREDICATE ). Support and confidence for each attribute condition in the consequent is returned in the predicate. Support is the number of transactions that satisfy the consequent. Confidence is the likelihood that a transaction will satisfy the consequent. rule_support The number of transactions that satisfy the rule. rule_confidence The likelihood of a transaction satisfying the rule. rule_lift The degree of improvement in the prediction over random chance when the rule is satisfied. antecedent_support The ratio of the number of transactions that satisfy the antecedent to the total number of transactions. consequent_support The ratio of the number of transactions that satisfy the consequent to the total number of transactions. number_of_items The total number of attributes referenced in the antecedent and consequent of the rule.