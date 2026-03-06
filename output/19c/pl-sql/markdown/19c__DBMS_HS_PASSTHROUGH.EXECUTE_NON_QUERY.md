---
id: 19c__DBMS_HS_PASSTHROUGH.EXECUTE_NON_QUERY
name: DBMS_HS_PASSTHROUGH.EXECUTE_NON_QUERY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.EXECUTE_NON_QUERY

This function runs a SQL statement. The SQL statement cannot be a SELECT statement. A cursor has to be open and the SQL statement has to be parsed before the SQL statement can be run.

## Syntax

```sql
DBMS_HS_PASSTHROUGH.EXECUTE_NON_QUERY ( 
   c IN BINARY_INTEGER NOT NULL)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | BINARY_INTEGER | IN | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_HS_PASSTHROUGH.EXECUTE_NON_QUERY ( c IN BINARY_INTEGER NOT NULL) RETURN BINARY_INTEGER; Parameters Table 85-18 EXECUTE_NON_QUERY Function Parameters Parameter Description c Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. Return Values The number of rows affected by the SQL statement in the non-Oracle system Exceptions Table 85-19 EXECUTE_NON_QUERY Function Exceptions Exception Description ORA-28550 The cursor passed is invalid. ORA-28552 Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) ORA-28555 A NULL value was passed for a NOT NULL parameter.