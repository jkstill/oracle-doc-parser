---
id: 19c__DBMS_DATA_MINING_TRANSFORM.INSERT_BIN_NUM_QTILE
name: DBMS_DATA_MINING_TRANSFORM.INSERT_BIN_NUM_QTILE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.INSERT_BIN_NUM_QTILE

This procedure performs numerical binning and inserts the transformation definitions in a transformation definition table. The procedure calls the SQL NTILE function to order the data and divide it equally into the specified number of bins (quantiles).

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.INSERT_BIN_NUM_QTILE (
    bin_table_name       IN VARCHAR2,
    data_table_name      IN VARCHAR2,
    bin_num              IN PLS_INTEGER DEFAULT 10,
    exclude_list         IN COLUMN_LIST DEFAULT NULL,
    bin_schema_name      IN VARCHAR2 DEFAULT NULL,
    data_schema_name     IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bin_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical binning. You can use the CREATE_BIN_NUM Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) VAL NUMBER BIN VARCHAR2(4000) CREATE_BIN_NUM creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_BIN_NUM_QTILE . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| bin_num | PLS_INTEGER | IN | Number of bins. No binning occurs if bin_num is 0 or NULL . The default number of bins is 10. |
| exclude_list | COLUMN_LIST | IN | List of numerical columns to be excluded from the binning process. If you do not specify exclude_list , all numerical columns in the data source are binned. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| bin_schema_name | VARCHAR2 | IN | Schema of bin_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

INSERT_BIN_NUM_QTILE bins all the NUMBER and FLOAT columns in the data source unless you specify a list of columns to ignore. Syntax DBMS_DATA_MINING_TRANSFORM.INSERT_BIN_NUM_QTILE ( bin_table_name IN VARCHAR2, data_table_name IN VARCHAR2, bin_num IN PLS_INTEGER DEFAULT 10, exclude_list IN COLUMN_LIST DEFAULT NULL, bin_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-23 INSERT_BIN_NUM_QTILE Procedure Parameters Parameter Description bin_table_name Name of the transformation definition table for numerical binning. You can use the CREATE_BIN_NUM Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) VAL NUMBER BIN VARCHAR2(4000) CREATE_BIN_NUM creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_BIN_NUM_QTILE . data_table_name Name of the table containing the data to be transformed bin_num Number of bins. No binning occurs if bin_num is 0 or NULL . The default number of bins is 10. exclude_list List of numerical columns to be excluded from the binning process. If you do not specify exclude_list , all numerical columns in the data source are binned. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') bin_schema_name Schema of bin_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. After dividing the data into quantiles, the NTILE function distributes any remainder values one for each quantile, starting with the first. See Oracle Database SQL Language Reference for details. Columns with all NULL values are ignored by INSERT_BIN_NUM_QTILE . Examples In this example, INSERT_BIN_NUM_QTILE computes the bin boundaries for the cust_year_of_birth and cust_credit_limit columns in sh.customers and inserts the transformations in a transformation definition table. The STACK_BIN_NUM Procedure creates a transformation list from the contents of the definition table. The SQL expression that computes the transformation is shown in STACK_VIEW . The view is for display purposes only; it cannot be used to embed the transformations in a model. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_year_of_birth, cust_credit_limit, cust_city FROM sh.customers; DESCRIBE mining_data Name Null? Type --------------------------------------- -------- ----------------------------- CUST_ID NOT NULL NUMBER CUST_YEAR_OF_BIRTH NOT NULL NUMBER(4) CUST_CREDIT_LIMIT NUMBER CUST_CITY NOT NULL VARCHAR2(30) BEGIN dbms_data_mining_transform.CREATE_BIN_NUM( bin_table_name => 'bin_tbl'); dbms_data_mining_transform.INSERT_BIN_NUM_QTILE ( bin_table_name => 'bin_tbl', data_table_name => 'mining_data', bin_num => 3, exclude_list => dbms_data_mining_transform.COLUMN_LIST('cust_id')); END; / set numwidth 8 column val off column col format a20 column bin format a10 SELECT col, val, bin FROM bin_tbl ORDER BY col ASC, val ASC; COL VAL BIN -------------------- -------- ---------- CUST_CREDIT_LIMIT 1500 CUST_CREDIT_LIMIT 3000 1 CUST_CREDIT_LIMIT 9000 2 CUST_CREDIT_LIMIT 15000 3 CUST_YEAR_OF_BIRTH 1913 CUST_YEAR_OF_BIRTH 1949 1 CUST_YEAR_OF_BIRTH 1965 2 CUST_YEAR_OF_BIRTH 1990 3 DECLARE xforms dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.STACK_BIN_NUM ( bin_table_name => 'bin_tbl', xform_list => xforms); dbms_data_mining_transform.XFORM_STACK ( xform_list => xforms, data_table_name => 'mining_data', xform_view_name => 'stack_view'); END; / set long 3000 SELECT text FROM user_views WHERE view_name in 'STACK_VIEW'; TEXT -------------------------------------------------------------------------------- SELECT "CUST_ID",CASE WHEN "CUST_YEAR_OF_BIRTH"<1913 THEN NULL WHEN "CUST_YEAR_O F_BIRTH"<=1949 THEN '1' WHEN "CUST_YEAR_OF_BIRTH"<=1965 THEN '2' WHEN "CUST_YEAR _OF_BIRTH"<=1990 THEN '3' END "CUST_YEAR_OF_BIRTH",CASE WHEN "CUST_CREDIT_LIMIT" <1500 THEN NULL WHEN "CUST_CREDIT_LIMIT"<=3000 THEN '1' WHEN "CUST_CREDIT_LIMIT" <=9000 THEN '2' WHEN "CUST_CREDIT_LIMIT"<=15000 THEN '3' END "CUST_CREDIT_LIMIT" ,"CUST_CITY" FROM mining_data