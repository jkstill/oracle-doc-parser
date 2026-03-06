---
id: 19c__DBMS_DATA_MINING.DROP_MODEL
name: DBMS_DATA_MINING.DROP_MODEL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.DROP_MODEL

This procedure deletes the specified mining model.

## Syntax

```sql
DBMS_DATA_MINING.DROP_MODEL (model_name IN VARCHAR2,
                             force      IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the mining model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. |
| force | BOOLEAN | IN | Forces the mining model to be dropped even if it is invalid. A mining model may be invalid if a serious system error interrupted the model build process. |

## Usage Notes

Syntax DBMS_DATA_MINING.DROP_MODEL (model_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameters Table 47-66 DROP_MODEL Procedure Parameters Parameter Description model_name Name of the mining model in the form [ schema_name .] model_name . If you do not specify a schema, your own schema is used. force Forces the mining model to be dropped even if it is invalid. A mining model may be invalid if a serious system error interrupted the model build process. Usage Note To drop a mining model, you must be the owner or you must have the DROP ANY MINING MODEL privilege. See Oracle Data Mining User's Guide for information about privileges for data mining. Example You can use the following command to delete a valid mining model named nb_sh_clas_sample that exists in your schema. BEGIN DBMS_DATA_MINING.DROP_MODEL(model_name => 'nb_sh_clas_sample'); END; /