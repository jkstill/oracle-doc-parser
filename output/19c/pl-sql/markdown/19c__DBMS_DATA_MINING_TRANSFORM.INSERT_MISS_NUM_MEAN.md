---
id: 19c__DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_NUM_MEAN
name: DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_NUM_MEAN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_NUM_MEAN

This procedure replaces missing numerical values with the average (the mean) and inserts the transformation definitions in a transformation definition table.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_NUM_MEAN (
    miss_table_name    IN VARCHAR2,
    data_table_name    IN VARCHAR2,
    exclude_list       IN COLUMN_LIST DEFAULT NULL,
    round_num          IN PLS_INTEGER DEFAULT 6,
    miss_schema_name   IN VARCHAR2 DEFAULT NULL,
    data_schema_name   IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| miss_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical missing value treatment. You can use the CREATE_MISS_NUM Procedure to create the definition table. The following columns are required by INSERT_MISS_NUM_MEAN : COL VARCHAR2(30) VAL NUMBER CREATE_MISS_NUM creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_MISS_NUM_MEAN . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| exclude_list | COLUMN_LIST | IN | List of numerical columns to be excluded from missing value treatment. If you do not specify exclude_list , all numerical columns are transformed. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| round_num | PLS_INTEGER | IN | The number of significant digits to use for the mean. The default number is 6. |
| miss_schema_name | VARCHAR2 | IN | Schema of miss_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

INSERT_MISS_NUM_MEAN replaces missing values in all NUMBER and FLOAT columns in the data source unless you specify a list of columns to ignore. Syntax DBMS_DATA_MINING_TRANSFORM.INSERT_MISS_NUM_MEAN ( miss_table_name IN VARCHAR2, data_table_name IN VARCHAR2, exclude_list IN COLUMN_LIST DEFAULT NULL, round_num IN PLS_INTEGER DEFAULT 6, miss_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-28 INSERT_MISS_NUM_MEAN Procedure Parameters Parameter Description miss_table_name Name of the transformation definition table for numerical missing value treatment. You can use the CREATE_MISS_NUM Procedure to create the definition table. The following columns are required by INSERT_MISS_NUM_MEAN : COL VARCHAR2(30) VAL NUMBER CREATE_MISS_NUM creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_MISS_NUM_MEAN . data_table_name Name of the table containing the data to be transformed exclude_list List of numerical columns to be excluded from missing value treatment. If you do not specify exclude_list , all numerical columns are transformed. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') round_num The number of significant digits to use for the mean. The default number is 6. miss_schema_name Schema of miss_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. If you wish to replace numerical missing values with a value other than the mean, you can edit the transformation definition table. See Also: Oracle Data Mining User's Guide for information about default missing value treatment in Oracle Data Mining See Also: Oracle Data Mining User's Guide for information about default missing value treatment in Oracle Data Mining