---
id: 19c__DBMS_DATA_MINING.ALTER_REVERSE_EXPRESSION
name: DBMS_DATA_MINING.ALTER_REVERSE_EXPRESSION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.ALTER_REVERSE_EXPRESSION

This procedure replaces a reverse transformation expression with an expression that you specify. If the attribute does not have a reverse expression, the procedure creates one from the specified expression.

## Syntax

```sql
DBMS_DATA_MINING.ALTER_REVERSE_EXPRESSION (
         model_name             VARCHAR2,
         expression             CLOB,
         attribute_name         VARCHAR2 DEFAULT NULL,
         attribute_subname      VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. |
| expression | CLOB | IN | An expression to replace the reverse transformation associated with the attribute. |
| attribute_name | VARCHAR2 | IN | Name of the attribute. Specify NULL if you wish to apply expression to a cluster, feature, or One-Class SVM prediction. |
| attribute_subname | VARCHAR2 | IN | Name of the nested attribute if attribute_name is a nested column, otherwise NULL . |

## Usage Notes

You can also use this procedure to customize the output of clustering, feature extraction, and anomaly detection models. Syntax DBMS_DATA_MINING.ALTER_REVERSE_EXPRESSION ( model_name VARCHAR2, expression CLOB, attribute_name VARCHAR2 DEFAULT NULL, attribute_subname VARCHAR2 DEFAULT NULL); Parameters Table 47-39 ALTER_REVERSE_EXPRESSION Procedure Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. expression An expression to replace the reverse transformation associated with the attribute. attribute_name Name of the attribute. Specify NULL if you wish to apply expression to a cluster, feature, or One-Class SVM prediction. attribute_subname Name of the nested attribute if attribute_name is a nested column, otherwise NULL . Usage Notes For purposes of model transparency, Oracle Data Mining provides reverse transformations for transformations that are embedded in a model. Reverse transformations are applied to the attributes returned in model details ( GET_MODEL_DETAILS_ * functions) and to the scored target of predictive models. See Also: “About Transformation Lists” under DBMS_DATA_MINING_TRANSFORM Operational Notes If you alter the reverse transformation for the target of a model that has a cost matrix, you must specify a transformation expression that has the same type as the actual and predicted values in the cost matrix. Also, the reverse transformation that you specify must result in values that are present in the cost matrix. See Also: " ADD_COST_MATRIX Procedure " and Oracle Data Mining Concepts for information about cost matrixes. To prevent reverse transformation of an attribute, you can specify NULL for expression . The reverse transformation expression can contain a reference to a PL/SQL function that returns a valid Oracle datatype. For example, you could define a function like the following for a categorical attribute named blood_pressure that has values 'Low', 'Medium' and 'High'. CREATE OR REPLACE FUNCTION numx(c char) RETURN NUMBER IS BEGIN CASE c WHEN ''Low'' THEN RETURN 1; WHEN ''Medium'' THEN RETURN 2; WHEN ''High'' THEN RETURN 3; ELSE RETURN null; END CASE; END numx; Then you could invoke ALTER_REVERSE_EXPRESION for blood_pressure as follows. EXEC dbms_data_mining.alter_reverse_expression( '<model_name>', 'NUMX(blood_pressure)', 'blood_pressure'); You can use ALTER_REVERSE_EXPRESSION to label clusters produced by clustering models and features produced by feature extraction. You can use ALTER_REVERSE_EXPRESSION to replace the zeros and ones returned by anomaly-detection models. By default, anomaly-detection models label anomalous records with 0 and all other records with 1. See Also: Oracle Data Mining Concepts for information about anomaly detection See Also: “About Transformation Lists” under DBMS_DATA_MINING_TRANSFORM Operational Notes