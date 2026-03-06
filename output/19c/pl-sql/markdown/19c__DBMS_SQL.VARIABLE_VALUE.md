---
id: 19c__DBMS_SQL.VARIABLE_VALUE
name: DBMS_SQL.VARIABLE_VALUE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.VARIABLE_VALUE

This procedure returns the value of the named variable for a given cursor. It is used to return the values of bind variables inside PL/SQL blocks or DML statements with returning clause.

## Syntax

```sql
DBMS_SQL.VARIABLE_VALUE (
   c               IN  INTEGER,
   name            IN  VARCHAR2,
   value           OUT NOCOPY <datatype>);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor from which to get the values. |
| name | VARCHAR2 | IN | Name of the variable for which you are retrieving the value. |
| value | NOCOPY | OUT | Single row option: Returns the value of the variable for the specified position. Oracle raises the exception ORA-06562 , inconsistent_type , if the type of this output parameter differs from the actual type of the value, as defined by the call to BIND_VARIABLE . Array option: Local variable that has been declared < table_type >. For bulk operations, value is an OUT NOCOPY parameter. |

## Usage Notes

Syntax DBMS_SQL.VARIABLE_VALUE ( c IN INTEGER, name IN VARCHAR2, value OUT NOCOPY <datatype>); Where <datatype> can be any one of the following types: ADT (user-defined object types) BINARY_DOUBLE BINARY_FLOAT BFILE BLOB BOOLEAN CLOB CHARACTER SET ANY_CS DATE DSINTERVAL_UNCONSTRAINED NESTED table NUMBER OPAQUE types REF TIME_UNCONSTRAINED TIME_TZ_UNCONSTRAINED TIMESTAMP_LTZ_UNCONSTRAINED TIMESTAMP_TZ_UNCONSTRAINED TIMESTAMP_UNCONSTRAINED UROWID VARCHAR2 CHARACTER SET ANY_CS VARRAY YMINTERVAL_UNCONSTRAINED For variables containing CHAR , RAW , and ROWID data, you can use the following variations on the syntax: DBMS_SQL.VARIABLE_VALUE_CHAR ( c IN INTEGER, name IN VARCHAR2, value OUT CHAR CHARACTER SET ANY_CS); DBMS_SQL.VARIABLE_VALUE_RAW ( c IN INTEGER, name IN VARCHAR2, value OUT RAW); DBMS_SQL.VARIABLE_VALUE_ROWID ( c IN INTEGER, name IN VARCHAR2, value OUT ROWID); The following syntax enables the VARIABLE_VALUE procedure to accommodate bulk operations: DBMS_SQL.VARIABLE_VALUE ( c IN INTEGER, name IN VARCHAR2, value OUT NOCOPY <table_type>); For bulk operations, < table_type > must be a supported DBMS_SQL predefined TABLE type. See DBMS_SQL Data Structures Pragmas pragma restrict_references(variable_value,RNDS,WNDS); Parameters Table 162-33 VARIABLE_VALUE Procedure Parameters Parameter Description c ID number of the cursor from which to get the values. name Name of the variable for which you are retrieving the value. value Single row option: Returns the value of the variable for the specified position. Oracle raises the exception ORA-06562 , inconsistent_type , if the type of this output parameter differs from the actual type of the value, as defined by the call to BIND_VARIABLE . Array option: Local variable that has been declared < table_type >. For bulk operations, value is an OUT NOCOPY parameter.