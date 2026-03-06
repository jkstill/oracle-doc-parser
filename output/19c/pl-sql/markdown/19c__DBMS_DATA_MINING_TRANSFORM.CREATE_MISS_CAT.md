---
id: 19c__DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_CAT
name: DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_CAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_CAT

This procedure creates a transformation definition table for replacing categorical missing values.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_CAT (
     miss_table_name       IN VARCHAR2,
     miss_schema_name      IN VARCHAR2 DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table to be created |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

The columns are described in the following table. Syntax DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_CAT ( miss_table_name IN VARCHAR2, miss_schema_name IN VARCHAR2 DEFAULT NULL ); Parameters Table 48-13 CREATE_MISS_CAT Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table to be created miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about categorical data. See " Nested Data Transformations " for information about transformation definition tables and nested data. You can use the INSERT_MISS_CAT_MODE Procedure to populate the transformation definition table. See Also: "Missing Value Treatment" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes " See Also: "Missing Value Treatment" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes "