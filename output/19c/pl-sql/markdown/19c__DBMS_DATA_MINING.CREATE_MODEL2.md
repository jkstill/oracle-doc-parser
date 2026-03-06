---
id: 19c__DBMS_DATA_MINING.CREATE_MODEL2
name: DBMS_DATA_MINING.CREATE_MODEL2
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.CREATE_MODEL2

The CREATE_MODEL2 procedure is an alternate procedure to the CREATE_MODEL procedure, which enables creating a model without extra persistence stages. In the CREATE_MODEL procedure, the input is a table or a view and if such an object is not already present, the user must create it. By using the CREATE_MODEL2 procedure, the user does not need to create such transient database objects.

## Syntax

```sql
DBMS_DATA_MINING.CREATE_MODEL2 (
     model_name            IN VARCHAR2,
     mining_function       IN VARCHAR2,
     data_query            IN CLOB,
     set_list              IN SETTING_LIST,
     case_id_column_name   IN VARCHAR2 DEFAULT NULL,
     target_column_name    IN VARCHAR2 DEFAULT NULL,
     xform_list            IN TRANSFORM_LIST DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then the current schema is used. See the Usage Notes, CREATE_MODEL Procedure for model naming restrictions. |
| mining_function | VARCHAR2 | IN | The mining function. Values are listed in DBMS_DATA_MINING — Mining Function Settings . |
| data_query | CLOB | IN | A query which provides training data for building the model. |
| set_list | SETTING_LIST | IN | Specifies the SETTING_LIST SETTING_LIST is a table of CLOB index by VARCHAR2(30) ; Where the index is the setting name and the CLOB is the setting value for that name. |
| case_id_column_name | VARCHAR2 | IN | Case identifier column in the build data. |
| target_column_name | VARCHAR2 | IN | For supervised models, the target column in the build data. NULL for unsupervised models. |
| xform_list | TRANSFORM_LIST | IN | Refer to CREATE_MODEL Procedure . |

## Usage Notes

Syntax DBMS_DATA_MINING.CREATE_MODEL2 ( model_name IN VARCHAR2, mining_function IN VARCHAR2, data_query IN CLOB, set_list IN SETTING_LIST, case_id_column_name IN VARCHAR2 DEFAULT NULL, target_column_name IN VARCHAR2 DEFAULT NULL, xform_list IN TRANSFORM_LIST DEFAULT NULL); Parameters Table 47-63 CREATE_MODEL2 Procedure Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then the current schema is used. See the Usage Notes, CREATE_MODEL Procedure for model naming restrictions. mining_function The mining function. Values are listed in DBMS_DATA_MINING — Mining Function Settings . data_query A query which provides training data for building the model. set_list Specifies the SETTING_LIST SETTING_LIST is a table of CLOB index by VARCHAR2(30) ; Where the index is the setting name and the CLOB is the setting value for that name. case_id_column_name Case identifier column in the build data. target_column_name For supervised models, the target column in the build data. NULL for unsupervised models. xform_list Refer to CREATE_MODEL Procedure . Usage Notes Refer to CREATE_MODEL Procedure for Usage Notes. Examples The following example uses the Support Vector Machine algorithm. declare v_setlst DBMS_DATA_MINING.SETTING_LIST; BEGIN v_setlst(dbms_data_mining.algo_name) := dbms_data_mining.algo_support_vector_machines; v_setlst(dbms_data_mining.prep_auto) := dbms_data_mining.prep_auto_on; DBMS_DATA_MINING.CREATE_MODEL2( model_name => 'svm_model', mining_function => dbms_data_mining.classification, data_query => 'select * from mining_data_build_v', data_table_name => 'mining_data_build_v', case_id_column_name=> 'cust_id', target_column_name => 'affinity_card', set_list => v_setlst, case_id_column_name=> 'cust_id', target_column_name => 'affinity_card'); END; /