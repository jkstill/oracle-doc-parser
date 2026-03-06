---
id: 19c__DBMS_SQL.LAST_SQL_FUNCTION_CODE
name: DBMS_SQL.LAST_SQL_FUNCTION_CODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.LAST_SQL_FUNCTION_CODE

This function returns the SQL function code for the statement.

## Syntax

```sql
DBMS_SQL.LAST_SQL_FUNCTION_CODE 
   RETURN INTEGER;
```

**Returns:** `INTEGER`

## Usage Notes

These codes are listed in the Oracle Call Interface Programmer's Guide. Syntax DBMS_SQL.LAST_SQL_FUNCTION_CODE RETURN INTEGER; Pragmas pragma restrict_references(last_sql_function_code,RNDS,WNDS); Return Values Returns the SQL function code for the statement Usage Notes You must call this function immediately after the SQL statement is run; otherwise, the return value is undefined.