---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_EM_COMP
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_EM_COMP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_EM_COMP

he GET_MODEL_DETAILS_EM_COMP table function returns a set of rows that provide details about the parameters of an Expectation Maximization model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_em_comp(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_EM_COMPONENT_SET PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model to retrieve details for. |

**Returns:** `DM_EM_COMPONENT_SET`

## Usage Notes

Syntax DBMS_DATA_MINING.get_model_details_em_comp( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_EM_COMPONENT_SET PIPELINED; Parameters Table 47-80 GET_MODEL_DETAILS_EM_COMP Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. partition_name Specifies a partition in a partitioned model to retrieve details for. Return Values Table 47-81 GET_MODEL_DETAILS_EM_COMP Function Return Values Return Value Description DM_EM_COMPONENT_SET A set of rows of type DM_EM_COMPONENT . The rows have the following columns: (info_type VARCHAR2(30), component_id NUMBER, cluster_id NUMBER, attribute_name VARCHAR2(4000), covariate_name VARCHAR2(4000), attribute_value VARCHAR2(4000), value NUMBER ) Usage Notes This table function pipes out rows of type DM_EM_COMPONENT . For information on Data Mining datatypes and piped output from table functions, see " Datatypes " . The columns in each row returned by GET_MODEL_DETAILS_EM_COMP are described as follows: Column in DM_EM_COMPONENT Description info_type The type of information in the row. The following information types are supported: cluster prior mean covariance frequency component_id Unique identifier of a component cluster_id Unique identifier of the high-level leaf cluster for each component attribute_name Name of an original attribute or a derived feature ID. The derived feature ID is used in models built on data with nested columns. The derived feature definitions can be obtained from the GET_MODEL_DETAILS_EM_PROJ Function . covariate_name Name of an original attribute or a derived feature ID used in variance/covariance definition attribute_value Categorical value or bin interval for binned numerical attributes value Encodes different information depending on the value of info_type , as follows: cluster — The value field is NULL prior — The value field returns the component prior mean — The value field returns the mean of the attribute specified in attribute_name covariance — The value field returns the covariance of the attributes specified in attribute_name and covariate_name . Using the same attribute in attribute_name and covariate_name , returns the variance. frequency — The value field returns the multivalued Bernoulli frequency parameter for the attribute/value combination specified by attribute_name and attribute_value See Usage Note 2 for details. The following table shows which fields are used for each info_type . The blank cells represent NULL s. info_type component_id cluster_id attribute_name covariate_name attribute_value value cluster X X prior X X X mean X X X X covariance X X X X X frequency X X X X X GET_MODEL_DETAILS functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.