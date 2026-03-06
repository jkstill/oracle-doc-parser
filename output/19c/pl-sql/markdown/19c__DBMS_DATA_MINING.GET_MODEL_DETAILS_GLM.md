---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_GLM
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_GLM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_GLM

The GET_MODEL_DETAILS_GLM function returns the coefficient statistics for a Generalized Linear Model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_glm(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_GLM_Coeff_Set PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model |

**Returns:** `DM_GLM_Coeff_Set`

## Usage Notes

The same set of statistics is returned for both linear and Logistic Regression, but statistics that do not apply to the mining function are returned as NULL . For more details, see the Usage Notes. Syntax DBMS_DATA_MINING.get_model_details_glm( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_GLM_Coeff_Set PIPELINED; Parameters Table 47-84 GET_MODEL_DETAILS_GLM Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model Return Values Table 47-85 GET_MODEL_DETAILS_GLM Return Values Return Value Description DM_GLM_COEFF_SET A set of rows of type DM_GLM_COEFF . The rows have the following columns: (class VARCHAR2(4000), attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), feature_expression VARCHAR2(4000), coefficient NUMBER, std_error NUMBER, test_statistic NUMBER, p_value NUMBER, VIF NUMBER, std_coefficient NUMBER, lower_coeff_limit NUMBER, upper_coeff_limit NUMBER, exp_coefficient BINARY_DOUBLE, exp_lower_coeff_limit BINARY_DOUBLE, exp_upper_coeff_limit BINARY_DOUBLE) GET_MODEL_DETAILS_GLM returns a row of statistics for each attribute and one extra row for the intercept, which is identified by a null value in the attribute name. Each row has the DM_GLM_COEFF datatype. The statistics are described in Table 47-86 . Table 47-86 DM_GLM_COEFF Datatype Description Column Description class The non-reference target class for Logistic Regression. The model is built to predict the probability of this class. The other class (the reference class) is specified in the model setting GLMS_REFERENCE_CLASS_NAME . See Table 47-18 . For Linear Regression, class is null. attribute_name The attribute name when there is no subname, or first part of the attribute name when there is a subname. The value of attribute_name is also the name of the column in the case table that is the source for this attribute. For the intercept, attribute_name is null. Intercepts are equivalent to the bias term in SVM models. attribute_subname The name of an attribute in a nested table. The full name of a nested attribute has the form: attribute_name.attribute_subname where attribute_name is the name of the nested column in the case table that is the source for this attribute. If the attribute is not nested, then attribute_subname is null. If the attribute is an intercept, then both the attribute_name and the attribute_subname are null. attribute_value The value of the attribute (categorical attribute only). For numeric attributes, attribute_value is null. feature_expression The feature name constructed by the algorithm when feature generation is enabled and higher-order features are found. If feature selection is not enabled, then the feature name is simply the fully-qualified attribute name ( attribute_name.attribute_subname if the attribute is in a nested column). For categorical attributes, the algorithm constructs a feature name that has the following form: fully-qualified_attribute_name.attribute_value For numeric attributes, the algorithm constructs a name for the higher-order feature by taking the product of the resulting values: ( attrib1 )*( attrib2 ))*...... where attrib1 and attrib2 are fully-qualified attribute names. coefficient The linear coefficient estimate. std_error Standard error of the coefficient estimate. test_statistic For Linear Regression, the t-value of the coefficient estimate. For Logistic Regression, the Wald chi-square value of the coefficient estimate. p-value Probability of the test_statistic . Used to analyze the significance of specific attributes in the model. VIF Variance Inflation Factor. The value is zero for the intercept. For Logistic Regression, VIF is null. VIF is not computed if the solver is Cholesky. std_coefficient Standardized estimate of the coefficient. lower_coeff_limit Lower confidence bound of the coefficient. upper_coeff_limit Upper confidence bound of the coefficient. exp_coefficient Exponentiated coefficient for Logistic Regression. For Linear Regression, exp_coefficient is null. exp_lower_coeff_limit Exponentiated coefficient for lower confidence bound of the coefficient for Logistic Regression. For Linear Regression, exp_lower_coeff_limit is null. exp_upper_coeff_limit Exponentiated coefficient for upper confidence bound of the coefficient for Logistic Regression. For Linear Regression, exp_lower_coeff_limit is null. Usage Notes Not all statistics are necessarily returned for each coefficient. Statistics will be null if: They do not apply to the mining function. For example, exp_coefficient does not apply to Linear Regression. They cannot be computed from a theoretical standpoint. For information on ridge regression, see Table 47-18 . They cannot be computed because of limitations in system resources. Their values would be infinity. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.