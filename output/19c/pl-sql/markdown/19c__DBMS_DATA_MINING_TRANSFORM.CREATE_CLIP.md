---
id: 19c__DBMS_DATA_MINING_TRANSFORM.CREATE_CLIP
name: DBMS_DATA_MINING_TRANSFORM.CREATE_CLIP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.CREATE_CLIP

This procedure creates a transformation definition table for clipping or winsorizing to minimize the effect of outliers.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.CREATE_CLIP (
     clip_table_name    IN VARCHAR2,
     clip_schema_name   IN VARCHAR2 DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| clip_table_name | VARCHAR2 | IN | Name of the transformation definition table to be created |
| clip_schema_name | VARCHAR2 | IN | Schema of clip_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

The columns are described in the following table. Syntax DBMS_DATA_MINING_TRANSFORM.CREATE_CLIP ( clip_table_name IN VARCHAR2, clip_schema_name IN VARCHAR2 DEFAULT NULL ); Parameters Table 48-9 CREATE_CLIP Procedure Parameters Parameter Description clip_table_name Name of the transformation definition table to be created clip_schema_name Schema of clip_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. See " Nested Data Transformations " for information about transformation definition tables and nested data. You can use the following procedures to populate the transformation definition table: INSERT_CLIP_TRIM_TAIL Procedure — replaces outliers with nulls INSERT_CLIP_WINSOR_TAIL Procedure — replaces outliers with an average value See Also: "Outlier Treatment" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes " See Also: "Outlier Treatment" in DBMS_DATA_MINING_TRANSFORM Overview " Operational Notes "