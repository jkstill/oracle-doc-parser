---
id: 19c__DBMS_DATA_MINING_TRANSFORM.STACK_MISS_CAT
name: DBMS_DATA_MINING_TRANSFORM.STACK_MISS_CAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.STACK_MISS_CAT

This procedure adds categorical missing value transformations to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.STACK_MISS_CAT (
     miss_table_name     IN       VARCHAR2,
     xform_list          IN OUT   NOCOPY TRANSFORM_LIST,
     miss_schema_name    IN       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table for categorical missing value treatment. You can use the CREATE_MISS_CAT Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_MISS_CAT . To populate the table, you can use the INSERT_MISS_CAT_MODE Procedure or you can write your own SQL. See Table 48-12 . |
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.STACK_MISS_CAT ( miss_table_name IN VARCHAR2, xform_list IN OUT NOCOPY TRANSFORM_LIST, miss_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-38 STACK_MISS_CAT Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table for categorical missing value treatment. You can use the CREATE_MISS_CAT Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_MISS_CAT . To populate the table, you can use the INSERT_MISS_CAT_MODE Procedure or you can write your own SQL. See Table 48-12 . xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . The following sections are especially relevant: " About Transformation Lists " " About Stacking " " Nested Data Transformations " Examples This example shows how the missing values in the column cust_marital_status could be replaced with the mode in a transformation list called mining_data_stack . Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, country_id, cust_marital_status FROM sh.customers where cust_id BETWEEN 1 AND 10; BEGIN dbms_data_mining_transform.create_miss_cat ('miss_cat_tbl'); dbms_data_mining_transform.insert_miss_cat_mode ('miss_cat_tbl', 'mining_data'); END; / DECLARE MINING_DATA_STACK dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.stack_miss_cat ( miss_table_name => 'miss_cat_tbl', xform_list => mining_data_stack); dbms_data_mining_transform.XFORM_STACK ( xform_list => mining_data_stack, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack_view'); END; / SELECT * FROM mining_data ORDER BY cust_id; CUST_ID COUNTRY_ID CUST_MARITAL_STATUS ------- ---------- -------------------- 1 52789 2 52778 3 52770 4 52770 5 52789 6 52769 single 7 52790 single 8 52790 married 9 52770 divorced 10 52790 widow SELECT * FROM mining_data_stack_view ORDER By cust_id; CUST_ID COUNTRY_ID CUST_MARITAL_STATUS ------- ----------- -------------------- 1 52789 single 2 52778 single 3 52770 single 4 52770 single 5 52789 single 6 52769 single 7 52790 single 8 52790 married 9 52770 divorced 10 52790 widow Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example.