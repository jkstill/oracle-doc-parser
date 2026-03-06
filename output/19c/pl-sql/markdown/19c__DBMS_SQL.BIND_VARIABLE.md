---
id: 19c__DBMS_SQL.BIND_VARIABLE
name: DBMS_SQL.BIND_VARIABLE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.BIND_VARIABLE

These procedures bind a given value or set of values to a given variable in a cursor, based on the name of the variable in the statement.

## Syntax

```sql
DBMS_SQL.BIND_VARIABLE (
   c              IN INTEGER,
   name           IN VARCHAR2,
   value          IN <datatype>);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor to which you want to bind a value. |
| name | VARCHAR2 | IN | Name of the variable in the statement. The length of the bind variable name must be <=30 bytes. |
| value | IN | IN | Value that you want to bind to the variable in the cursor. For IN and IN / OUT variables, the value has the same type as the type of the value being passed in for this parameter. |
| out_value_size |  |  | Maximum expected OUT value size, in bytes, for the VARCHAR2 , RAW , CHAR OUT or IN / OUT variable. If no size is given, then the length of the current value is used. This parameter must be specified if the value parameter is not initialized. |

## Usage Notes

Syntax DBMS_SQL.BIND_VARIABLE ( c IN INTEGER, name IN VARCHAR2, value IN <datatype>); Where <datatype> can be any one of the following types: ADT (user-defined object types) BINARY_DOUBLE BINARY_FLOAT BFILE BLOB BOOLEAN CLOB CHARACTER SET ANY_CS DATE DSINTERVAL_UNCONSTRAINED NESTED table NUMBER OPAQUE types REF TIME_UNCONSTRAINED TIME_TZ_UNCONSTRAINED TIMESTAMP_LTZ_UNCONSTRAINED TIMESTAMP_TZ_UNCONSTRAINED TIMESTAMP_UNCONSTRAINED UROWID VARCHAR2 CHARACTER SET ANY_CS VARRAY YMINTERVAL_UNCONSTRAINED Notice that BIND_VARIABLE is overloaded to accept different datatype. The following syntax is also supported for BIND_VARIABLE . The square brackets [] indicate an optional parameter for the BIND_VARIABLE procedure. DBMS_SQL.BIND_VARIABLE ( c IN INTEGER, name IN VARCHAR2, value IN VARCHAR2 CHARACTER SET ANY_CS [,out_value_size IN INTEGER]); To bind CHAR , RAW , and ROWID data, you can use the following variations on the syntax: DBMS_SQL.BIND_VARIABLE_CHAR ( c IN INTEGER, name IN VARCHAR2, value IN CHAR CHARACTER SET ANY_CS [,out_value_size IN INTEGER]); DBMS_SQL.BIND_VARIABLE_RAW ( c IN INTEGER, name IN VARCHAR2, value IN RAW [,out_value_size IN INTEGER]); DBMS_SQL.BIND_VARIABLE_ROWID ( c IN INTEGER, name IN VARCHAR2, value IN ROWID); Pragmas pragma restrict_references(bind_variable,WNDS); Parameters Table 162-8 BIND_VARIABLE Procedures Parameters Parameter Description c ID number of the cursor to which you want to bind a value. name Name of the variable in the statement. The length of the bind variable name must be <=30 bytes. value Value that you want to bind to the variable in the cursor. For IN and IN / OUT variables, the value has the same type as the type of the value being passed in for this parameter. out_value_size Maximum expected OUT value size, in bytes, for the VARCHAR2 , RAW , CHAR OUT or IN / OUT variable. If no size is given, then the length of the current value is used. This parameter must be specified if the value parameter is not initialized. Usage Notes If the variable is an IN or IN / OUT variable or an IN collection, then the given bind value must be valid for the variable or array type. Bind values for OUT variables are ignored. The bind variables or collections of a SQL statement are identified by their names. When binding a value to a bind variable or bind array, the string identifying it in the statement must contain a leading colon, as shown in the following example: SELECT emp_name FROM emp WHERE SAL > :X; For this example, the corresponding bind call would look similar to BIND_VARIABLE(cursor_name, ':X', 3500); or BIND_VARIABLE (cursor_name, 'X', 3500);