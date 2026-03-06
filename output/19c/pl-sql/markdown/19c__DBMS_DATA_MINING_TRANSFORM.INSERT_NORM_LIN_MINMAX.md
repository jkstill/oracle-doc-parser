---
id: 19c__DBMS_DATA_MINING_TRANSFORM.INSERT_NORM_LIN_MINMAX
name: DBMS_DATA_MINING_TRANSFORM.INSERT_NORM_LIN_MINMAX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.INSERT_NORM_LIN_MINMAX

This procedure performs linear normalization and inserts the transformation definitions in a transformation definition table.

## Syntax

```sql
shift = min
scale = max - min
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| norm_table_name |  |  | Name of the transformation definition table for linear normalization. You can use the CREATE_NORM_LIN Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) SHIFT NUMBER SCALE NUMBER CREATE_NORM_LIN creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_NORM_LIN_MINMAX . |
| data_table_name |  |  | Name of the table containing the data to be transformed |
| exclude_list |  |  | List of numerical columns to be excluded from normalization. If you do not specify exclude_list , all numerical columns are transformed. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| round_num |  |  | The number of significant digits to use for the minimum and maximum. The default number is 6. |
| norm_schema_name |  |  | Schema of norm_table_name . If no schema is specified, the current schema is used. |
| data_schema_name |  |  | Schema of data_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

INSERT_NORM_LIN_MINMAX computes the minimum and maximum values from the data and sets the value of shift and scale as follows: shift = min scale = max - min Normalization is computed as: x_new = ( x_old - shift )/ scale INSERT_NORM_LIN_MINMAX rounds the value of scale to a specified number of significant digits before storing it in the transformation definition table. INSERT_NORM_LIN_MINMAX normalizes all the NUMBER and FLOAT columns in the data source unless you specify a list of columns to ignore. Syntax DBMS_DATA_MINING_TRANSFORM.INSERT_NORM_LIN_MINMAX ( norm_table_name IN VARCHAR2, data_table_name IN VARCHAR2, exclude_list IN COLUMN_LIST DEFAULT NULL, round_num IN PLS_INTEGER DEFAULT 6, norm_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-29 INSERT_NORM_LIN_MINMAX Procedure Parameters Parameter Description norm_table_name Name of the transformation definition table for linear normalization. You can use the CREATE_NORM_LIN Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) SHIFT NUMBER SCALE NUMBER CREATE_NORM_LIN creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_NORM_LIN_MINMAX . data_table_name Name of the table containing the data to be transformed exclude_list List of numerical columns to be excluded from normalization. If you do not specify exclude_list , all numerical columns are transformed. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') round_num The number of significant digits to use for the minimum and maximum. The default number is 6. norm_schema_name Schema of norm_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. Examples In this example, INSERT_NORM_LIN_MINMAX normalizes the cust_year_of_birth column and inserts the transformation in a transformation definition table. The STACK_NORM_LIN Procedure creates a transformation list from the contents of the definition table. The SQL expression that computes the transformation is shown in the view MINING_DATA_STACK . The view is for display purposes only; it cannot be used to embed the transformations in a model. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_gender, cust_year_of_birth FROM sh.customers; describe mining_data Name Null? Type ------------------------------------ -------- ---------------- CUST_ID NOT NULL NUMBER CUST_GENDER NOT NULL CHAR(1) CUST_YEAR_OF_BIRTH NOT NULL NUMBER(4) BEGIN dbms_data_mining_transform.CREATE_NORM_LIN( norm_table_name => 'norm_tbl'); dbms_data_mining_transform.INSERT_NORM_LIN_MINMAX( norm_table_name => 'norm_tbl', data_table_name => 'mining_data', exclude_list => dbms_data_mining_transform.COLUMN_LIST( 'cust_id'), round_num => 3); END; / SELECT col, shift, scale FROM norm_tbl; COL SHIFT SCALE ------------------------------ ---------- ---------- CUST_YEAR_OF_BIRTH 1910 77 DECLARE xforms dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.STACK_NORM_LIN ( norm_table_name => 'norm_tbl', xform_list => xforms); dbms_data_mining_transform.XFORM_STACK ( xform_list => xforms, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack'); END; / set long 3000 SELECT text FROM user_views WHERE view_name IN 'MINING_DATA_STACK'; TEXT -------------------------------------------------------------------------------- SELECT "CUST_ID","CUST_GENDER",("CUST_YEAR_OF_BIRTH"-1910)/77 "CUST_YEAR_OF_BIRT H" FROM mining_data