---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_CAT
name: DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_CAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_CAT

This procedure creates a view that implements the categorical missing value treatment transformations specified in a definition table. Only the columns that are specified in the definition table are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_CAT (
    miss_table_name       IN VARCHAR2, 
    data_table_name       IN VARCHAR2,
    xform_view_name       IN VARCHAR2,
    miss_schema_name      IN VARCHAR2 DEFAULT NULL,
    data_schema_name      IN VARCHAR2 DEFAULT NULL,
    xform_schema_name     IN VARCHAR2 DEFAULT NULL;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table for categorical missing value treatment. You can use the CREATE_MISS_CAT Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_MISS_CAT . To populate the table, you can use the INSERT_MISS_CAT_MODE Procedure or you can write your own SQL. See Table 48-12 . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in miss_table_name . |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_CAT ( miss_table_name IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, miss_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL; Parameters Table 48-47 XFORM_MISS_CAT Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table for categorical missing value treatment. You can use the CREATE_MISS_CAT Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_MISS_CAT . To populate the table, you can use the INSERT_MISS_CAT_MODE Procedure or you can write your own SQL. See Table 48-12 . data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in miss_table_name . miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . Examples This example creates a view that replaces missing categorical values with the mode. SELECT * FROM geog; REG_ID REGION ------ ------------------------------ 1 NE 2 SW 3 SE 4 SW 5 6 NE 7 NW 8 NW 9 10 11 SE 12 SE 13 NW 14 SE 15 SE SELECT STATS_MODE(region) FROM geog; STATS_MODE(REGION) ------------------------------ SE BEGIN DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_CAT('misscat_xtbl'); DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_CAT_MODE ( miss_table_name => 'misscat_xtbl', data_table_name => 'geog' ); END; / SELECT col, val FROM misscat_xtbl; COL VAL ---------- ---------- REGION SE BEGIN DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_CAT ( miss_table_name => 'misscat_xtbl', data_table_name => 'geog', xform_view_name => 'geogxf_view'); END; / SELECT * FROM geogxf_view; REG_ID REGION ------ ------------------------------ 1 NE 2 SW 3 SE 4 SW 5 SE 6 NE 7 NW 8 NW 9 SE 10 SE 11 SE 12 SE 13 NW 14 SE 15 SE