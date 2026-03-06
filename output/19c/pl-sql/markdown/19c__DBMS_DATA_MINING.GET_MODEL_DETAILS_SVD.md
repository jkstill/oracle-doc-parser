---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_SVD
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_SVD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_SVD

The GET_MODEL_DETAILS_SVD function returns a set of rows that provide the details of a Singular Value Decomposition model. Oracle recommends to use model details view settings. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_svd(
      model_name IN VARCHAR2,
      matrix_type IN VARCHAR2 DEFAULT NULL,
      partition_name VARCHAR2 DEFAULT NULL)
   RETURN DM_SVD_MATRIX_Set PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| matrix_type | VARCHAR2 | IN | Specifies which of the three SVD matrix types to return. Values are: U , S , V , and NULL . When matrix_type is null (default), all matrices are returned. The U matrix is only computed when the SVDS_U_MATRIX_OUTPUT setting is enabled. It is not computed by default. If the model does not contain U matrices and you set matrix_type to U , an empty set of rows is returned. See Table 47-26 . |
| partition_name | VARCHAR2 | IN | A partition in a partitioned model. |

**Returns:** `DM_SVD_MATRIX_Set`

## Usage Notes

Refer to Model Details View for Singular Value Decomposition . Syntax DBMS_DATA_MINING.get_model_details_svd( model_name IN VARCHAR2, matrix_type IN VARCHAR2 DEFAULT NULL, partition_name VARCHAR2 DEFAULT NULL) RETURN DM_SVD_MATRIX_Set PIPELINED; Parameters Table 47-99 GET_MODEL_DETAILS_SVD Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. matrix_type Specifies which of the three SVD matrix types to return. Values are: U , S , V , and NULL . When matrix_type is null (default), all matrices are returned. The U matrix is only computed when the SVDS_U_MATRIX_OUTPUT setting is enabled. It is not computed by default. If the model does not contain U matrices and you set matrix_type to U , an empty set of rows is returned. See Table 47-26 . partition_name A partition in a partitioned model. Return Values Table 47-100 GET_MODEL_DETAILS_SVD Function Return Values Return Value Description DM_SVD_MATRIX_SET A set of rows of type DM_SVD_MATRIX . The rows have the following columns: (matrix_type CHAR(1), feature_id NUMBER, mapped_feature_id VARCHAR2(4000), attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), case_id VARCHAR2(4000), value NUMBER, variance NUMBER, pct_cum_variance NUMBER) See Usage Notes for details. Usage Notes This table function pipes out rows of type DM_SVD_MATRIX . For information on Data Mining datatypes and piped output from table functions, see " Datatypes " . The columns in each row returned by GET_MODEL_DETAILS_SVD are described as follows: Column in DM_SVD_MATRIX_SET Description matrix_type The type of matrix. Possible values are S , V , and U . This field is never null. feature_id The feature that the matrix entry refers to. mapped_feature_id A descriptive name for the feature. attribute_name Column name in the V matrix component bases. This field is null for the S and U matrices. attribute_subname Subname in the V matrix component bases. This is relevant only in the case of a nested column. This field is null for the S and U matrices. case_id Unique identifier of the row in the build data described by the U matrix projection. This field is null for the S and V matrices. value The matrix entry value. variance The variance explained by a component. It is non-null only for S matrix entries. This column is non-null only for S matrix entries and for SVD models with setting dbms_data_mining.svds_scoring_mode set to dbms_data_mining.svds_scoring_pca and the build data is centered, either manually or because the setting dbms_data_mining.prep_auto is set to dbms_data_mining.prep_auto_on . pct_cum_variance The percent cumulative variance explained by the components thus far. The components are ranked by the explained variance in descending order. This column is non-null only for S matrix entries and for SVD models with setting dbms_data_mining.svds_scoring_mode set to dbms_data_mining.svds_scoring_pca and the build data is centered, either manually or because the setting dbms_data_mining.prep_auto is set to dbms_data_mining.prep_auto_on . The output of GET_MODEL_DETAILS is in sparse format. Zero values are not returned. Only the diagonal elements of the S matrix, the non-zero coefficients in the V matrix bases, and the non-zero U matrix projections are returned. There is one exception: If the data row does not produce non-zero U Matrix projections, the case ID for that row is returned with NULL for the feature_id and value . This is done to avoid losing any records from the original data. GET_MODEL_DETAILS functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the preferred partition name.