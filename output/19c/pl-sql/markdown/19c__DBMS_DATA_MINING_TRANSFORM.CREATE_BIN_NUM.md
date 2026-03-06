---
id: 19c__DBMS_DATA_MINING_TRANSFORM.CREATE_BIN_NUM
name: DBMS_DATA_MINING_TRANSFORM.CREATE_BIN_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.CREATE_BIN_NUM

This procedure creates a transformation definition table for numerical binning.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.CREATE_BIN_NUM (
     bin_table_name    IN VARCHAR2,
     bin_schema_name   IN VARCHAR2 DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bin_table_name | VARCHAR2 | IN | Name of the transformation definition table to be created |
| bin_schema_name | VARCHAR2 | IN | Schema of bin_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

The columns are described in the following table. Syntax DBMS_DATA_MINING_TRANSFORM.CREATE_BIN_NUM ( bin_table_name IN VARCHAR2, bin_schema_name IN VARCHAR2 DEFAULT NULL ); Parameters Table 48-7 CREATE_BIN_NUM Procedure Parameters Parameter Description bin_table_name Name of the transformation definition table to be created bin_schema_name Schema of bin_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. See " Nested Data Transformations " for information about transformation definition tables and nested data. You can use the following procedures to populate the transformation definition table: INSERT_AUTOBIN_NUM_EQWIDTH Procedure — automatic equi-width binning INSERT_BIN_NUM_EQWIDTH Procedure — user-specified equi-width binning INSERT_BIN_NUM_QTILE Procedure — quantile binning INSERT_BIN_SUPER Procedure — supervised binning See Also: "Binning" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes " See Also: "Binning" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes "