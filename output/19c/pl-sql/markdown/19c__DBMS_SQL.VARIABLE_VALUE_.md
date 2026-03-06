---
id: 19c__DBMS_SQL.VARIABLE_VALUE_
name: DBMS_SQL.VARIABLE_VALUE,
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.VARIABLE_VALUE,

The type of call determines which procedure or function to use.

## Usage Notes

For queries, call the COLUMN_VALUE Procedure to determine the value of a column retrieved by the FETCH_ROWS Function . For anonymous blocks containing calls to PL / SQL procedures or DML statements with returning clause, call the VARIABLE_VALUE Procedures or the VARIABLE_VALUE_PKG Procedure to retrieve the values assigned to the output variables when statements were run. To fetch only part of a LONG database column (which can be up to two gigabytes in size), use the DEFINE_COLUMN_LONG Procedure . You can specify the offset (in bytes) into the column value, and the number of bytes to fetch.