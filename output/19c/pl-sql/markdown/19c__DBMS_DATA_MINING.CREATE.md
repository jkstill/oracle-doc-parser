---
id: 19c__DBMS_DATA_MINING.CREATE
name: DBMS_DATA_MINING.CREATE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.CREATE

Create model function fetches the setting information from JSON object.

## Syntax

```sql
CREATE TABLE GLM_RDEMO_SETTINGS_CL (
                                                   
   setting_name  VARCHAR2(30),
   setting_value VARCHAR2(4000));
   BEGIN
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
         ('ALGO_EXTENSIBLE_LANG', 'R');
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
         (dbms_data_mining.ralg_registration_algo_name, 't1');
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
        (dbms_data_mining.odms_formula,   
        'AGE + EDUCATION + HOUSEHOLD_SIZE + OCCUPATION');
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
         ('RALG_PARAMETER_FAMILY',   'binomial(logit)' );
   END;
   /
     BEGIN
          DBMS_DATA_MINING.CREATE_MODEL(
          model_name                    =>    'GLM_RDEMO_CLASSIFICATION',
          mining_function               =>     dbms_data_mining.classification,
          data_table_name               =>    'mining_data_build_v',
          case_id_column_name           =>    'CUST_ID',
          target_column_name            =>    'AFFINITY_CARD',
          settings_table_name           =>    'GLM_RDEMO_SETTINGS_CL');
      END;
      /
```

## Usage Notes

Usage Notes If an algorithm is registered, user can create model using the registered algorithm name. Since all R scripts and default setting values are already registered, providing the value through the setting table is not necessary. This makes the use of this algorithm easier. Examples The first example builds a Classification model using the GLM algorithm. CREATE TABLE GLM_RDEMO_SETTINGS_CL ( setting_name VARCHAR2(30), setting_value VARCHAR2(4000)); BEGIN INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES ('ALGO_EXTENSIBLE_LANG', 'R'); INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES (dbms_data_mining.ralg_registration_algo_name, 't1'); INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES (dbms_data_mining.odms_formula, 'AGE + EDUCATION + HOUSEHOLD_SIZE + OCCUPATION'); INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES ('RALG_PARAMETER_FAMILY', 'binomial(logit)' ); END; / BEGIN DBMS_DATA_MINING.CREATE_MODEL( model_name => 'GLM_RDEMO_CLASSIFICATION', mining_function => dbms_data_mining.classification, data_table_name => 'mining_data_build_v', case_id_column_name => 'CUST_ID', target_column_name => 'AFFINITY_CARD', settings_table_name => 'GLM_RDEMO_SETTINGS_CL'); END; /