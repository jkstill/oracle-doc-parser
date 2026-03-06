---
id: 19c__DBMS_SQL.COLUMN_VALUE
name: DBMS_SQL.COLUMN_VALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.COLUMN_VALUE

This procedure returns the value of the cursor element for a given position in a given cursor. This procedure is used to access the data fetched by calling FETCH_ROWS .

## Syntax

```sql
DBMS_SQL.COLUMN_VALUE (
   c                 IN  INTEGER,
   position          IN  INTEGER,
   value             OUT <datatype> 
 [,column_error      OUT NUMBER] 
 [,actual_length     OUT INTEGER]);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor from which you are fetching the values. |
| position | INTEGER | IN | Relative position of the column in the cursor. The first column in a statement has position 1. |
| value | OUT | IN | Returns the value at the specified column. Oracle raises exception ORA-06562 , inconsistent_type , if the type of this output parameter differs from the actual type of the value, as defined by the call to DEFINE_COLUMN . |
| column_error | NUMBER | OUT | Returns any error code for the specified column value. |
| actual_length | INTEGER | OUT | The actual length, before any truncation, of the value in the specified column. |

## Usage Notes

Syntax DBMS_SQL.COLUMN_VALUE ( c IN INTEGER, position IN INTEGER, value OUT <datatype> [,column_error OUT NUMBER] [,actual_length OUT INTEGER]); Where square brackets [ ] indicate optional parameters and < datatype > can be any one of the following types: BINARY_DOUBLE BINARY_FLOAT BFILE BLOB CLOB CHARACTER SET ANY_CS DATE DSINTERVAL_UNCONSTRAINED NUMBER TIME_TZ_UNCONSTRAINED TIME_UNCONSTRAINED TIMESTAMP_LTZ_UNCONSTRAINED TIMESTAMP_TZ_UNCONSTRAINED TIMESTAMP_UNCONSTRAINED UROWID VARCHAR2 CHARACTER SET ANY_CS YMINTERVAL_UNCONSTRAINED user-defined object types collections (VARRAYs and nested tables) REFs Opaque types For variables containing CHAR , RAW , and ROWID data, you can use the following variations on the syntax: DBMS_SQL.COLUMN_VALUE_CHAR ( c IN INTEGER, position IN INTEGER, value OUT CHAR CHARACTER SET ANY_CS [,column_error OUT NUMBER] [,actual_length OUT INTEGER]); DBMS_SQL.COLUMN_VALUE_RAW ( c IN INTEGER, position IN INTEGER, value OUT RAW [,column_error OUT NUMBER] [,actual_length OUT INTEGER]); DBMS_SQL.COLUMN_VALUE_ROWID ( c IN INTEGER, position IN INTEGER, value OUT ROWID [,column_error OUT NUMBER] [,actual_length OUT INTEGER]); The following syntax enables the COLUMN_VALUE procedure to accommodate bulk operations: DBMS_SQL.COLUMN_VALUE( c IN INTEGER, position IN INTEGER, <param_name> IN OUT NOCOPY <table_type>); Where the < param_name > and its corresponding < table_type > can be any one of these matching pairs: bdbl_tab Binary_Double_Table bflt_tab Binary_Float_Table bf_tab Bfile_Table bl_tab Blob_Table cl_tab Clob_Table d_tab Date_Table ids_tab Interval_Day_To_Second_Table iym_tab Interval_Year_To_Month_Table n_tab Number_Table tm_tab Time_Table ttz_tab Time_With_Time_Zone_Table tms_tab Timestamp_Table tstz_tab Timestamp_With_ltz_Table tstz_tab Timestamp_With_Time_Zone_Table ur_tab Urowid_Table c_tab Varchar2_Table Pragmas pragma restrict_references(column_value,RNDS,WNDS); Parameters Table 162-11 COLUMN_VALUE Procedure Parameters (Single Row) Parameter Description c ID number of the cursor from which you are fetching the values. position Relative position of the column in the cursor. The first column in a statement has position 1. value Returns the value at the specified column. Oracle raises exception ORA-06562 , inconsistent_type , if the type of this output parameter differs from the actual type of the value, as defined by the call to DEFINE_COLUMN . column_error Returns any error code for the specified column value. actual_length The actual length, before any truncation, of the value in the specified column. Table 162-12 COLUMN_VALUE Procedure Parameters (Bulk) Parameter Description c ID number of the cursor from which you are fetching the values. position Relative position of the column in the cursor. The first column in a statement has position 1. <param_name> Local variable that has been declared < table_type >. < param_name > is an IN OUT NOCOPY parameter for bulk operations. For bulk operations, the subprogram appends the new elements at the appropriate (implicitly maintained) index. For instance if on utilizing the DEFINE_ARRAY Procedure a batch size (the cnt parameter) of 10 rows was specified and a start index ( lower_bound ) of 1 was specified, then the first call to this subprogram after calling the FETCH_ROWS Function will populate elements at index 1..10, and the next call will populate elements 11..20, and so on. Exceptions INCONSISTENT_TYPE ( ORA - 06562 ) is raised if the type of the given OUT parameter value is different from the actual type of the value. This type was the given type when the column was defined by calling procedure DEFINE_COLUMN .