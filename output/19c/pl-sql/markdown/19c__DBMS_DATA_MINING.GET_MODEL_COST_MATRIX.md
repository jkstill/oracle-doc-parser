---
id: 19c__DBMS_DATA_MINING.GET_MODEL_COST_MATRIX
name: DBMS_DATA_MINING.GET_MODEL_COST_MATRIX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_COST_MATRIX

The GET_* interfaces are replaced by model views, and Oracle recommends that users leverage the views instead. The GET_MODEL_COST_MATRIX function is replaced by the DM$VC prefixed view, Scoring Cost Matrix. The cost matrix used when building a Decision Tree is made available by the DM$VM prefixed view, Decision Tree Build Cost Matrix.

## Syntax

```sql
DBMS_DATA_MINING.GET_MODEL_COST_MATRIX (
      model_name                IN VARCHAR2,
      matrix_type               IN VARCHAR2 DEFAULT cost_matrix_type_score)
      partition_name            IN VARCHAR2 DEFAULT NULL);
RETURN DM_COST_MATRIX PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| matrix_type | VARCHAR2 | IN | The type of cost matrix. COST_MATRIX_TYPE_SCORE — cost matrix used for scoring. (Default.) COST_MATRIX_TYPE_CREATE — cost matrix used to create the model (Decision Tree only). |
| partition_name | VARCHAR2 | IN | Name of the partition in a partitioned model |

**Returns:** `DM_COST_MATRIX`

## Usage Notes

Refer to Model Detail View for Classification Algorithm . The GET_MODEL_COST_MATRIX function returns the rows of a cost matrix associated with the specified model. By default, this function returns the scoring cost matrix that was added to the model with the ADD_COST_MATRIX procedure. If you wish to obtain the cost matrix used to create a model, specify cost_matrix_type_create as the matrix_type . See Table 47-75 . See also ADD_COST_MATRIX Procedure . Syntax DBMS_DATA_MINING.GET_MODEL_COST_MATRIX ( model_name IN VARCHAR2, matrix_type IN VARCHAR2 DEFAULT cost_matrix_type_score) partition_name IN VARCHAR2 DEFAULT NULL); RETURN DM_COST_MATRIX PIPELINED; Parameters Table 47-75 GET_MODEL_COST_MATRIX Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. matrix_type The type of cost matrix. COST_MATRIX_TYPE_SCORE — cost matrix used for scoring. (Default.) COST_MATRIX_TYPE_CREATE — cost matrix used to create the model (Decision Tree only). partition_name Name of the partition in a partitioned model Return Values Table 47-76 GET_MODEL_COST_MATRIX Function Return Values Return Value Description DM_COST_MATRIX A set of rows of type DM_COST_ELEMENT . The rows have the following columns: actual VARCHAR2(4000), NUMBER, predicted VARCHAR2(4000), cost NUMBER) Usage Notes Only Decision Tree models can be built with a cost matrix. If you want to build a Decision Tree model with a cost matrix, specify the cost matrix table name in the CLAS_COST_TABLE_NAME setting in the settings table for the model. See Table 47-7 . The cost matrix used to create a Decision Tree model becomes the default scoring matrix for the model. If you want to specify different costs for scoring, you can use the REMOVE_COST_MATRIX procedure to remove the cost matrix and the ADD_COST_MATRIX procedure to add a new one. The GET_MODEL_COST_MATRIX may return either the build or scoring cost matrix defined for a model or model partition. If you do not specify a partitioned model name, then an error is displayed.