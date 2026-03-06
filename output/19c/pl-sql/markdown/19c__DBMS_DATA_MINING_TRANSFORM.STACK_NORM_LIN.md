---
id: 19c__DBMS_DATA_MINING_TRANSFORM.STACK_NORM_LIN
name: DBMS_DATA_MINING_TRANSFORM.STACK_NORM_LIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.STACK_NORM_LIN

This procedure adds linear normalization transformations to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.STACK_NORM_LIN (
     norm_table_name     IN       VARCHAR2,
     xform_list          IN OUT   NOCOPY TRANSFORM_LIST,
     norm_schema_name    IN       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| norm_table_name | VARCHAR2 | IN | Name of the transformation definition table for linear normalization. You can use the CREATE_NORM_LIN Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_NORM_LIN .To populate the table, you can use one of the INSERT procedures for normalization or you can write your own SQL. See Table 48-16 . |
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| norm_schema_name | VARCHAR2 | IN | Schema of norm_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.STACK_NORM_LIN ( norm_table_name IN VARCHAR2, xform_list IN OUT NOCOPY TRANSFORM_LIST, norm_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-40 STACK_NORM_LIN Procedure Parameters Parameter Description norm_table_name Name of the transformation definition table for linear normalization. You can use the CREATE_NORM_LIN Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_NORM_LIN .To populate the table, you can use one of the INSERT procedures for normalization or you can write your own SQL. See Table 48-16 . xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. norm_schema_name Schema of norm_table_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . The following sections are especially relevant: " About Transformation Lists " " About Stacking " " Nested Data Transformations " Examples This example shows how the column cust_credit_limit could be normalized in a transformation list called mining_data_stack . Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, country_id, cust_postal_code, cust_credit_limit FROM sh.customers; BEGIN dbms_data_mining_transform.create_norm_lin ('norm_lin_tbl'); dbms_data_mining_transform.insert_norm_lin_minmax ( norm_table_name => 'norm_lin_tbl', data_table_name => 'mining_data', exclude_list => dbms_data_mining_transform.COLUMN_LIST('cust_id', 'country_id')); END; / SELECT * FROM norm_lin_tbl; COL ATT SHIFT SCALE -------------------- ----- ------ ------ CUST_CREDIT_LIMIT 1500 13500 DECLARE MINING_DATA_STACK dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.stack_norm_lin ( norm_table_name => 'norm_lin_tbl', xform_list => mining_data_stack); dbms_data_mining_transform.XFORM_STACK ( xform_list => mining_data_stack, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack_view'); END; / SELECT * FROM mining_data WHERE cust_id between 1 and 10 ORDER BY cust_id; CUST_ID COUNTRY_ID CUST_POSTAL_CODE CUST_CREDIT_LIMIT ------- ---------- -------------------- ----------------- 1 52789 30828 9000 2 52778 86319 10000 3 52770 88666 1500 4 52770 87551 1500 5 52789 59200 1500 6 52769 77287 1500 7 52790 38763 1500 8 52790 58488 3000 9 52770 63033 3000 10 52790 52602 3000 SELECT * FROM mining_data_stack_view WHERE cust_id between 1 and 10 ORDER BY cust_id; CUST_ID COUNTRY_ID CUST_POSTAL_CODE CUST_CREDIT_LIMIT ------- ---------- -------------------- ----------------- 1 52789 30828 .55556 2 52778 86319 .62963 3 52770 88666 0 4 52770 87551 0 5 52789 59200 0 6 52769 77287 0 7 52790 38763 0 8 52790 58488 .11111 9 52770 63033 .11111 10 52790 52602 .11111 Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example.