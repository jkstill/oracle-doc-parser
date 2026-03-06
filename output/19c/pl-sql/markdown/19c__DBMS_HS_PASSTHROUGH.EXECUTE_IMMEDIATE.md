---
id: 19c__DBMS_HS_PASSTHROUGH.EXECUTE_IMMEDIATE
name: DBMS_HS_PASSTHROUGH.EXECUTE_IMMEDIATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.EXECUTE_IMMEDIATE

This function runs a SQL statement immediately. Any valid SQL command except SELECT can be run immediately.

## Syntax

```sql
DBMS_HS_PASSTHROUGH.EXECUTE_IMMEDIATE ( 
   s IN VARCHAR2 NOT NULL)  
RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| s | VARCHAR2 | IN | VARCHAR2 variable with the statement to be executed immediately. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

The statement must not contain any bind variables. The statement is passed in as a VARCHAR2 in the argument. Internally the SQL statement is run using the PASSTHROUGH SQL protocol sequence of OPEN_CURSOR , PARSE , EXECUTE_NON_QUERY , CLOSE_CURSOR . Syntax DBMS_HS_PASSTHROUGH.EXECUTE_IMMEDIATE ( s IN VARCHAR2 NOT NULL) RETURN BINARY_INTEGER; Parameters Table 85-16 EXECUTE_IMMEDIATE Procedure Parameters Parameter Description s VARCHAR2 variable with the statement to be executed immediately. Return Values The number of rows affected by the execution of the SQL statement. Exceptions Table 85-17 EXECUTE_IMMEDIATE Procedure Exceptions Exception Description ORA-28551 SQL statement is invalid. ORA-28554 Max open cursors. ORA-28555 A NULL value was passed for a NOT NULL parameter.