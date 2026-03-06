---
id: 19c__DBMS_DATA_MINING.RENAME_MODEL
name: DBMS_DATA_MINING.RENAME_MODEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.RENAME_MODEL

This procedure changes the name of the mining model indicated by model_name to the name that you specify as new_model_name .

## Syntax

```sql
DBMS_DATA_MINING.RENAME_MODEL (
     model_name            IN VARCHAR2,
     new_model_name        IN VARCHAR2,
     versioned_model_name  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Model to be renamed. |
| new_model_name | VARCHAR2 | IN | New name for the model model_name . |
| versioned_model_name | VARCHAR2 | IN | New name for the model new_model_name if it already exists. |

## Usage Notes

If a model with new_model_name already exists, then the procedure optionally renames new_model_name to versioned_model_name before renaming model_name to new_model_name . The model name is in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. For mining model naming restrictions, see the Usage Notes for " CREATE_MODEL Procedure " . Syntax DBMS_DATA_MINING.RENAME_MODEL ( model_name IN VARCHAR2, new_model_name IN VARCHAR2, versioned_model_name IN VARCHAR2 DEFAULT NULL); Parameters Table 47-113 RENAME_MODEL Procedure Parameters Parameter Description model_name Model to be renamed. new_model_name New name for the model model_name . versioned_model_name New name for the model new_model_name if it already exists. Usage Notes If you attempt to rename a model while it is being applied, then the model will be renamed but the apply operation will return indeterminate results. Examples This example changes the name of model census_model to census_model_2012 . BEGIN DBMS_DATA_MINING.RENAME_MODEL( model_name => 'census_model', new_model_name => 'census_model_2012'); END; / In this example, there are two classification models in the user's schema: clas_mod , the working model, and clas_mod_tst , a test model. The RENAME_MODEL procedure preserves clas_mod as clas_mod_old and makes the test model the new working model. SELECT model_name FROM user_mining_models; MODEL_NAME ------------------------------------------------------------------- CLAS_MOD CLAS_MOD_TST BEGIN DBMS_DATA_MINING.RENAME_MODEL( model_name => 'clas_mod_tst', new_model_name => 'clas_mod', versioned_model_name => 'clas_mod_old'); END; / SELECT model_name FROM user_mining_models; MODEL_NAME ------------------------------------------------------------------- CLAS_MOD CLAS_MOD_OLD