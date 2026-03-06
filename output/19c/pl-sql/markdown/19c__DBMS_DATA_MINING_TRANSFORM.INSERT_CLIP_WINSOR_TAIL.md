---
id: 19c__DBMS_DATA_MINING_TRANSFORM.INSERT_CLIP_WINSOR_TAIL
name: DBMS_DATA_MINING_TRANSFORM.INSERT_CLIP_WINSOR_TAIL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATA_MINING_TRANSFORM
tags: [dbms_data_mining_transform]
source_file: DBMS_DATA_MINING_TRANSFORM.html
---

# DBMS_DATA_MINING_TRANSFORM.INSERT_CLIP_WINSOR_TAIL

This procedure replaces numeric outliers with the upper or lower boundary values. It inserts the transformation definitions in a transformation definition table.

## Syntax

```sql
DBMS_DATA_MINING_TRANSFORM.INSERT_CLIP_WINSOR_TAIL (
    clip_table_name    IN VARCHAR2,
    data_table_name    IN VARCHAR2,
    tail_frac          IN NUMBER DEFAULT 0.025,
    exclude_list       IN COLUMN_LIST DEFAULT NULL,
    clip_schema_name   IN VARCHAR2 DEFAULT NULL,
    data_schema_name   IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| clip_table_name | VARCHAR2 | IN | Name of the transformation definition table for numerical clipping. You can use the CREATE_CLIP Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) LCUT NUMBER LVAL NUMBER RCUT NUMBER RVAL NUMBER CREATE_CLIP creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_CLIP_WINSOR_TAIL . |
| data_table_name | VARCHAR2 | IN | Name of the table containing the data to be transformed |
| tail_frac | NUMBER | IN | The percentage of non-null values to be designated as outliers at each end of the data. For example, if tail_frac is .01, then 1% of the data at the low end and 1% of the data at the high end will be treated as outliers. If tail_frac is greater than or equal to .5, no clipping occurs. The default value of tail_frac is 0.025. |
| exclude_list | COLUMN_LIST | IN | List of numerical columns to be excluded from the clipping process. If you do not specify exclude_list , all numerical columns in the data are clipped. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') |
| clip_schema_name | VARCHAR2 | IN | Schema of clip_table_name . If no schema is specified, the current schema is used. |
| data_schema_name | VARCHAR2 | IN | Schema of data_table_name . If no schema is specified, the current schema is used. |

## Usage Notes

INSERT_CLIP_WINSOR_TAIL computes the boundaries of the data based on a specified percentage. It replaces the values that fall outside the boundaries (tail values) with the related boundary value. If you wish to set tail values to null, use the INSERT_CLIP_TRIM_TAIL Procedure . INSERT_CLIP_WINSOR_TAIL clips all the NUMBER and FLOAT columns in the data source unless you specify a list of columns to ignore. Syntax DBMS_DATA_MINING_TRANSFORM.INSERT_CLIP_WINSOR_TAIL ( clip_table_name IN VARCHAR2, data_table_name IN VARCHAR2, tail_frac IN NUMBER DEFAULT 0.025, exclude_list IN COLUMN_LIST DEFAULT NULL, clip_schema_name IN VARCHAR2 DEFAULT NULL, data_schema_name IN VARCHAR2 DEFAULT NULL); Parameters Table 48-26 INSERT_CLIP_WINSOR_TAIL Procedure Parameters Parameter Description clip_table_name Name of the transformation definition table for numerical clipping. You can use the CREATE_CLIP Procedure to create the definition table. The following columns are required: COL VARCHAR2(30) LCUT NUMBER LVAL NUMBER RCUT NUMBER RVAL NUMBER CREATE_CLIP creates an additional column, ATT , which may be used for specifying nested attributes. This column is not used by INSERT_CLIP_WINSOR_TAIL . data_table_name Name of the table containing the data to be transformed tail_frac The percentage of non-null values to be designated as outliers at each end of the data. For example, if tail_frac is .01, then 1% of the data at the low end and 1% of the data at the high end will be treated as outliers. If tail_frac is greater than or equal to .5, no clipping occurs. The default value of tail_frac is 0.025. exclude_list List of numerical columns to be excluded from the clipping process. If you do not specify exclude_list , all numerical columns in the data are clipped. The format of exclude_list is: dbms_data_mining_transform.COLUMN_LIST('col 1 ','col 2 ', ...'col n ') clip_schema_name Schema of clip_table_name . If no schema is specified, the current schema is used. data_schema_name Schema of data_table_name . If no schema is specified, the current schema is used. Usage Notes See Oracle Data Mining User's Guide for details about numerical data. The DBMS_DATA_MINING_TRANSFORM package provides two clipping procedures: INSERT_CLIP_WINSOR_TAIL and INSERT_CLIP_TRIM_TAIL . Both procedures compute the boundaries as follows: Count the number of non-null values, n , and sort them in ascending order Calculate the number of outliers, t , as n*tail_frac Define the lower boundary lcut as the value at position 1+ floor (t) Define the upper boundary rcut as the value at position n- floor (t) (The SQL FLOOR function returns the largest integer less than or equal to t .) All values that are <= lcut or => rcut are designated as outliers. INSERT_CLIP_WINSOR_TAIL assigns lcut to the low outliers and rcut to the high outliers. INSERT_CLIP_TRIM_TAIL replaces the outliers with nulls, effectively removing them from the data. Examples In this example, INSERT_CLIP_WINSOR_TAIL winsorizes 10% of the data in two columns (5% from the high end, and 5% from the low end) and inserts the transformations in a transformation definition table. The STACK_CLIP Procedure creates a transformation list from the contents of the definition table. The SQL expression that computes the transformation is shown in the view MINING_DATA_STACK . The view is for display purposes only; it cannot be used to embed the transformations in a model. CREATE OR REPLACE VIEW mining_data AS SELECT cust_id, cust_year_of_birth, cust_credit_limit, cust_city FROM sh.customers; describe mining_data Name Null? Type ---------------------------------------- -------- ------------- CUST_ID NOT NULL NUMBER CUST_YEAR_OF_BIRTH NOT NULL NUMBER(4) CUST_CREDIT_LIMIT NUMBER CUST_CITY NOT NULL VARCHAR2(30) BEGIN dbms_data_mining_transform.CREATE_CLIP( clip_table_name => 'clip_tbl'); dbms_data_mining_transform.INSERT_CLIP_WINSOR_TAIL( clip_table_name => 'clip_tbl', data_table_name => 'mining_data', tail_frac => 0.05, exclude_list => DBMS_DATA_MINING_TRANSFORM.COLUMN_LIST('cust_id')); END; / SELECT col, lcut, lval, rcut, rval FROM clip_tbl ORDER BY col ASC; COL LCUT LVAL RCUT RVAL ------------------------------ -------- -------- -------- -------- CUST_CREDIT_LIMIT 1500 1500 11000 11000 CUST_YEAR_OF_BIRTH 1934 1934 1982 1982 DECLARE xforms dbms_data_mining_transform.TRANSFORM_LIST; BEGIN dbms_data_mining_transform.STACK_CLIP ( clip_table_name => 'clip_tbl', xform_list => xforms); dbms_data_mining_transform.XFORM_STACK ( xform_list => xforms, data_table_name => 'mining_data', xform_view_name => 'mining_data_stack'); END; / set long 3000 SQL> SELECT text FROM user_views WHERE view_name IN 'MINING_DATA_STACK'; TEXT -------------------------------------------------------------------------------- SELECT "CUST_ID",CASE WHEN "CUST_YEAR_OF_BIRTH" < 1934 THEN 1934 WHEN "CUST_YEAR _OF_BIRTH" > 1982 THEN 1982 ELSE "CUST_YEAR_OF_BIRTH" END "CUST_YEAR_OF_BIRTH",C ASE WHEN "CUST_CREDIT_LIMIT" < 1500 THEN 1500 WHEN "CUST_CREDIT_LIMIT" > 11000 T HEN 11000 ELSE "CUST_CREDIT_LIMIT" END "CUST_CREDIT_LIMIT","CUST_CITY" FROM mini ng_data