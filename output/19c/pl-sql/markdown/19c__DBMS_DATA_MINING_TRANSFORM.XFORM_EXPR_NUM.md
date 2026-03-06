---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_NUM
name: DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_NUM

This procedure creates a view that implements the specified numeric transformations. Only the columns that you specify are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_NUM (
     expr_pattern       IN       VARCHAR2,
     data_table_name    IN       VARCHAR2,
     xform_view_name    IN       VARCHAR2,
     exclude_list       IN       COLUMN_LIST DEFAULT NULL,
     include_list       IN       COLUMN_LIST DEFAULT NULL,
     col_pattern        IN       VARCHAR2 DEFAULT ':col',
     data_schema_name   IN       VARCHAR2 DEFAULT NULL,
     xform_schema_name  IN       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| expr_pattern | VARCHAR2 | IN | A numeric transformation expression |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in expr_pattern and col_pattern . |
| exclude_list | COLUMN_LIST | IN | List of numerical columns to exclude. If NULL , no numerical columns are excluded. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| include_list | COLUMN_LIST | IN | List of numeric columns to include. If NULL , all numeric columns are included. The format of include_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| col_pattern | VARCHAR2 | IN | The value within expr_pattern that will be replaced with a column name. The value of col_pattern is case-sensitive. The default value of col_pattern is ':col' |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_NUM ( expr_pattern IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, exclude_list IN COLUMN_LIST DEFAULT NULL, include_list IN COLUMN_LIST DEFAULT NULL, col_pattern IN VARCHAR2 DEFAULT ':col', data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-45 XFORM_EXPR_NUM Procedure Parameters Parameter Description expr_pattern A numeric transformation expression data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in expr_pattern and col_pattern . exclude_list List of numerical columns to exclude. If NULL , no numerical columns are excluded. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') include_list List of numeric columns to include. If NULL , all numeric columns are included. The format of include_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') col_pattern The value within expr_pattern that will be replaced with a column name. The value of col_pattern is case-sensitive. The default value of col_pattern is ':col' data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes The XFORM_EXPR_NUM procedure constructs numeric transformation expressions from the specified expression pattern ( expr_pattern ) by replacing every occurrence of the specified column pattern ( col_pattern ) with an actual column name. XFORM_EXPR_NUM uses the SQL REPLACE function to construct the transformation expressions. REPLACE ( expr_pattern , col_pattern ,'" column_name "') || '" column_name "' If there is a column match, then the replacement is made in the transformation expression; if there is not a match, then the column is used without transformation. See: Oracle Database SQL Language Reference for information about the REPLACE function Because of the include and exclude list parameters, the XFORM_EXPR_NUM and XFORM_EXPR_STR procedures allow you to easily specify individual columns for transformation within large data sets. The other XFORM_ * procedures support an exclude list only. In these procedures, you must enumerate every column that you do not want to transform. See " Operational Notes " See: Oracle Database SQL Language Reference for information about the REPLACE function Examples This example creates a view that transforms the datatype of numeric columns. describe customers Name Null? Type ----------------------------------- -------- ------------------------ CUST_ID NOT NULL NUMBER CUST_MARITAL_STATUS VARCHAR2(20) OCCUPATION VARCHAR2(21) AGE NUMBER YRS_RESIDENCE NUMBER BEGIN DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_NUM( expr_pattern => 'to_char(:col)', data_table_name => 'customers', xform_view_name => 'cust_nonum_view', exclude_list => dbms_data_mining_transform.COLUMN_LIST( 'cust_id'), include_list => null, col_pattern => ':col'); END; / describe cust_nonum_view Name Null? Type ----------------------------------- -------- ------------------------ CUST_ID NOT NULL NUMBER CUST_MARITAL_STATUS VARCHAR2(20) OCCUPATION VARCHAR2(21) AGE VARCHAR2(40) YRS_RESIDENCE VARCHAR2(40)