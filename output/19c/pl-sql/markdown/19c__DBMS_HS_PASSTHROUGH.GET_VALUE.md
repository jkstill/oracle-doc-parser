---
id: 19c__DBMS_HS_PASSTHROUGH.GET_VALUE
name: DBMS_HS_PASSTHROUGH.GET_VALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.GET_VALUE

This procedure has two purposes: it retrieves the select list items of SELECT statements after a row has been fetched, and it retrieves the OUT bind values, after the SQL statement has been run.

## Syntax

```sql
DBMS_HS_PASSTHROUGH.GET_VALUE (
   c      IN  BINARY_INTEGER NOT NULL,
   p    IN  BINARY_INTEGER NOT NULL,
   v    OUT <dty>);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | BINARY_INTEGER | IN | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. |
| p | BINARY_INTEGER | IN | Position of the bind variable or select list item in the SQL statement: Starts at 1. |
| v | OUT | IN | Variable in which the OUT bind variable or select list item stores its value. |

## Usage Notes

Syntax DBMS_HS_PASSTHROUGH.GET_VALUE ( c IN BINARY_INTEGER NOT NULL, p IN BINARY_INTEGER NOT NULL, v OUT <dty>); <dty> is either DATE , NUMBER , or VARCHAR2 . See Also: For retrieving values of datatype RAW , see GET_VALUE_RAW Procedure . See Also: For retrieving values of datatype RAW , see GET_VALUE_RAW Procedure . Pragmas Purity level defined : WNDS Parameters Table 85-22 GET_VALUE Procedure Parameters Parameter Description c Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. p Position of the bind variable or select list item in the SQL statement: Starts at 1. v Variable in which the OUT bind variable or select list item stores its value. Exceptions Table 85-23 GET_VALUE Procedure Exceptions Exception Description ORA-1403 Returns NO_DATA_FOUND exception when running the GET_VALUE after the last row was fetched (that is, FETCH_ROW returned "0"). ORA-28550 The cursor passed is invalid. ORA-28552 Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) ORA-28553 The position of the bind variable is out of range. ORA-28555 A NULL value was passed for a NOT NULL parameter.