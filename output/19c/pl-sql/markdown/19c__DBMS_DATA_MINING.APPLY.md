---
id: 19c__DBMS_DATA_MINING.APPLY
name: DBMS_DATA_MINING.APPLY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING
tags: [dbms_data_mining]
source_file: DBMS_DATA_MINING.html
---

# DBMS_DATA_MINING.APPLY

The APPLY procedure applies a mining model to the data of interest, and generates the results in a table. The APPLY procedure is also referred to as scoring .

## Syntax

```sql
DBMS_DATA_MINING.APPLY (
      model_name           IN VARCHAR2,
      data_table_name      IN VARCHAR2,
      case_id_column_name  IN VARCHAR2,
      result_table_name    IN VARCHAR2,
      data_schema_name     IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| model_name | VARCHAR2 | IN | Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. |
| data_table_name | VARCHAR2 | IN | Name of table or view containing the data to be scored |
| case_id_column_name | VARCHAR2 | IN | Name of the case identifier column |
| result_table_name | VARCHAR2 | IN | Name of the table in which to store apply results |
| data_schema_name | VARCHAR2 | IN | Name of the schema containing the data to be scored |

## Usage Notes

For predictive mining functions, the APPLY procedure generates predictions in a target column. For descriptive mining functions such as Clustering, the APPLY process assigns each case to a cluster with a probability. In Oracle Data Mining, the APPLY procedure is not applicable to Association models and Attribute Importance models. Note: Scoring can also be performed directly in SQL using the Data Mining functions. See "Data Mining Functions" in Oracle Database SQL Language Reference "Scoring and Deployment" in Oracle Data Mining User's Guide Note: Scoring can also be performed directly in SQL using the Data Mining functions. See "Data Mining Functions" in Oracle Database SQL Language Reference "Scoring and Deployment" in Oracle Data Mining User's Guide Syntax DBMS_DATA_MINING.APPLY ( model_name IN VARCHAR2, data_table_name IN VARCHAR2, case_id_column_name IN VARCHAR2, result_table_name IN VARCHAR2, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 47-40 APPLY Procedure Parameters Parameter Description model_name Name of the model in the form [ schema_name .] model_name . If you do not specify a schema, then your own schema is used. data_table_name Name of table or view containing the data to be scored case_id_column_name Name of the case identifier column result_table_name Name of the table in which to store apply results data_schema_name Name of the schema containing the data to be scored Usage Notes The data provided for APPLY must undergo the same preprocessing as the data used to create and test the model. When you use Automatic Data Preparation, the preprocessing required by the algorithm is handled for you by the model: both at build time and apply time. (See " Automatic Data Preparation " .) APPLY creates a table in the user's schema to hold the results. The columns are algorithm-specific. The columns in the results table are listed in Table 47-41 through Table 47-45 . The case ID column name in the results table will match the case ID column name provided by you. The type of the incoming case ID column is also preserved in APPLY output. Note: Make sure that the case ID column does not have the same name as one of the columns that will be created by APPLY . For example, when applying a Classification model, the case ID in the scoring data must not be PREDICTION or PROBABILITY (See Table 47-41 ). The datatype for the PREDICTION , CLUSTER_ID , and FEATURE_ID output columns is influenced by any reverse expression that is embedded in the model by the user. If the user does not provide a reverse expression that alters the scored value type, then the types will conform to the descriptions in the following tables. See " ALTER_REVERSE_EXPRESSION Procedure " . If the model is partitioned, the result_table_name can contain results from different partitions depending on the data from the input data table. An additional column called PARTITION_NAME is added to the result table indicating the partition name that is associated with each row. For a non-partitioned model, the behavior does not change. Classification The results table for Classification has the columns described in Table 47-41 . If the target of the model is categorical, the PREDICTION column will have a VARCHAR2 datatype. If the target has a binary type, the PREDICTION column will have the binary type of the target. Table 47-41 APPLY Results Table for Classification Column Name Datatype Case ID column name Type of the case ID PREDICTION Type of the target PROBABILITY BINARY_DOUBLE Anomaly Detection The results table for Anomaly Detection has the columns described in Table 47-42 . Table 47-42 APPLY Results Table for Anomaly Detection Column Name Datatype Case ID column name Type of the case ID PREDICTION NUMBER PROBABILITY BINARY_DOUBLE Regression The results table for Regression has the columns described in APPLY Procedure . Table 47-43 APPLY Results Table for Regression Column Name Datatype Case ID column name Type of the case ID PREDICTION Type of the target Clustering Clustering is an unsupervised mining function, and hence there are no targets. The results of an APPLY procedure will contain simply the cluster identifier corresponding to a case, and the associated probability. The results table has the columns described in Table 47-44 . Table 47-44 APPLY Results Table for Clustering Column Name Datatype Case ID column name Type of the case ID CLUSTER_ID NUMBER PROBABILITY BINARY_DOUBLE Feature Extraction Feature Extraction is also an unsupervised mining function, and hence there are no targets. The results of an APPLY procedure will contain simply the feature identifier corresponding to a case, and the associated match quality. The results table has the columns described in Table 47-45 . Table 47-45 APPLY Results Table for Feature Extraction Column Name Datatype Case ID column name Type of the case ID FEATURE_ID NUMBER MATCH_QUALITY BINARY_DOUBLE