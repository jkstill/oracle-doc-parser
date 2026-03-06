---
id: 19c__DBMS_SQL.BIND_ARRAY
name: DBMS_SQL.BIND_ARRAY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.BIND_ARRAY

This procedure binds a given value or set of values to a given variable in a cursor, based on the name of the variable in the statement.

## Syntax

```sql
DBMS_SQL.BIND_ARRAY ( 
   c                   IN INTEGER, 
   name                IN VARCHAR2, 
   <table_variable>    IN <datatype> 
 [,index1              IN INTEGER, 
   index2              IN INTEGER)] );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor to which you want to bind a value. |
| name | VARCHAR2 | IN | Name of the collection in the statement. |
| table_variable |  |  | Local variable that has been declared as < datatype >. |
| index1 | INTEGER | IN | Index for the table element that marks the lower bound of the range. |
| index2 | INTEGER) | IN | Index for the table element that marks the upper bound of the range. |

## Usage Notes

Syntax DBMS_SQL.BIND_ARRAY ( c IN INTEGER, name IN VARCHAR2, <table_variable> IN <datatype> [,index1 IN INTEGER, index2 IN INTEGER)] ); Where the < table_variable > and its corresponding < datatype > can be any one of the following matching pairs: <clob_tab> Clob_Table <bflt_tab> Binary_Float_Table <bdbl_tab> Binary_Double_Table <blob_tab> Blob_Table <bfile_tab> Bfile_Table <date_tab> Date_Table <num_tab> Number_Table <urowid_tab> Urowid_Table <vchr2_tab> Varchar2_Table <tm_tab> Time_Table <ttz_tab> Time_With_Time_Zone_Table <tms_tab> Timestamp_Table <tstz_tab> Timestamp_With_ltz_Table <tstz_tab> Timestamp_With_Time_Zone_Table <ids_tab> Interval_Day_To_Second_Table <iym_tab> Interval_Year_To_Month_Table Notice that the BIND_ARRAY procedure is overloaded to accept different datatype. Parameters Table 162-7 BIND_ARRAY Procedure Parameters Parameter Description c ID number of the cursor to which you want to bind a value. name Name of the collection in the statement. table_variable Local variable that has been declared as < datatype >. index1 Index for the table element that marks the lower bound of the range. index2 Index for the table element that marks the upper bound of the range. Usage Notes For binding a range, the table must contain the elements that specify the range — tab(index1) and tab(index2) — but the range does not have to be dense. Index1 must be less than or equal to index2. All elements between tab(index1) and tab(index2) are used in the bind. If you do not specify indexes in the bind call, and two different binds in a statement specify tables that contain a different number of elements, then the number of elements actually used is the minimum number between all tables. This is also the case if you specify indexes — the minimum range is selected between the two indexes for all tables. Not all bind variables in a query have to be array binds. Some can be regular binds and the same value are used for each element of the collections in expression evaluations (and so forth). Bulk Array Binds Bulk selects, inserts, updates, and deletes can enhance the performance of applications by bundling many calls into one. The DBMS_SQL package lets you work on collections of data using the PL/SQL table type. Table items are unbounded homogeneous collections. In persistent storage, they are like other relational tables and have no intrinsic ordering. But when a table item is brought into the workspace (either by querying or by navigational access of persistent data), or when it is created as the value of a PL/SQL variable or parameter, its elements are given subscripts that can be used with array-style syntax to get and set the values of elements. The subscripts of these elements need not be dense, and can be any number including negative numbers. For example, a table item can contain elements at locations -10, 2, and 7 only. When a table item is moved from transient workspace to persistent storage, the subscripts are not stored; the table item is unordered in persistent storage. At bind time the table is copied out from the PL/SQL buffers into local DBMS_SQL buffers (the same as for all scalar types) and then the table is manipulated from the local DBMS_SQL buffers. Therefore, if you change the table after the bind call, then that change does not affect the way the execute acts. Types for Scalar and LOB Collections You can declare a local variable as one of the following table-item types, which are defined as public types in DBMS_SQL . TYPE binary_double_table IS TABLE OF BINARY_DOUBLE INDEX BY BINARY_INTEGER; TYPE binary_float_table IS TABLE OF BINARY_FLOAT INDEX BY BINARY_INTEGER; TYPE bfile_table IS TABLE OF BFILE INDEX BY BINARY_INTEGER; TYPE blob_table IS TABLE OF BLOB INDEX BY BINARY_INTEGER; TYPE clob_table IS TABLE OF CLOB INDEX BY BINARY_INTEGER; TYPE date_table IS TABLE OF DATE INDEX BY BINARY_INTEGER; TYPE interval_day_to_second_Table IS TABLE OF dsinterval_unconstrained INDEX BY BINARY_INTEGER; TYPE interval_year_to_MONTH_Table IS TABLE OF yminterval_unconstrained INDEX BY BINARY_INTEGER; TYPE number_table IS TABLE OF NUMBER INDEX BY BINARY_INTEGER; TYPE time_table IS TABLE OF time_unconstrained INDEX BY BINARY_INTEGER; TYPE time_with_time_zone_table IS TABLE OF time_tz_unconstrained INDEX BY BINARY_INTEGER; TYPE timestamp_table IS TABLE OF timestamp_unconstrained INDEX BY BINARY_INTEGER; TYPE timestamp_with_ltz_Table IS TABLE OF timestamp_ltz_unconstrained INDEX BY BINARY_INTEGER; TYPE timestamp_with_time_zone_Table IS TABLE OF timestamp_tz_unconstrained INDEX BY BINARY_INTEGER; TYPE urowid_table IS TABLE OF UROWID INDEX BY BINARY_INTEGER; TYPE varchar2_table IS TABLE OF VARCHAR2(2000) INDEX BY BINARY_INTEGER;