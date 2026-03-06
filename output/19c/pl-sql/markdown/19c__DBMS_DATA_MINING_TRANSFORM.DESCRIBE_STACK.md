---
id: 19c__DBMS_DATA_MINING_TRANSFORM.DESCRIBE_STACK
name: DBMS_DATA_MINING_TRANSFORM.DESCRIBE_STACK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.DESCRIBE_STACK

This procedure describes the columns of the data table after a list of transformations has been applied.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.DESCRIBE_STACK (
     xform_list           IN  TRANSFORM_LIST,
     data_table_name      IN  VARCHAR2,
     describe_list        OUT DESCRIBE_LIST,
     data_schema_name     IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xform_list | TRANSFORM_LIST | IN | A list of transformations. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| describe_list | DESCRIBE_LIST | OUT | Descriptions of the columns in the data table after the transformations specified in xform_list have been applied. See Table 48-1 for a description of the DESCRIBE_LIST object type. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Only the columns that are specified in the transformation list are transformed. The remaining columns in the data table are included in the output without changes. To create a view of the data table after the transformations have been applied, use the XFORM_STACK Procedure . Syntax DBMS_DATA_MINING_TRANSFORM.DESCRIBE_STACK ( xform_list IN TRANSFORM_LIST, data_table_name IN VARCHAR2, describe_list OUT DESCRIBE_LIST, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-18 DESCRIBE_STACK Procedure Parameters Parameter Description xform_list A list of transformations. See Table 48-1 for a description of the TRANSFORM_LIST object type. data_table_name Name of the table containing the data to be transformed describe_list Descriptions of the columns in the data table after the transformations specified in xform_list have been applied. See Table 48-1 for a description of the DESCRIBE_LIST object type. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " for information about transformation lists and embedded transformations. Examples This example shows the column name and datatype, the column name length, and the column maximum length for the view dmuser.cust_info after the transformation list has been applied. All the transformations are user-specified. The results of DESCRIBE_STACK do not include one of the columns in the original table, because the SET_TRANSFORM procedure sets that column to NULL . CREATE OR REPLACE VIEW cust_info AS SELECT a.cust_id, c.country_id, c.cust_year_of_birth, CAST(COLLECT(DM_Nested_Numerical( b.prod_name, 1)) AS DM_Nested_Numericals) custprods FROM sh.sales a, sh.products b, sh.customers c WHERE a.prod_id = b.prod_id AND a.cust_id=c.cust_id and a.cust_id between 100001 AND 105000 GROUP BY a.cust_id, country_id, cust_year_of_birth; describe cust_info Name Null? Type ----------------------------------------- -------- ---------------------------- CUST_ID NOT NULL NUMBER COUNTRY_ID NOT NULL NUMBER CUST_YEAR_OF_BIRTH NOT NULL NUMBER(4) CUSTPRODS SYS.DM_NESTED_NUMERICALS DECLARE cust_stack dbms_data_mining_transform.TRANSFORM_LIST; cust_cols dbms_data_mining_transform.DESCRIBE_LIST; BEGIN dbms_data_mining_transform.SET_TRANSFORM (cust_stack, 'country_id', NULL, 'country_id/10', 'country_id*10'); dbms_data_mining_transform.SET_TRANSFORM (cust_stack, 'cust_year_of_birth', NULL, NULL, NULL); dbms_data_mining_transform.SET_TRANSFORM (cust_stack, 'custprods', 'Mouse Pad', 'value*100', 'value/100'); dbms_data_mining_transform.DESCRIBE_STACK ( xform_list => cust_stack, data_table_name => 'cust_info', describe_list => cust_cols); dbms_output.put_line('===='); for i in 1..cust_cols.COUNT loop dbms_output.put_line('COLUMN_NAME: '||cust_cols(i).col_name); dbms_output.put_line('COLUMN_TYPE: '||cust_cols(i).col_type); dbms_output.put_line('COLUMN_NAME_LEN: '||cust_cols(i).col_name_len); dbms_output.put_line('COLUMN_MAX_LEN: '||cust_cols(i).col_max_len); dbms_output.put_line('===='); END loop; END; / ==== COLUMN_NAME: CUST_ID COLUMN_TYPE: 2 COLUMN_NAME_LEN: 7 COLUMN_MAX_LEN: 22 ==== COLUMN_NAME: COUNTRY_ID COLUMN_TYPE: 2 COLUMN_NAME_LEN: 10 COLUMN_MAX_LEN: 22 ==== COLUMN_NAME: CUSTPRODS COLUMN_TYPE: 100001 COLUMN_NAME_LEN: 9 COLUMN_MAX_LEN: 40 ====