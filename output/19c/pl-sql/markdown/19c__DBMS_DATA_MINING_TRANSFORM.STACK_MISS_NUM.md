---
id: 19c__DBMS_DATA_MINING_TRANSFORM.STACK_MISS_NUM
name: DBMS_DATA_MINING_TRANSFORM.STACK_MISS_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.STACK_MISS_NUM

This procedure adds numeric missing value transformations to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.STACK_MISS_NUM (
     miss_table_name     IN       VARCHAR2,
     xform_list          IN OUT   NOCOPY TRANSFORM_LIST,
     miss_schema_name    IN       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical missing value treatment. You can use the CREATE_MISS_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_MISS_NUM . To populate the table, you can use the INSERT_MISS_NUM_MEAN Procedure or you can write your own SQL. See Table 48-14 . |
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.STACK_MISS_NUM ( miss_table_name IN VARCHAR2, xform_list IN OUT NOCOPY TRANSFORM_LIST, miss_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-39 STACK_MISS_NUM Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table for numerical missing value treatment. You can use the CREATE_MISS_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_MISS_NUM . To populate the table, you can use the INSERT_MISS_NUM_MEAN Procedure or you can write your own SQL. See Table 48-14 . xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . The following sections are especially relevant: " About Transformation Lists " " About Stacking " " Nested Data Transformations " Examples This example shows how the missing values in the column cust_credit_limit could be replaced with the mean in a transformation list called mining_data_stack . Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example. describe mining_data Name Null? Type ----------------------------------------------------- -------- ----- CUST_ID NOT NULL NUMBER CUST_CREDIT_LIMIT NUMBER BEGIN dbms_data_mining_transform.create_miss_num ('miss_num_tbl'); dbms_data_mining_transform.insert_miss_num_mean ('miss_num_tbl','mining_data'); END; / SELECT * FROM miss_num_tbl; COL ATT VAL -------------------- ----- ------ CUST_ID 5.5 CUST_CREDIT_LIMIT 185.71 DECLARE MINING_DATA_STACK dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.STACK_MISS_NUM ( miss_table_name => 'miss_num_tbl', xform_list => mining_data_stack); dbms_data_mining_transform.XFORM_STACK ( xform_list => mining_data_stack, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack_view'); END; / -- Before transformation SELECT * FROM mining_data ORDER BY cust_id; CUST_ID CUST_CREDIT_LIMIT ------- ----------------- 1 100 2 3 200 4 5 150 6 400 7 150 8 9 100 10 200 -- After transformation SELECT * FROM mining_data_stack_view ORDER BY cust_id; CUST_ID CUST_CREDIT_LIMIT ------- ----------------- 1 100 2 185.71 3 200 4 185.71 5 150 6 400 7 150 8 185.71 9 100 10 200 Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example.