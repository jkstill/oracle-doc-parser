---
id: 19c__DBMS_SQL.DEFINE_COLUMN_
name: DBMS_SQL.DEFINE_COLUMN,
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.DEFINE_COLUMN,

The DEFINE_COLUMN , DEFINE_COLUMN_LONG , and DEFINE_ARRAY procedures specify the variables that receive SELECT values on a query.

## Usage Notes

The columns of the row being selected in a SELECT statement are identified by their relative positions as they appear in the select list, from left to right. For a query, you must call one of the define procedures ( DEFINE_COLUMN Procedures , DEFINE_COLUMN_LONG Procedure , or DEFINE_ARRAY Procedure ) to specify the variables that are to receive the SELECT values, much the way an INTO clause does for a static query. Use the DEFINE_COLUMN_LONG procedure to define LONG columns, in the same way that DEFINE_COLUMN is used to define non- LONG columns. You must call DEFINE_COLUMN_LONG before using the COLUMN_VALUE_LONG Procedure to fetch from the LONG column. Use the DEFINE_ARRAY procedure to define a PL/SQL collection into which you want to fetch rows in a single SELECT statement. DEFINE_ARRAY provides an interface to fetch multiple rows at one fetch. You must call DEFINE_ARRAY before using the COLUMN_VALUE procedure to fetch the rows.