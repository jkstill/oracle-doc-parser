---
id: 19c__DBMS_DATA_MINING.ADD_COST_MATRIX
name: DBMS_DATA_MINING.ADD_COST_MATRIX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.ADD_COST_MATRIX

The ADD_COST_MATRIX procedure associates a cost matrix table with a Classification model. The cost matrix biases the model by assigning costs or benefits to specific model outcomes.

## Syntax

```sql
DBMS_DATA_MINING.ADD_COST_MATRIX (
       model_name                IN VARCHAR2,
       cost_matrix_table_name    IN VARCHAR2,
       cost_matrix_schema_name   IN VARCHAR2 DEFAULT NULL);
       partition_name            IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is assumed. |
| cost_matrix_table_name | VARCHAR2 | IN | Name of the cost matrix table (described in Table 47-37 ). |
| cost_matrix_schema_name | VARCHAR2 | IN | Schema of the cost matrix table. If no schema is specified, then the current schema is used. |
| partition_name | VARCHAR2 | IN | Name of the partition in a partitioned model |

## Usage Notes

The cost matrix is stored with the model and taken into account when the model is scored. You can also specify a cost matrix inline when you invoke a Data Mining SQL function for scoring. To view the scoring matrix for a model, query the DM$VC prefixed model view. Refer to Model Detail View for Classification Algorithm . To obtain the default scoring matrix for a model, query the DM$VC prefixed model view. To remove the default scoring matrix from a model, use the REMOVE_COST_MATRIX procedure. See " GET_MODEL_COST_MATRIX Function " and " REMOVE_COST_MATRIX Procedure " . See Also: "Biasing a Classification Model" in Oracle Data Mining Concepts for more information about costs Oracle Database SQL Language Reference for syntax of inline cost matrix Oracle Data Mining User’s Guide See Also: "Biasing a Classification Model" in Oracle Data Mining Concepts for more information about costs Oracle Database SQL Language Reference for syntax of inline cost matrix Oracle Data Mining User’s Guide Syntax DBMS_DATA_MINING.ADD_COST_MATRIX ( model_name IN VARCHAR2, cost_matrix_table_name IN VARCHAR2, cost_matrix_schema_name IN VARCHAR2 DEFAULT NULL); partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 47-36 ADD_COST_MATRIX Procedure Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is assumed. cost_matrix_table_name Name of the cost matrix table (described in Table 47-37 ). cost_matrix_schema_name Schema of the cost matrix table. If no schema is specified, then the current schema is used. partition_name Name of the partition in a partitioned model Usage Notes If the model is not in your schema, then ADD_COST_MATRIX requires the ALTER ANY MINING MODEL system privilege or the ALTER object privilege for the mining model. The cost matrix table must have the columns shown in Table 47-37 . Table 47-37 Required Columns in a Cost Matrix Table Column Name Datatype ACTUAL_TARGET_VALUE Valid target data type PREDICTED_TARGET_VALUE Valid target data type COST NUMBER, FLOAT , BINARY_DOUBLE , or BINARY_FLOAT See Also: Oracle Data Mining User's Guide for valid target datatypes The types of the actual and predicted target values must be the same as the type of the model target. For example, if the target of the model is BINARY_DOUBLE , then the actual and predicted values must be BINARY_DOUBLE . If the actual and predicted values are CHAR or VARCHAR , then ADD_COST_MATRIX treats them as VARCHAR2 internally. If the types do not match, or if the actual or predicted value is not a valid target value, then the ADD_COST_MATRIX procedure raises an error. Note: If a reverse transformation is associated with the target, then the actual and predicted values must be consistent with the target after the reverse transformation has been applied. See “Reverse Transformations and Model Transparency” under the “About Transformation Lists” section in DBMS_DATA_MINING_TRANSFORM Operational Notes for more information. Since a benefit can be viewed as a negative cost, you can specify a benefit for a given outcome by providing a negative number in the costs column of the cost matrix table. All Classification algorithms can use a cost matrix for scoring. The Decision Tree algorithm can also use a cost matrix at build time. If you want to build a Decision Tree model with a cost matrix, specify the cost matrix table name in the CLAS_COST_TABLE_NAME setting in the settings table for the model. See Table 47-7 . The cost matrix used to create a Decision Tree model becomes the default scoring matrix for the model. If you want to specify different costs for scoring, use the REMOVE_COST_MATRIX procedure to remove the cost matrix and the ADD_COST_MATRIX procedure to add a new one. Scoring on a partitioned model is partition-specific. Scoring cost matrices can be added to or removed from an individual partition in a partitioned model. If PARTITION_NAME is NOT NULL, then the model must be a partitioned model. The COST_MATRIX is added to that partition of the partitioned model. If the PARTITION_NAME is NULL, but the model is a partitioned model, then the COST_MATRIX table is added to every partition in the model.