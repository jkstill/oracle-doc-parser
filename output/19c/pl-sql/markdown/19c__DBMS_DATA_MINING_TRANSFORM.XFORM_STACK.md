---
id: 19c__DBMS_DATA_MINING_TRANSFORM.XFORM_STACK
name: DBMS_DATA_MINING_TRANSFORM.XFORM_STACK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.XFORM_STACK

This procedure creates a view that implements the transformations specified by the stack. Only the columns and nested attributes that are specified in the stack are transformed. Any remaining columns and nested attributes from the data table appear in the view without changes.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.XFORM_STACK (
     xform_list         IN     TRANSFORM_list,
     data_table_name    IN     VARCHAR2,
     xform_view_name    IN     VARCHAR2,
     data_schema_name   IN     VARCHAR2 DEFAULT NULL,
     xform_schema_name  IN     VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xform_list | TRANSFORM_list | IN | The transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| xform_view_name | VARCHAR2 | IN | Name of the view to be created. The view applies the transformations in xform_list to data_table_name . |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |
| xform_schema_name | VARCHAR2 | IN | Schema of xform_view_name . If no schema is specified, the current schema is used. |

## Usage Notes

To create a list of objects that describe the transformed columns, use the DESCRIBE_STACK Procedure . See Also: " Overview " Oracle Data Mining User's Guide for more information about data mining attributes See Also: " Overview " Oracle Data Mining User's Guide for more information about data mining attributes Syntax DBMS_DATA_MINING_TRANSFORM.XFORM_STACK ( xform_list IN TRANSFORM_list, data_table_name IN VARCHAR2, xform_view_name IN VARCHAR2, data_schema_name IN VARCHAR2 DEFAULT NULL, xform_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-50 XFORM_STACK Procedure Parameters Parameter Description xform_list The transformation list. See Table 48-1 for a description of the TRANSFORM_LIST object type. data_table_name Name of the table containing the data to be transformed xform_view_name Name of the view to be created. The view applies the transformations in xform_list to data_table_name . data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. xform_schema_name Schema of xform_view_name . If no schema is specified, the current schema is used. Usage Notes See " Operational Notes " . The following sections are especially relevant: " About Transformation Lists " " About Stacking " " Nested Data Transformations "