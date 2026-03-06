---
id: 19c__DBMS_SQL.DEFINE_ARRAY
name: DBMS_SQL.DEFINE_ARRAY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DEFINE_ARRAY

This procedure defines the collection for column into which you want to fetch rows (with a FETCH_ROWS call). This procedure lets you do batch fetching of rows from a single SELECT statement. A single fetch call brings over a number of rows into the PL/SQL aggregate object.

## Syntax

```sql
TYPE binary_double_table 
                    IS TABLE OF BINARY_DOUBLE  INDEX BY BINARY_INTEGER;
TYPE binary_float_table 
                    IS TABLE OF BINARY_FLOAT   INDEX BY BINARY_INTEGER;
TYPE bfile_table    IS TABLE OF BFILE          INDEX BY BINARY_INTEGER;
TYPE blob_table     IS TABLE OF BLOB           INDEX BY BINARY_INTEGER;
TYPE clob_table     IS TABLE OF CLOB           INDEX BY BINARY_INTEGER;
TYPE date_table     IS TABLE OF DATE           INDEX BY BINARY_INTEGER;
TYPE interval_day_to_second_Table 
                    IS TABLE OF dsinterval_unconstrained 
                                               INDEX BY BINARY_INTEGER;
TYPE interval_year_to_MONTH_Table 
                    IS TABLE OF yminterval_unconstrained 
                                               INDEX BY BINARY_INTEGER;
TYPE number_table   IS TABLE OF NUMBER         INDEX BY BINARY_INTEGER;
TYPE time_table     IS TABLE OF time_unconstrained           
                                               INDEX BY BINARY_INTEGER;
TYPE time_with_time_zone_table 
                    IS TABLE OF time_tz_unconstrained 
                                               INDEX BY BINARY_INTEGER;
TYPE timestamp_table 
                    IS TABLE OF timestamp_unconstrained   
                                               INDEX BY BINARY_INTEGER;
TYPE timestamp_with_ltz_Table 
                    IS TABLE OF timestamp_ltz_unconstrained 
                                               INDEX BY BINARY_INTEGER;
TYPE timestamp_with_time_zone_Table 
                    IS TABLE OF timestamp_tz_unconstrained 
                                               INDEX BY BINARY_INTEGER;
TYPE urowid_table   IS TABLE OF UROWID         INDEX BY BINARY_INTEGER;
TYPE varchar2_table IS TABLE OF VARCHAR2(2000) INDEX BY BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c |  |  | ID number of the cursor to which you want to bind an array. |
| position |  |  | Relative position of the column in the array being defined. The first column in a statement has position 1. |
| table_variable |  |  | Local variable that has been declared as < datatype >. |
| cnt |  |  | Number of rows that must be fetched. |
| lower_bnd |  |  | Results are copied into the collection, starting at this lower bound index. |

## Usage Notes

When you fetch the rows, they are copied into DBMS_SQL buffers until you run a COLUMN_VALUE call, at which time the rows are copied into the table that was passed as an argument to the COLUMN_VALUE call. Scalar and LOB Types for Collections You can declare a local variable as one of the following table-item types, and then fetch any number of rows into it using DBMS_SQL . (These are the same types as you can specify for the BIND_ARRAY procedure.) TYPE binary_double_table IS TABLE OF BINARY_DOUBLE INDEX BY BINARY_INTEGER; TYPE binary_float_table IS TABLE OF BINARY_FLOAT INDEX BY BINARY_INTEGER; TYPE bfile_table IS TABLE OF BFILE INDEX BY BINARY_INTEGER; TYPE blob_table IS TABLE OF BLOB INDEX BY BINARY_INTEGER; TYPE clob_table IS TABLE OF CLOB INDEX BY BINARY_INTEGER; TYPE date_table IS TABLE OF DATE INDEX BY BINARY_INTEGER; TYPE interval_day_to_second_Table IS TABLE OF dsinterval_unconstrained INDEX BY BINARY_INTEGER; TYPE interval_year_to_MONTH_Table IS TABLE OF yminterval_unconstrained INDEX BY BINARY_INTEGER; TYPE number_table IS TABLE OF NUMBER INDEX BY BINARY_INTEGER; TYPE time_table IS TABLE OF time_unconstrained INDEX BY BINARY_INTEGER; TYPE time_with_time_zone_table IS TABLE OF time_tz_unconstrained INDEX BY BINARY_INTEGER; TYPE timestamp_table IS TABLE OF timestamp_unconstrained INDEX BY BINARY_INTEGER; TYPE timestamp_with_ltz_Table IS TABLE OF timestamp_ltz_unconstrained INDEX BY BINARY_INTEGER; TYPE timestamp_with_time_zone_Table IS TABLE OF timestamp_tz_unconstrained INDEX BY BINARY_INTEGER; TYPE urowid_table IS TABLE OF UROWID INDEX BY BINARY_INTEGER; TYPE varchar2_table IS TABLE OF VARCHAR2(2000) INDEX BY BINARY_INTEGER; Syntax DBMS_SQL.DEFINE_ARRAY ( c IN INTEGER, position IN INTEGER, <table_variable> IN <datatype> cnt IN INTEGER, lower_bnd IN INTEGER); Where < table_variable > and its corresponding <datatype> can be any one of the following matching pairs, DEFINE_ARRAY being overloaded to accept different datatypes: <clob_tab> Clob_Table <bflt_tab> Binary_Float_Table <bdbl_tab> Binary_Double_Table <blob_tab> Blob_Table <bfile_tab> Bfile_Table <date_tab> Date_Table <num_tab> Number_Table <urowid_tab> Urowid_Table <vchr2_tab> Varchar2_Table <tm_tab> Time_Table <ttz_tab> Time_With_Time_Zone_Table <tms_tab> Timestamp_Table <tstz_tab> Timestamp_With_ltz_Table <tstz_tab> Timestamp_With_Time_Zone_Table <ids_tab> Interval_Day_To_Second_Table <iym_tab> Interval_Year_To_Month_Table Pragmas pragma restrict_references(define_array,RNDS,WNDS); The subsequent FETCH_ROWS call fetch "count" rows. When the COLUMN_VALUE call is made, these rows are placed in positions lower_bnd , lower_bnd +1, lower_bnd +2, and so on. While there are still rows coming, the user keeps issuing FETCH_ROWS / COLUMN_VALUE calls. The rows keep accumulating in the table specified as an argument in the COLUMN_VALUE call. Parameters Table 162-14 DEFINE_ARRAY Procedure Parameters Parameter Description c ID number of the cursor to which you want to bind an array. position Relative position of the column in the array being defined. The first column in a statement has position 1. table_variable Local variable that has been declared as < datatype >. cnt Number of rows that must be fetched. lower_bnd Results are copied into the collection, starting at this lower bound index.