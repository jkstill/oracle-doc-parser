---
id: 19c__DBMS_HS_PASSTHROUGH.BIND_VARIABLE_RAW
name: DBMS_HS_PASSTHROUGH.BIND_VARIABLE_RAW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.BIND_VARIABLE_RAW

This procedure binds IN variables of type RAW .

## Syntax

```sql
DBMS_HS_PASSTHROUGH.BIND_VARIABLE_RAW (
   c    IN BINARY_INTEGER NOT NULL,
   p    IN BINARY_INTEGER NOT NULL,
   v    IN RAW,  
   n    IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | BINARY_INTEGER | IN | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. |
| p | BINARY_INTEGER | IN | Position of the bind variable in the SQL statement: Starts at 1. |
| v | RAW | IN | Value that must be passed to the bind variable. |
| n | VARCHAR2) | IN | (Optional) Name of the bind variable. For example, in SELECT * FROM emp WHERE ename=:ename , the position of the bind variable : ename is 1, the name is : ename . This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

## Usage Notes

Syntax DBMS_HS_PASSTHROUGH.BIND_VARIABLE_RAW ( c IN BINARY_INTEGER NOT NULL, p IN BINARY_INTEGER NOT NULL, v IN RAW, n IN VARCHAR2); Pragmas Purity level defined : WNDS, RNDS Parameters Table 85-12 BIND_VARIABLE_RAW Procedure Parameters Parameter Description c Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. p Position of the bind variable in the SQL statement: Starts at 1. v Value that must be passed to the bind variable. n (Optional) Name of the bind variable. For example, in SELECT * FROM emp WHERE ename=:ename , the position of the bind variable : ename is 1, the name is : ename . This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. Exceptions Table 85-13 BIND_VARIABLE_RAW Procedure Exceptions Exception Description ORA-28550 The cursor passed is invalid. ORA-28552 Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) ORA-28553 The position of the bind variable is out of range. ORA-28555 A NULL value was passed for a NOT NULL parameter.