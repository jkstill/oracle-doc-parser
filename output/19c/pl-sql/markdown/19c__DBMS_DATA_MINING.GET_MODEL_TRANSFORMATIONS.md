---
id: 19c__DBMS_DATA_MINING.GET_MODEL_TRANSFORMATIONS
name: DBMS_DATA_MINING.GET_MODEL_TRANSFORMATIONS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_TRANSFORMATIONS

This function returns the transformation expressions embedded in the specified model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Static Data Dictionary Views: ALL_ALL_TABLES to ALL_OUTLINES " in Oracle Database Reference .

## Syntax

```sql
DBMS_DATA_MINING.get_model_transformations(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_Transforms PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Indicates the name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| partition_name | VARCHAR2 | IN | Specifies a partition in a partitioned model |

**Returns:** `DM_Transforms`

## Usage Notes

All GET_* interfaces are replaced by model views, and Oracle recommends that users reference the model views to retrieve the relevant information. The GET_MODEL_TRANSFORMATIONS function is replaced by the following: USER(/DBA/ALL)_MINING_MODEL_XFORMS: provides the user-embedded transformations DM$VX prefixed model view: provides text feature extraction information D$VN prefixed mode view: provides normalization and missing value information DM$VB: provides binning information See Also: “About Transformation Lists” in DBMS_DATA_MINING_TRANSFORM Operational Notes " GET_TRANSFORM_LIST Procedure " " CREATE_MODEL Procedure " " ALL_MINING_MODEL_XFORMS " in Oracle Database Reference " DBA_MINING_MODEL_XFORMS " in Oracle Database Reference " USER_MINING_MODEL_XFORMS " in Oracle Database Reference Model Details View for Binning Normalization and Missing Value Handling Data Preparation for Text Features See Also: “About Transformation Lists” in DBMS_DATA_MINING_TRANSFORM Operational Notes " GET_TRANSFORM_LIST Procedure " " CREATE_MODEL Procedure " " ALL_MINING_MODEL_XFORMS " in Oracle Database Reference " DBA_MINING_MODEL_XFORMS " in Oracle Database Reference " USER_MINING_MODEL_XFORMS " in Oracle Database Reference Model Details View for Binning Normalization and Missing Value Handling Data Preparation for Text Features Syntax DBMS_DATA_MINING.get_model_transformations( model_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL) RETURN DM_Transforms PIPELINED; Parameters Table 47-105 GET_MODEL_TRANSFORMATIONS Function Parameters Parameter Description model_name Indicates the name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. partition_name Specifies a partition in a partitioned model Return Values Table 47-106 GET_MODEL_TRANSFORMATIONS Function Return Value Return Value Description DM_TRANSFORMS The transformation expressions embedded in model_name . The DM_TRANSFORMS type is a table of DM_TRANSFORM objects. Each DM_TRANSFORM has these fields: attribute_name VARCHAR2(4000) attribute_subname VARCHAR2(4000) expression CLOB reverse_expression CLOB