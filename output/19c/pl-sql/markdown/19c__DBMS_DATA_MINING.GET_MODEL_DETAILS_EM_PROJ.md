---
id: 19c__DBMS_DATA_MINING.GET_MODEL_DETAILS_EM_PROJ
name: DBMS_DATA_MINING.GET_MODEL_DETAILS_EM_PROJ
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_DETAILS_EM_PROJ

The GET_MODEL_DETAILS_EM_PROJ function returns a set of rows that provide statistics about the projections produced by an Expectation Maximization model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Model Detail Views" in Oracle Data Mining User’s Guide .

## Syntax

```sql
DBMS_DATA_MINING.get_model_details_em_proj(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_EM_PROJECTION_SET PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model |

**Returns:** `DM_EM_PROJECTION_SET`

## Usage Notes

Syntax DBMS_DATA_MINING.get_model_details_em_proj( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_EM_PROJECTION_SET PIPELINED; Parameters Table 47-82 GET_MODEL_DETAILS_EM_PROJ Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model Return Values Table 47-83 GET_MODEL_DETAILS_EM_PROJ Function Return Values Return Value Description DM_EM_PROJECTION_SET A set of rows of type DM_EM_PROJECTION . The rows have the following columns: (feature_name VARCHAR2(4000), attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), coefficient NUMBER ) See Usage Notes for details. Usage Notes This table function pipes out rows of type DM_EM_PROJECTION . For information on Data Mining datatypes and piped output from table functions, see " Datatypes " . The columns in each row returned by GET_MODEL_DETAILS_EM_PROJ are described as follows: Column in DM_EM_PROJECTION Description feature_name Name of a derived feature. The feature maps to the attribute_name returned by the GET_MODEL_DETAILS_EM Function . attribute_name Name of a column in the build data attribute_subname Subname in a nested column attribute_value Categorical value coefficient Projection coefficient. The representation is sparse; only the non-zero coefficients are returned. GET_MODEL_DETAILS functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model. The coefficients are related to the transformed, not the original, attributes. When returned directly with the model details, the coefficients may not provide meaningful information. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.