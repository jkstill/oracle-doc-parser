---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_NUM
name: DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_NUM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_NUM

This procedure creates a view that implements the numerical missing value treatment transformations specified in a definition table. Only the columns that are specified in the definition table are transformed; the remaining columns from the data table are present in the view, but they are not changed.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_NUM (
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
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical missing value treatment. You can use the CREATE_MISS_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_MISS_NUM . To populate the table, you can use the INSERT_MISS_NUM_MEAN Procedure or you can write your own SQL. See Table 48-14 . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view presents columns in data_table_name with the transformations specified in miss_table_name . |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_NUM ( miss_table_name IN VARCHAR2, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, miss_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL; Parameters Table 48-48 XFORM_MISS_NUM Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table for numerical missing value treatment. You can use the CREATE_MISS_NUM Procedure to create the definition table. The table must be populated with transformation definitions before you call XFORM_MISS_NUM . To populate the table, you can use the INSERT_MISS_NUM_MEAN Procedure or you can write your own SQL. See Table 48-14 . data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view presents columns in data_table_name with the transformations specified in miss_table_name . miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . Examples This example creates a view that replaces missing numerical values with the mean. SELECT * FROM items; ITEM_ID QTY ---------- ------ aa 200 bb 200 cc 250 dd ee ff 100 gg 250 hh 200 ii jj 200 SELECT AVG(qty) FROM items; AVG(QTY) -------- 200 BEGIN DBMS_DATA_MINING_TRANSFORM.CREATE_MISS_NUM('missnum_xtbl'); DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_NUM_MEAN ( miss_table_name => 'missnum_xtbl', data_table_name => 'items' ); END; / SELECT col, val FROM missnum_xtbl; COL VAL ---------- ------ QTY 200 BEGIN DBMS_DATA_MINING_TRANSFORM.XFORM_MISS_NUM ( miss_table_name => 'missnum_xtbl', data_table_name => 'items', xform_view_name => 'items_view'); END; / SELECT * FROM items_view; ITEM_ID QTY ---------- ------ aa 200 bb 200 cc 250 dd 200 ee 200 ff 100 gg 250 hh 200 ii 200 jj 200