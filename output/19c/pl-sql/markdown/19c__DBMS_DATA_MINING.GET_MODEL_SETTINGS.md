---
id: 19c__DBMS_DATA_MINING.GET_MODEL_SETTINGS
name: DBMS_DATA_MINING.GET_MODEL_SETTINGS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.GET_MODEL_SETTINGS

The GET_MODEL_SETTINGS function returns the settings used to build the given model. Starting from Oracle Database 12 c Release 2, this function is deprecated. See "Static Data Dictionary Views: ALL_ALL_TABLES to ALL_OUTLINES " in Oracle Database Reference .

## Syntax

```sql
FUNCTION get_model_settings(model_name IN VARCHAR2)
  RETURN DM_Model_Settings PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2) | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |

**Returns:** `DM_Model_Settings`

## Usage Notes

Syntax FUNCTION get_model_settings(model_name IN VARCHAR2) RETURN DM_Model_Settings PIPELINED; Parameters Table 47-95 GET_MODEL_SETTINGS Function Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. Return Values Table 47-96 GET_MODEL_SETTINGS Function Return Values Return Value Description DM_MODEL_SETTINGS A set of rows of type DM_MODEL_SETTINGS . The rows have the following columns: DM_MODEL_SETTINGS TABLE OF SYS.DM_MODEL_SETTING Name Type ---------------------- -------------------- SETTING_NAME VARCHAR2(30) SETTING_VALUE VARCHAR2(4000) Usage Notes This table function pipes out rows of type DM_MODEL_SETTINGS . For information on Data Mining datatypes and piped output from table functions, see " DBMS_DATA_MINING Datatypes " . The setting names/values include both those specified by the user and any defaults assigned by the build process. Examples The following example returns model model settings for an example Naive Bayes model. SETTING_NAME SETTING_VALUE ------------------------------ ------------------------------ ALGO_NAME ALGO_NAIVE_BAYES PREP_AUTO ON ODMS_MAX_PARTITIONS 1000 NABS_SINGLETON_THRESHOLD 0 CLAS_WEIGHTS_BALANCED OFF NABS_PAIRWISE_THRESHOLD 0 ODMS_PARTITION_COLUMNS GENDER,Y_BOX_GAMES ODMS_MISSING_VALUE_TREATMENT ODMS_MISSING_VALUE_AUTO ODMS_SAMPLING ODMS_SAMPLING_DISABLE 9 rows selected.