---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_SVM
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_SVM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_SVM

The GET_MODEL_DETAILS_SVM function returns a set of rows that provide the details of a linear Support Vector Machine (SVM) model. If invoked for nonlinear SVM, it returns ORA-40215 . Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_svm(
      model_name   VARCHAR2,
      reverse_coef NUMBER DEFAULT 0,
      partition_name VARCHAR2 DEFAULT NULL)
  RETURN DM_SVM_Linear_Coeff_Set PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| reverse_coef | NUMBER | IN | Whether or not GET_MODEL_DETAILS_SVM should transform the attribute coefficients using the original attribute transformations. When reverse_coef is set to 0 (default), GET_MODEL_DETAILS_SVM returns the coefficients directly from the model without applying transformations. When reverse_coef is set to 1, GET_MODEL_DETAILS_SVM transforms the coefficients and bias by applying the normalization shifts and scales that were generated using automatic data preparation. See Usage Note 4 . |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model. |

**Returns:** `DM_SVM_Linear_Coeff_Set`

## Usage Notes

In linear SVM models, only nonzero coefficients are stored. This reduces storage and speeds up model loading. As a result, if an attribute is missing in the coefficient list returned by GET_MODEL_DETAILS_SVM , then the coefficient of this attribute should be interpreted as zero. Syntax DBMS_DATA_MINING.get_model_details_svm( model_name VARCHAR2, reverse_coef NUMBER DEFAULT 0, partition_name VARCHAR2 DEFAULT NULL) RETURN DM_SVM_Linear_Coeff_Set PIPELINED; Parameters Table 47-101 GET_MODEL_DETAILS_SVM Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. reverse_coef Whether or not GET_MODEL_DETAILS_SVM should transform the attribute coefficients using the original attribute transformations. When reverse_coef is set to 0 (default), GET_MODEL_DETAILS_SVM returns the coefficients directly from the model without applying transformations. When reverse_coef is set to 1, GET_MODEL_DETAILS_SVM transforms the coefficients and bias by applying the normalization shifts and scales that were generated using automatic data preparation. See Usage Note 4 . partition_name Specifies a partition in a partitioned model. Return Values Table 47-102 GET_MODEL_DETAILS_SVM Function Return Values Return Value Description DM_SVM_LINEAR_COEFF_SET A set of rows of type DM_SVM_LINEAR_COEFF . The rows have the following columns: (class VARCHAR2(4000), attribute_set DM_SVM_ATTRIBUTE_SET) The attribute_set column returns a nested table of type DM_SVM_ATTRIBUTE_SET . The rows, of type DM_SVM_ATTRIBUTE , have the following columns: (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), coefficient NUMBER) See Usage Notes. Usage Notes This table function pipes out rows of type DM_SVM_LINEAR_COEFF . For information on Data Mining datatypes and piped output from table functions, see " Datatypes " . The class column of DM_SVM_LINEAR_COEFF contains Classification target values. For SVM Regression models, class is null. For each Classification target value, a set of coefficients is returned. For Binary Classification, one-class Classification, and Regression models, only a single set of coefficients is returned. The attribute_value column in DM_SVM_ATTRIBUTE_SET is used for categorical attributes. GET_MODEL_DETAILS functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model. The coefficients are related to the transformed, not the original, attributes. When returned directly with the model details, the coefficients may not provide meaningful information. If you want GET_MODEL_DETAILS_SVM to transform the coefficients such that they relate to the original attributes, set the reverse_coef parameter to 1. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.