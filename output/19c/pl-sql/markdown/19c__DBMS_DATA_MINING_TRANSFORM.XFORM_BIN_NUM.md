---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_BIN_NUM
name: DBMS_DATA_MINING_TRANSFORM.XFORM_BIN_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_BIN_NUM

This procedure creates a view that implements the numerical binning transformations specified in a definition table. Only the columns that are specified in the definition table are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_BIN_NUM (
     bin_table_name     IN VARCHAR2,
     data_table_name    IN VARCHAR2,
     xform_view_name    IN VARCHAR2,
     literal_flag       IN BOOLEAN DEFAULT FALSE,
     bin_schema_name    IN VARCHAR2 DEFAULT NULL,
     data_schema_name   IN VARCHAR2 DEFAULT NULL,
     xform_schema_name  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bin_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical binning. You can use the CREATE_BIN_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_BIN_NUM . To populate the table, you can use one of the INSERT procedures for numerical binning or you can write your own SQL. See " Table 48-6 " . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in bin_table_name . |
| literal_flag | BOOLEAN | IN | Indicates whether the values in the bin column in the transformation definition table are valid SQL literals. When literal_flag is FALSE (the default), the bin identifiers will be transformed to SQL literals by surrounding them with single quotes. Set literal_flag to TRUE if the bin identifiers are numbers that should have a numeric datatype, as is the case for an O-Cluster model. See " INSERT_BIN_NUM_EQWIDTH Procedure " for an example. |
| bin_schema_name | VARCHAR2 | IN | Schema of bin_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_BIN_NUM ( bin_table_name IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, literal_flag IN BOOLEAN DEFAULT FALSE, bin_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-42 XFORM_BIN_NUM Procedure Parameters Parameter Description bin_table_name Name of the transformation definition table for numerical binning. You can use the CREATE_BIN_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_BIN_NUM . To populate the table, you can use one of the INSERT procedures for numerical binning or you can write your own SQL. See " Table 48-6 " . data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in bin_table_name . literal_flag Indicates whether the values in the bin column in the transformation definition table are valid SQL literals. When literal_flag is FALSE (the default), the bin identifiers will be transformed to SQL literals by surrounding them with single quotes. Set literal_flag to TRUE if the bin identifiers are numbers that should have a numeric datatype, as is the case for an O-Cluster model. See " INSERT_BIN_NUM_EQWIDTH Procedure " for an example. bin_schema_name Schema of bin_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . Examples This example creates a view that bins the cust_credit_limit column. The data source consists of three columns from sh.customer. describe mining_data Name Null? Type -------------------------------------- -------- ------------------------ CUST_ID NOT NULL NUMBER CUST_POSTAL_CODE NOT NULL VARCHAR2(10) CUST_CREDIT_LIMIT NUMBER column cust_credit_limit off SELECT * FROM mining_data WHERE cust_id between 104066 and 104069; CUST_ID CUST_POSTAL_CODE CUST_CREDIT_LIMIT --------- ------------------ -------------------- 104066 69776 7000 104067 52602 9000 104068 55787 11000 104069 55977 5000 BEGIN dbms_data_mining_transform.create_bin_num( bin_table_name => 'bin_num_tbl'); dbms_data_mining_transform.insert_autobin_num_eqwidth( bin_table_name => 'bin_num_tbl', data_table_name => 'mining_data', bin_num => 5, max_bin_num => 10, exclude_list => dbms_data_mining_transform.COLUMN_LIST('cust_id')); dbms_data_mining_transform.xform_bin_num( bin_table_name => 'bin_num_tbl', data_table_name => 'mining_data', xform_view_name => 'mining_data_view'); END; / describe mining_data_view Name Null? Type ------------------------------------ -------- ------------------------ CUST_ID NOT NULL NUMBER CUST_POSTAL_CODE NOT NULL VARCHAR2(10) CUST_CREDIT_LIMIT VARCHAR2(2) col cust_credit_limit on col cust_credit_limit format a25 SELECT * FROM mining_data_view WHERE cust_id between 104066 and 104069; CUST_ID CUST_POSTAL_CODE CUST_CREDIT_LIMIT ---------- -------------------- ------------------------- 104066 69776 5 104067 52602 6 104068 55787 8 104069 55977 3 set long 2000 SELECT text FROM user_views WHERE view_name IN 'MINING_DATA_VIEW'; TEXT -------------------------------------------------------------------------------- SELECT "CUST_ID","CUST_POSTAL_CODE",CASE WHEN "CUST_CREDIT_LIMIT"<1500 THEN NULL WHEN "CUST_CREDIT_LIMIT"<=2850 THEN '1' WHEN "CUST_CREDIT_LIMIT"<=4200 THEN '2' WHEN "CUST_CREDIT_LIMIT"<=5550 THEN '3' WHEN "CUST_CREDIT_LIMIT"<=6900 THEN '4' WHEN "CUST_CREDIT_LIMIT"<=8250 THEN '5' WHEN "CUST_CREDIT_LIMIT"<=9600 THEN '6' WHEN "CUST_CREDIT_LIMIT"<=10950 THEN '7' WHEN "CUST_CREDIT_LIMIT"<=12300 THEN ' 8' WHEN "CUST_CREDIT_LIMIT"<=13650 THEN '9' WHEN "CUST_CREDIT_LIMIT"<=15000 THEN '10' END "CUST_CREDIT_LIMIT" FROM mining_data