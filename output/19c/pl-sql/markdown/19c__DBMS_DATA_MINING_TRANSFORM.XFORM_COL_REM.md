---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_COL_REM
name: DBMS_DATA_MINING_TRANSFORM.XFORM_COL_REM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_COL_REM

This procedure creates a view that implements the column removal transformations specified in a definition table. Only the columns that are specified in the definition table are removed; the remaining columns from the data table are present in the view.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_COL_REM (
     rem_table_name     IN       VARCHAR2,
     data_table_name    IN       VARCHAR2,
     xform_view_name    IN       VARCHAR2,
     rem_schema_name    IN       VARCHAR2 DEFAULT NULL,
     data_schema_name   IN       VARCHAR2 DEFAULT NULL,
     xform_schema_name  IN       VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rem_table_name | VARCHAR2 | IN | Name of the transformation definition table for column removal. You can use the CREATE_COL_REM Procedure to create the definition table. See Table 48-10 . The table must be populated with column names before you call XFORM_COL_REM . The INSERT_BIN_SUPER Procedure and the INSERT_AUTOBIN_NUM_EQWIDTH Procedure can optionally be used to populate the table. You can also use SQL INSERT statements. |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents the columns in data_table_name that are not specified in rem_table_name . |
| rem_schema_name | VARCHAR2 | IN | Schema of rem_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_COL_REM ( rem_table_name IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, rem_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-44 XFORM_COL_REM Procedure Parameters Parameter Description rem_table_name Name of the transformation definition table for column removal. You can use the CREATE_COL_REM Procedure to create the definition table. See Table 48-10 . The table must be populated with column names before you call XFORM_COL_REM . The INSERT_BIN_SUPER Procedure and the INSERT_AUTOBIN_NUM_EQWIDTH Procedure can optionally be used to populate the table. You can also use SQL INSERT statements. data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents the columns in data_table_name that are not specified in rem_table_name . rem_schema_name Schema of rem_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . Examples This example creates a view that includes all but one column from the table customers in the current schema. describe customers Name Null? Type ----------------------------------------- -------- ---------------------------- CUST_ID NOT NULL NUMBER CUST_MARITAL_STATUS VARCHAR2(20) OCCUPATION VARCHAR2(21) AGE NUMBER YRS_RESIDENCE NUMBER BEGIN DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM ('colrem_xtbl'); END; / INSERT INTO colrem_xtbl VALUES('CUST_MARITAL_STATUS', null); NOTE: This currently doesn't work. See bug 9310319 BEGIN DBMS_DATA_MINING_TRANSFORM.XFORM_COL_REM ( rem_table_name => 'colrem_xtbl', data_table_name => 'customers', xform_view_name => 'colrem_view'); END; / describe colrem_view Name Null? Type ----------------------------------------- -------- ---------------------------- CUST_ID NOT NULL NUMBER OCCUPATION VARCHAR2(21) AGE NUMBER YRS_RESIDENCE NUMBER