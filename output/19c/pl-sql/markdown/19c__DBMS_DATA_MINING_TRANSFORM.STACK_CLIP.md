---
id: 19c__DBMS_DATA_MINING_TRANSFORM.STACK_CLIP
name: DBMS_DATA_MINING_TRANSFORM.STACK_CLIP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.STACK_CLIP

This procedure adds clipping transformations to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.STACK_CLIP (
          clip_table_name     IN            VARCHAR2,
          xform_list          IN OUT NOCOPY TRANSFORM_LIST,
          clip_schema_name    IN            VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| clip_table_name | VARCHAR2 | IN | Name of the transformation definition table for clipping.You can use the CREATE_CLIP Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_CLIP . To populate the table, you can use one of the INSERT procedures for clipping or you can write your own SQL. See Table 48-8 |
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| clip_schema_name | VARCHAR2 | IN | Schema of clip_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.STACK_CLIP ( clip_table_name IN VARCHAR2, xform_list IN OUT NOCOPY TRANSFORM_LIST, clip_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-36 STACK_CLIP Procedure Parameters Parameter Description clip_table_name Name of the transformation definition table for clipping.You can use the CREATE_CLIP Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_CLIP . To populate the table, you can use one of the INSERT procedures for clipping or you can write your own SQL. See Table 48-8 xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. clip_schema_name Schema of clip_table_name . If no schema is specified, the current schema is used. Usage Notes See DBMS_DATA_MINING_TRANSFORM Operational Notes . The following sections are especially relevant: “About Transformation Lists” “About Stacking” “Nested Data Transformations” Examples This example shows how a clipping transformation for the numerical column cust_credit_limit could be added to a stack called mining_data_stack . Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_postal_code, cust_credit_limit FROM sh.customers WHERE cust_id BETWEEN 100050 AND 100100; BEGIN dbms_data_mining_transform.create_clip ('clip_tbl'); dbms_data_mining_transform.insert_clip_winsor_tail ( clip_table_name => 'clip_tbl', data_table_name => 'mining_data', tail_frac => 0.25, exclude_list => dbms_data_mining_transform.COLUMN_LIST('cust_id')); END; / DECLARE MINING_DATA_STACK dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.STACK_CLIP ( clip_table_name => 'clip_tbl', xform_list => mining_data_stack); dbms_data_mining_transform.XFORM_STACK ( xform_list => mining_data_stack, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack_view'); END; / -- Before transformation SELECT cust_id, cust_postal_code, round(cust_credit_limit) FROM mining_data WHERE cust_id BETWEEN 100050 AND 100054 ORDER BY cust_id; CUST_ID CUST_POSTAL_CODE ROUND(CUST_CREDIT_LIMIT) ------- ---------------- ------------------------ 100050 76486 1500 100051 73216 9000 100052 69499 5000 100053 45704 7000 100054 88021 11000 -- After transformation SELECT cust_id, cust_postal_code, round(cust_credit_limit) FROM mining_data_stack_view WHERE cust_id BETWEEN 100050 AND 100054 ORDER BY cust_id; CUST_ID CUST_POSTAL_CODE ROUND(CUST_CREDIT_LIMIT) ------- ---------------- ------------------------ 100050 76486 5000 100051 73216 9000 100052 69499 5000 100053 45704 7000 100054 88021 11000 Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example.