---
id: 19c__DBMS_DATA_MINING_TRANSFORM.STACK_BIN_NUM
name: DBMS_DATA_MINING_TRANSFORM.STACK_BIN_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.STACK_BIN_NUM

This procedure adds numerical binning transformations to a transformation list.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.STACK_BIN_NUM (
     bin_table_name     IN             VARCHAR2,
     xform_list         IN OUT  NOCOPY TRANSFORM_LIST,
     literal_flag       IN             BOOLEAN  DEFAULT FALSE,
     bin_schema_name    IN             VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bin_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical binning. You can use the CREATE_BIN_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_BIN_NUM . To populate the table, you can use one of the INSERT procedures for numerical binning or you can write your own SQL. See Table 48-6 . |
| xform_list | NOCOPY | IN OUT | A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| literal_flag | BOOLEAN | IN | Indicates whether the values in the bin column in the transformation definition table are valid SQL literals. When literal_flag is FALSE (the default), the bin identifiers will be transformed to SQL literals by surrounding them with single quotes. Set literal_flag to TRUE if the bin identifiers are numbers that should have a numeric datatype, as is the case for an O-Cluster model. See " INSERT_BIN_NUM_EQWIDTH Procedure " for an example. |
| bin_schema_name | VARCHAR2 | IN | Schema of bin_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.STACK_BIN_NUM ( bin_table_name IN VARCHAR2, xform_list IN OUT NOCOPY TRANSFORM_LIST, literal_flag IN BOOLEAN DEFAULT FALSE, bin_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-35 STACK_BIN_NUM Procedure Parameters Parameter Description bin_table_name Name of the transformation definition table for numerical binning. You can use the CREATE_BIN_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call STACK_BIN_NUM . To populate the table, you can use one of the INSERT procedures for numerical binning or you can write your own SQL. See Table 48-6 . xform_list A transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. literal_flag Indicates whether the values in the bin column in the transformation definition table are valid SQL literals. When literal_flag is FALSE (the default), the bin identifiers will be transformed to SQL literals by surrounding them with single quotes. Set literal_flag to TRUE if the bin identifiers are numbers that should have a numeric datatype, as is the case for an O-Cluster model. See " INSERT_BIN_NUM_EQWIDTH Procedure " for an example. bin_schema_name Schema of bin_table_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . The following sections are especially relevant: " About Transformation Lists " " About Stacking " " Nested Data Transformations " Examples This example shows how a binning transformation for the numerical column cust_credit_limit could be added to a stack called mining_data_stack . Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_postal_code, cust_credit_limit FROM sh.customers WHERE cust_id BETWEEN 100050 and 100100; BEGIN dbms_data_mining_transform.create_bin_num ('bin_num_tbl'); dbms_data_mining_transform.insert_bin_num_qtile ( bin_table_name => 'bin_num_tbl', data_table_name => 'mining_data', bin_num => 5, exclude_list => dbms_data_mining_transform.COLUMN_LIST('cust_id')); END; / DECLARE MINING_DATA_STACK dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.STACK_BIN_CAT ( bin_table_name => 'bin_num_tbl', xform_list => mining_data_stack); dbms_data_mining_transform.XFORM_STACK ( xform_list => mining_data_stack, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack_view'); END; / -- Before transformation SELECT cust_id, cust_postal_code, ROUND(cust_credit_limit) FROM mining_data WHERE cust_id BETWEEN 100050 AND 100055 ORDER BY cust_id; CUST_ID CUST_POSTAL_CODE ROUND(CUST_CREDIT_LIMIT) ------- ----------------- ------------------------- 100050 76486 1500 100051 73216 9000 100052 69499 5000 100053 45704 7000 100055 74673 11000 100055 74673 11000 -- After transformation SELECT cust_id, cust_postal_code, ROUND(cust_credit_limit) FROM mining_data_stack_view WHERE cust_id BETWEEN 100050 AND 100055 ORDER BY cust_id; CUST_ID CUST_POSTAL_CODE ROUND(CUST_CREDIT_LIMITT) ------- ---------------- ------------------------- 100050 76486 100051 73216 2 100052 69499 1 100053 45704 100054 88021 3 100055 74673 3 Note: This example invokes the XFORM_STACK Procedure to show how the data is transformed by the stack. XFORM_STACK simply generates an external view of the transformed data. The actual purpose of the STACK procedures is to assemble a list of transformations for embedding in a model. The transformations are passed to CREATE_MODEL in the xform_list parameter. See INSERT_BIN_NUM_EQWIDTH Procedure for an example.