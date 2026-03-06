---
id: 19c__DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_CAT_MODE
name: DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_CAT_MODE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_CAT_MODE

This procedure replaces missing categorical values with the value that occurs most frequently in the column (the mode). It inserts the transformation definitions in a transformation definition table.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_CAT_MODE (
    miss_table_name    IN VARCHAR2,
    data_table_name    IN VARCHAR2,
    exclude_list       IN COLUMN_LIST DEFAULT NULL,
    miss_schema_name   IN VARCHAR2 DEFAULT NULL,
    data_schema_name   IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table for categorical missing value treatment. You can use the CREATE_MISS_CAT Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) VAL VARCHAR2(4000) CREATE_MISS_CAT creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_MISS_CAT_MODE . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| exclude_list | COLUMN_LIST | IN | List of categorical columns to be excluded from missing value treatment. If you do not specify exclude_list , all categorical columns are transformed. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

INSERT_MISS_CAT_MODE replaces missing values in all VARCHAR2 and CHAR columns in the data source unless you specify a list of columns to ignore. Syntax DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_CAT_MODE ( miss_table_name IN VARCHAR2, data_table_name IN VARCHAR2, exclude_list IN COLUMN_LIST DEFAULT NULL, miss_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-27 INSERT_MISS_CAT_MODE Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table for categorical missing value treatment. You can use the CREATE_MISS_CAT Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) VAL VARCHAR2(4000) CREATE_MISS_CAT creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_MISS_CAT_MODE . data_table_name Name of the table containing the data to be transformed exclude_list List of categorical columns to be excluded from missing value treatment. If you do not specify exclude_list , all categorical columns are transformed. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about categorical data. If you wish to replace categorical missing values with a value other than the mode, you can edit the transformation definition table. See Also: Oracle Data Mining User's Guide for information about default missing value treatment in Oracle Data Mining See Also: Oracle Data Mining User's Guide for information about default missing value treatment in Oracle Data Mining