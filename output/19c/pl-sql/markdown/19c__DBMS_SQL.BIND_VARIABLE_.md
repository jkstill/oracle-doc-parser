---
id: 19c__DBMS_SQL.BIND_VARIABLE_
name: DBMS_SQL.BIND_VARIABLE,
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.BIND_VARIABLE,

Many DML statements require that data in your program be input to Oracle. When you define a SQL statement that contains input data to be supplied at runtime, you must use placeholders in the SQL statement to mark where data must be supplied.

## Usage Notes

For each placeholder in the SQL statement, you must call one of the BIND_ARRAY Procedures , or BIND_VARIABLE Procedures , or the BIND_VARIABLE_PKG Procedure to supply the value of a variable in your program (or the values of an array) to the placeholder. When the SQL statement is subsequently run, Oracle uses the data that your program has placed in the output and input, or bind variables. DBMS_SQL can run a DML statement multiple times — each time with a different bind variable. The BIND_ARRAY procedure lets you bind a collection of scalars, each value of which is used as an input variable once for each EXECUTE . This is similar to the array interface supported by the OCI. Note that the datatype of the values bound to placeholders cannot be PL/SQL-only datatypes.