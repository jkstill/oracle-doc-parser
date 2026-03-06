---
id: 19c__DBMS_DATA_MINING_TRANSFORM.STACK_COL_REM
name: DBMS_DATA_MINING_TRANSFORM.STACK_COL_REM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.STACK_COL_REM

This procedure adds column removal transformations to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.STACK_COL_REM (
     rem_table_name     IN            VARCHAR2,
     xform_list         IN OUT NOCOPY TRANSFORM_LIST,
     rem_schema_name    IN            VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rem_table_name | VARCHAR2 | IN | Name of the transformation definition table for column removal. You can use the CREATE_COL_REM Procedure to create the definition table. See Table 48-10 . The table must be populated with column names before you call STACK_COL_REM . The INSERT_BIN_SUPER Procedure and the INSERT_AUTOBIN_NUM_EQWIDTH Procedure can optionally be used to populate the table. You can also use SQL INSERT statements. |
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| rem_schema_name | VARCHAR2 | IN | Schema of rem_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.STACK_COL_REM ( rem_table_name IN VARCHAR2, xform_list IN OUT NOCOPY TRANSFORM_LIST, rem_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-37 STACK_COL_REM Procedure Parameters Parameter Description rem_table_name Name of the transformation definition table for column removal. You can use the CREATE_COL_REM Procedure to create the definition table. See Table 48-10 . The table must be populated with column names before you call STACK_COL_REM . The INSERT_BIN_SUPER Procedure and the INSERT_AUTOBIN_NUM_EQWIDTH Procedure can optionally be used to populate the table. You can also use SQL INSERT statements. xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. rem_schema_name Schema of rem_table_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . The following sections are especially relevant: " About Transformation Lists " " About Stacking " " Nested Data Transformations " Examples This example shows how the column cust_credit_limit could be removed in a transformation list called mining_data_stack . Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, country_id, cust_postal_code, cust_credit_limit FROM sh.customers; BEGIN dbms_data_mining_transform.create_col_rem ('rem_tbl'); END; / INSERT into rem_tbl VALUES (upper('cust_postal_code'), null); DECLARE MINING_DATA_STACK dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.stack_col_rem ( rem_table_name => 'rem_tbl', xform_list => mining_data_stack); dbms_data_mining_transform.XFORM_STACK ( xform_list => mining_data_stack, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack_view'); END; / SELECT * FROM mining_data WHERE cust_id BETWEEN 100050 AND 100051 ORDER BY cust_id; CUST_ID COUNTRY_ID CUST_POSTAL_CODE CUST_CREDIT_LIMIT ------- ---------- ---------------- ----------------- 100050 52773 76486 1500 100051 52790 73216 9000 SELECT * FROM mining_data_stack_view WHERE cust_id BETWEEN 100050 AND 100051 ORDER BY cust_id; CUST_ID COUNTRY_ID CUST_CREDIT_LIMIT ------- ---------- ----------------- 100050 52773 1500 100051 52790 9000 Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example.