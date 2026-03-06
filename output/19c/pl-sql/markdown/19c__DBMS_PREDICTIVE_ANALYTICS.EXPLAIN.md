---
id: 19c__DBMS_PREDICTIVE_ANALYTICS.EXPLAIN
name: DBMS_PREDICTIVE_ANALYTICS.EXPLAIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PREDICTIVE_ANALYTICS
tags: [dbms_predictive_analytics]
source_file: DBMS_PREDICTIVE_ANALYTICS.html
---

# DBMS_PREDICTIVE_ANALYTICS.EXPLAIN

The EXPLAIN procedure identifies the attributes that are important in explaining the variation in values of a target column.

## Syntax

```sql
DBMS_PREDICTIVE_ANALYTICS.EXPLAIN (
     data_table_name     IN VARCHAR2,
     explain_column_name IN VARCHAR2,
     result_table_name   IN VARCHAR2,
     data_schema_name    IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| data_table_name | VARCHAR2 | IN | Name of input table or view |
| explain_column_name | VARCHAR2 | IN | Name of the column to be explained |
| result_table_name | VARCHAR2 | IN | Name of the table where results are saved |
| data_schema_name | VARCHAR2 | IN | Name of the schema where the input table or view resides and where the result table is created. Default: the current schema. |

## Usage Notes

The input data must contain some records where the target value is known (not NULL ). These records are used by the procedure to train a model that calculates the attribute importance. Note: EXPLAIN supports DATE and TIMESTAMP datatypes in addition to the numeric, character, and nested datatypes supported by Oracle Data Mining models. Data requirements for Oracle Data Mining are described in Oracle Data Mining User's Guide. The EXPLAIN procedure creates a result table that lists the attributes in order of their explanatory power. The result table is described in the Usage Notes. Note: EXPLAIN supports DATE and TIMESTAMP datatypes in addition to the numeric, character, and nested datatypes supported by Oracle Data Mining models. Data requirements for Oracle Data Mining are described in Oracle Data Mining User's Guide. Syntax DBMS_PREDICTIVE_ANALYTICS.EXPLAIN ( data_table_name IN VARCHAR2, explain_column_name IN VARCHAR2, result_table_name IN VARCHAR2, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 129-2 EXPLAIN Procedure Parameters Parameter Description data_table_name Name of input table or view explain_column_name Name of the column to be explained result_table_name Name of the table where results are saved data_schema_name Name of the schema where the input table or view resides and where the result table is created. Default: the current schema. Usage Notes The EXPLAIN procedure creates a result table with the columns described in Table 129-3 . Table 129-3 EXPLAIN Procedure Result Table Column Name Datatype Description ATTRIBUTE_NAME VARCHAR2(30) Name of a column in the input data; all columns except the explained column are listed in the result table. EXPLANATORY_VALUE NUMBER Value indicating how useful the column is for determining the value of the explained column. Higher values indicate greater explanatory power. Value can range from 0 to 1. An individual column's explanatory value is independent of other columns in the input table. The values are based on how strong each individual column correlates with the explained column. The value is affected by the number of records in the input table, and the relations of the values of the column to the values of the explain column. An explanatory power value of 0 implies there is no useful correlation between the column's values and the explain column's values. An explanatory power of 1 implies perfect correlation; such columns should be eliminated from consideration for PREDICT . In practice, an explanatory power equal to 1 is rarely returned. RANK NUMBER Ranking of explanatory power. Rows with equal values for explanatory_value have the same rank. Rank values are not skipped in the event of ties.