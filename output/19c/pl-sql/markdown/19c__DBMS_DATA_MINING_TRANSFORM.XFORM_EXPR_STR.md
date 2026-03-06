---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_STR
name: DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_STR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_STR

This procedure creates a view that implements the specified categorical transformations. Only the columns that you specify are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_STR (
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
| expr_pattern | VARCHAR2 | IN | A character transformation expression |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in expr_pattern and col_pattern . |
| exclude_list | COLUMN_LIST | IN | List of categorical columns to exclude. If NULL , no categorical columns are excluded. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| include_list | COLUMN_LIST | IN | List of character columns to include. If NULL , all character columns are included. The format of include_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| col_pattern | VARCHAR2 | IN | The value within expr_pattern that will be replaced with a column name. The value of col_pattern is case-sensitive. The default value of col_pattern is ':col' |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_STR ( expr_pattern IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, exclude_list IN COLUMN_LIST DEFAULT NULL, include_list IN COLUMN_LIST DEFAULT NULL, col_pattern IN VARCHAR2 DEFAULT ':col', data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-46 XFORM_EXPR_STR Procedure Parameters Parameter Description expr_pattern A character transformation expression data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in expr_pattern and col_pattern . exclude_list List of categorical columns to exclude. If NULL , no categorical columns are excluded. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') include_list List of character columns to include. If NULL , all character columns are included. The format of include_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') col_pattern The value within expr_pattern that will be replaced with a column name. The value of col_pattern is case-sensitive. The default value of col_pattern is ':col' data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes The XFORM_EXPR_STR procedure constructs character transformation expressions from the specified expression pattern ( expr_pattern ) by replacing every occurrence of the specified column pattern ( col_pattern ) with an actual column name. XFORM_EXPR_STR uses the SQL REPLACE function to construct the transformation expressions. REPLACE ( expr_pattern , col_pattern ,'" column_name "') || '" column_name "' If there is a column match, then the replacement is made in the transformation expression; if there is not a match, then the column is used without transformation. See: Oracle Database SQL Language Reference for information about the REPLACE function Because of the include and exclude list parameters, the XFORM_EXPR_STR and XFORM_EXPR_NUM procedures allow you to easily specify individual columns for transformation within large data sets. The other XFORM_ * procedures support an exclude list only. In these procedures, you must enumerate every column that you do not want to transform. See " Operational Notes " See: Oracle Database SQL Language Reference for information about the REPLACE function Examples This example creates a view that transforms character columns to upper case. describe customers Name Null? Type ----------------------------------- -------- ------------------------ CUST_ID NOT NULL NUMBER CUST_MARITAL_STATUS VARCHAR2(20) OCCUPATION VARCHAR2(21) AGE NUMBER YRS_RESIDENCE NUMBER SELECT cust_id, cust_marital_status, occupation FROM customers WHERE cust_id > 102995 ORDER BY cust_id desc; CUST_ID CUST_MARITAL_STATUS OCCUPATION ------- -------------------- --------------------- 103000 Divorc. Cleric. 102999 Married Cleric. 102998 Married Exec. 102997 Married Exec. 102996 NeverM Other BEGIN DBMS_DATA_MINING_TRANSFORM.XFORM_EXPR_STR( expr_pattern => 'upper(:col)', data_table_name => 'customers', xform_view_name => 'cust_upcase_view'); END; / describe cust_upcase_view Name Null? Type ----------------------------- -------- -------------------- CUST_ID NOT NULL NUMBER CUST_MARITAL_STATUS VARCHAR2(20) OCCUPATION VARCHAR2(21) AGE NUMBER YRS_RESIDENCE NUMBER SELECT cust_id, cust_marital_status, occupation FROM cust_upcase_view WHERE cust_id > 102995 ORDER BY cust_id desc; CUST_ID CUST_MARITAL_STATUS OCCUPATION ------- -------------------- --------------------- 103000 DIVORC. CLERIC. 102999 MARRIED CLERIC. 102998 MARRIED EXEC. 102997 MARRIED EXEC. 102996 NEVERM OTHER