---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_NORM_LIN
name: DBMS_DATA_MINING_TRANSFORM.XFORM_NORM_LIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_NORM_LIN

This procedure creates a view that implements the linear normalization transformations specified in a definition table. Only the columns that are specified in the definition table are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_NORM_LIN (
     norm_table_name      IN VARCHAR2,
     data_table_name      IN VARCHAR2,
     xform_view_name      IN VARCHAR2,
     norm_schema_name     IN VARCHAR2 DEFAULT NULL,
     data_schema_name     IN VARCHAR2 DEFAULT NULL,
     xform_schema_name    IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| norm_table_name | VARCHAR2 | IN | Name of the transformation definition table for linear normalization. You can use the CREATE_NORM_LIN Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_NORM_LIN . To populate the table, you can use one of the INSERT procedures for normalization or you can write your own SQL. See Table 48-12 . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in miss_table_name . |
| norm_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_NORM_LIN ( norm_table_name IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, norm_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-49 XFORM_NORM_LIN Procedure Parameters Parameter Description norm_table_name Name of the transformation definition table for linear normalization. You can use the CREATE_NORM_LIN Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_NORM_LIN . To populate the table, you can use one of the INSERT procedures for normalization or you can write your own SQL. See Table 48-12 . data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in miss_table_name . norm_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . Examples This example creates a view that normalizes the cust_year_of_birth and cust_credit_limit columns. The data source consists of three columns from sh.customer. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_year_of_birth, cust_credit_limit FROM sh.customers; describe mining_data Name Null? Type -------------------------------------- -------- -------------------------- CUST_ID NOT NULL NUMBER CUST_YEAR_OF_BIRTH NOT NULL NUMBER(4) CUST_CREDIT_LIMIT NUMBER SELECT * FROM mining_data WHERE cust_id > 104495 ORDER BY cust_year_of_birth; CUST_ID CUST_YEAR_OF_BIRTH CUST_CREDIT_LIMIT -------- ------------------ ----------------- 104496 1947 3000 104498 1954 10000 104500 1962 15000 104499 1970 3000 104497 1976 3000 BEGIN dbms_data_mining_transform.CREATE_NORM_LIN( norm_table_name => 'normx_tbl'); dbms_data_mining_transform.INSERT_NORM_LIN_MINMAX( norm_table_name => 'normx_tbl', data_table_name => 'mining_data', exclude_list => dbms_data_mining_transform.COLUMN_LIST( 'cust_id'), round_num => 3); END; / SELECT col, shift, scale FROM normx_tbl; COL SHIFT SCALE ------------------------------ -------- -------- CUST_YEAR_OF_BIRTH 1910 77 CUST_CREDIT_LIMIT 1500 13500 BEGIN DBMS_DATA_MINING_TRANSFORM.XFORM_NORM_LIN ( norm_table_name => 'normx_tbl', data_table_name => 'mining_data', xform_view_name => 'norm_view'); END; / SELECT * FROM norm_view WHERE cust_id > 104495 ORDER BY cust_year_of_birth; CUST_ID CUST_YEAR_OF_BIRTH CUST_CREDIT_LIMIT -------- ------------------ ----------------- 104496 .4805195 .1111111 104498 .5714286 .6296296 104500 .6753247 1 104499 .7792208 .1111111 104497 .8571429 .1111111 set long 2000 SQL> SELECT text FROM user_views WHERE view_name IN 'NORM_VIEW'; TEXT --------------------------------------------------------------------------- SELECT "CUST_ID",("CUST_YEAR_OF_BIRTH"-1910)/77 "CUST_YEAR_OF_BIRTH",("CUST _CREDIT_LIMIT"-1500)/13500 "CUST_CREDIT_LIMIT" FROM mining_data