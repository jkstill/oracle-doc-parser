---
id: 19c__DBMS_PREDICTIVE_ANALYTICS.PREDICT
name: DBMS_PREDICTIVE_ANALYTICS.PREDICT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PREDICTIVE_ANALYTICS
tags: [dbms_predictive_analytics]
source_file: DBMS_PREDICTIVE_ANALYTICS.html
---

# DBMS_PREDICTIVE_ANALYTICS.PREDICT

The PREDICT procedure predicts the values of a target column.

## Syntax

```sql
DBMS_PREDICTIVE_ANALYTICS.PREDICT (
    accuracy                  OUT NUMBER,
    data_table_name           IN VARCHAR2,
    case_id_column_name       IN VARCHAR2,
    target_column_name        IN VARCHAR2,
    result_table_name         IN VARCHAR2,
    data_schema_name          IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| accuracy | NUMBER | OUT | Output parameter that returns the predictive confidence, a measure of the accuracy of the predicted values. The predictive confidence for a categorical target is the most common target value; the predictive confidence for a numerical target is the mean. |
| data_table_name | VARCHAR2 | IN | Name of the input table or view. |
| case_id_column_name | VARCHAR2 | IN | Name of the column that uniquely identifies each case (record) in the input data. |
| target_column_name | VARCHAR2 | IN | Name of the column to predict. |
| result_table_name | VARCHAR2 | IN | Name of the table where results will be saved. |
| data_schema_name | VARCHAR2 | IN | Name of the schema where the input table or view resides and where the result table is created. Default: the current schema. |

## Usage Notes

The input data must contain some records where the target value is known (not NULL ). These records are used by the procedure to train and test a model that makes the predictions. Note: PREDICT supports DATE and TIMESTAMP datatypes in addition to the numeric, character, and nested datatypes supported by Oracle Data Mining models. Data requirements for Oracle Data Mining are described in Oracle Data Mining User's Guide. The PREDICT procedure creates a result table that contains a predicted target value for every record. The result table is described in the Usage Notes. Note: PREDICT supports DATE and TIMESTAMP datatypes in addition to the numeric, character, and nested datatypes supported by Oracle Data Mining models. Data requirements for Oracle Data Mining are described in Oracle Data Mining User's Guide. Syntax DBMS_PREDICTIVE_ANALYTICS.PREDICT ( accuracy OUT NUMBER, data_table_name IN VARCHAR2, case_id_column_name IN VARCHAR2, target_column_name IN VARCHAR2, result_table_name IN VARCHAR2, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 129-4 PREDICT Procedure Parameters Parameter Description accuracy Output parameter that returns the predictive confidence, a measure of the accuracy of the predicted values. The predictive confidence for a categorical target is the most common target value; the predictive confidence for a numerical target is the mean. data_table_name Name of the input table or view. case_id_column_name Name of the column that uniquely identifies each case (record) in the input data. target_column_name Name of the column to predict. result_table_name Name of the table where results will be saved. data_schema_name Name of the schema where the input table or view resides and where the result table is created. Default: the current schema. Usage Notes The PREDICT procedure creates a result table with the columns described in Table 129-5 . Table 129-5 PREDICT Procedure Result Table Column Name Datatype Description Case ID column name VARCHAR2 or NUMBER The name of the case ID column in the input data. PREDICTION VARCHAR2 or NUMBER The predicted value of the target column for the given case. PROBABILITY NUMBER For classification (categorical target), the probability of the prediction. For regression problems (numerical target), this column contains NULL . Note: Make sure that the name of the case ID column is not ' PREDICTION ' or ' PROBABILITY '. Predictions are returned for all cases whether or not they contained target values in the input. Predicted values for known cases may be interesting in some situations. For example, you could perform deviation analysis to compare predicted values and actual values.