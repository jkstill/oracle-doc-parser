---
id: 19c__DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM
name: DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM

This procedure creates a transformation definition table for removing columns from the data table.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM (
      rem_table_name           VARCHAR2,
      rem_schema_name          VARCHAR2 DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| rem_table_name | VARCHAR2 | IN | Name of the transformation definition table to be created |
| rem_schema_name | VARCHAR2 | IN | Schema of rem_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

The columns are described in the following table. Syntax DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM ( rem_table_name VARCHAR2, rem_schema_name VARCHAR2 DEFAULT NULL ); Parameters Table 48-11 CREATE_COL_REM Procedure Parameters Parameter Description rem_table_name Name of the transformation definition table to be created rem_schema_name Schema of rem_table_name . If no schema is specified, the current schema is used. Usage Notes See " Nested Data Transformations " for information about transformation definition tables and nested data. See " Operational Notes " . Examples The following statement creates a table called rem_att_xtbl in the current schema. The table has columns that can be populated with the names of attributes to exclude from the data to be mined. BEGIN DBMS_DATA_MINING_TRANSFORM.CREATE_COL_REM ('rem_att_xtbl'); END; / DESCRIBE rem_att_xtbl Name Null? Type ----------------------------------------- -------- ---------------------------- COL VARCHAR2(30) ATT VARCHAR2(4000)