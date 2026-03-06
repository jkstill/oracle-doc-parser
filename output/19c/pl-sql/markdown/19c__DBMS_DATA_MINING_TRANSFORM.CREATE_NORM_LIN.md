---
id: 19c__DBMS_DATA_MINING_TRANSFORM.CREATE_NORM_LIN
name: DBMS_DATA_MINING_TRANSFORM.CREATE_NORM_LIN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.CREATE_NORM_LIN

This procedure creates a transformation definition table for linear normalization.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.CREATE_NORM_LIN (
     norm_table_name       IN VARCHAR2,
     norm_schema_name      IN VARCHAR2 DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| norm_table_name | VARCHAR2 | IN | Name of the transformation definition table to be created |
| norm_schema_name | VARCHAR2 | IN | Schema of norm_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

The columns are described in Table 48-16 . Syntax DBMS_DATA_MINING_TRANSFORM.CREATE_NORM_LIN ( norm_table_name IN VARCHAR2, norm_schema_name IN VARCHAR2 DEFAULT NULL ); Parameters Table 48-17 CREATE_NORM_LIN Procedure Parameters Parameter Description norm_table_name Name of the transformation definition table to be created norm_schema_name Schema of norm_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. See " Nested Data Transformations " for information about transformation definition tables and nested data. You can use the following procedures to populate the transformation definition table: INSERT_NORM_LIN_MINMAX Procedure — Uses linear min-max normalization INSERT_NORM_LIN_SCALE Procedure — Uses linear scale normalization INSERT_NORM_LIN_ZSCORE Procedure — Uses linear zscore normalization See Also: "Linear Normalization" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes " See Also: "Linear Normalization" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes "