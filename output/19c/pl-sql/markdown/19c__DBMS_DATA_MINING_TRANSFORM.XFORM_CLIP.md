---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_CLIP
name: DBMS_DATA_MINING_TRANSFORM.XFORM_CLIP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_CLIP

This procedure creates a view that implements the clipping transformations specified in a definition table. Only the columns that are specified in the definition table are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_CLIP (
    clip_table_name       IN VARCHAR2, 
    data_table_name       IN VARCHAR2,
    xform_view_name       IN VARCHAR2,
    clip_schema_name      IN VARCHAR2 DEFAULT NULL,
    data_schema_name      IN VARCHAR2,DEFAULT NULL,
    xform_schema_name     IN VARCHAR2,DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| clip_table_name | VARCHAR2 | IN | Name of the transformation definition table for clipping. You can use the CREATE_CLIP Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_CLIP . To populate the table, you can use one of the INSERT procedures for clipping you can write your own SQL. See Table 48-8 . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in clip_table_name . |
| clip_schema_name | VARCHAR2 | IN | Schema of clip_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_CLIP ( clip_table_name IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, clip_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2,DEFAULT NULL, xform_schema_name IN VARCHAR2,DEFAULT NULL); Parameters Table 48-43 XFORM_CLIP Procedure Parameters Parameter Description clip_table_name Name of the transformation definition table for clipping. You can use the CREATE_CLIP Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_CLIP . To populate the table, you can use one of the INSERT procedures for clipping you can write your own SQL. See Table 48-8 . data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in clip_table_name . clip_schema_name Schema of clip_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Examples This example creates a view that clips the cust_credit_limit column. The data source consists of three columns from sh.customer. describe mining_data Name Null? Type ------------------------------ -------- ------------------------- CUST_ID NOT NULL NUMBER CUST_POSTAL_CODE NOT NULL VARCHAR2(10) CUST_CREDIT_LIMIT NUMBER BEGIN dbms_data_mining_transform.create_clip( clip_table_name => 'clip_tbl'); dbms_data_mining_transform.insert_clip_trim_tail( clip_table_name => 'clip_tbl', data_table_name => 'mining_data', tail_frac => 0.05, exclude_list => dbms_data_mining_transform.COLUMN_LIST('cust_id')); dbms_data_mining_transform.xform_clip( clip_table_name => 'clip_tbl', data_table_name => 'mining_data', xform_view_name => 'clip_view'); END; / describe clip_view Name Null? Type ----------------------------- -------- -------------------------- CUST_ID NOT NULL NUMBER CUST_POSTAL_CODE NOT NULL VARCHAR2(10) CUST_CREDIT_LIMIT NUMBER SELECT MIN(cust_credit_limit), MAX(cust_credit_limit) FROM mining_data; MIN(CUST_CREDIT_LIMIT) MAX(CUST_CREDIT_LIMIT) ---------------------- ---------------------- 1500 15000 SELECT MIN(cust_credit_limit), MAX(cust_credit_limit) FROM clip_view; MIN(CUST_CREDIT_LIMIT) MAX(CUST_CREDIT_LIMIT) ---------------------- ---------------------- 1500 11000 set long 2000 SELECT text FROM user_views WHERE view_name IN 'CLIP_VIEW'; TEXT -------------------------------------------------------------------------------- SELECT "CUST_ID","CUST_POSTAL_CODE",CASE WHEN "CUST_CREDIT_LIMIT" < 1500 THEN NU LL WHEN "CUST_CREDIT_LIMIT" > 11000 THEN NULL ELSE "CUST_CREDIT_LIMIT" END "CUST _CREDIT_LIMIT" FROM mining_data