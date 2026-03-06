---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_GLOBAL
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_GLOBAL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_GLOBAL

The GET_MODEL_DETAILS_GLOBAL function returns statistics about the model as a whole. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_global(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_model_global_details PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `DM_model_global_details`

## Usage Notes

Global details are available for Generalized Linear Models, Association Rules, Singular Value Decomposition, and Expectation Maximization. There are new Global model views which show global information for all algorithms. Oracle recommends that users leverage the views instead. Refer to Model Details View Global . Syntax DBMS_DATA_MINING.get_model_details_global( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_model_global_details PIPELINED; Parameters Table 47-87 GET_MODEL_DETAILS_GLOBAL Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model. Return Values Table 47-88 GET_MODEL_DETAILS_GLOBAL Function Return Values Return Value Description DM_MODEL_GLOBAL_DETAILS A collection of rows of type DM_MODEL_GLOBAL_DETAIL . The rows have the following columns: (global_detail_name VARCHAR2(30), global_detail_value NUMBER) Examples The following example returns the global model details for the GLM Regression model GLMR_SH_Regr_sample , which was created by the sample program dmglrdem.sql . For information about the sample programs, see Oracle Data Mining User's Guide . SELECT * FROM TABLE(dbms_data_mining.get_model_details_global( 'GLMR_SH_Regr_sample')) ORDER BY global_detail_name; GLOBAL_DETAIL_NAME GLOBAL_DETAIL_VALUE ------------------------------ ------------------- ADJUSTED_R_SQUARE .731412557 AIC 5931.814 COEFF_VAR 18.1711243 CORRECTED_TOTAL_DF 1499 CORRECTED_TOT_SS 278740.504 DEPENDENT_MEAN 38.892 ERROR_DF 1433 ERROR_MEAN_SQUARE 49.9440956 ERROR_SUM_SQUARES 71569.8891 F_VALUE 62.8492452 GMSEP 52.280819 HOCKING_SP .034877162 J_P 52.1749319 MODEL_CONVERGED 1 MODEL_DF 66 MODEL_F_P_VALUE 0 MODEL_MEAN_SQUARE 3138.94871 MODEL_SUM_SQUARES 207170.615 NUM_PARAMS 67 NUM_ROWS 1500 ROOT_MEAN_SQ 7.06711367 R_SQ .743238288 SBIC 6287.79977 VALID_COVARIANCE_MATRIX 1