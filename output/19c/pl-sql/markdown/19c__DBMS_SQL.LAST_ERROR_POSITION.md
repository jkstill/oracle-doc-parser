---
id: 19c__DBMS_SQL.LAST_ERROR_POSITION
name: DBMS_SQL.LAST_ERROR_POSITION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.LAST_ERROR_POSITION

This function returns the byte offset in the SQL statement text where the error occurred. The first character in the SQL statement is at position 0.

## Syntax

```sql
DBMS_SQL.LAST_ERROR_POSITION 
   RETURN INTEGER;
```

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_SQL.LAST_ERROR_POSITION RETURN INTEGER; Pragmas pragma restrict_references(last_error_position,RNDS,WNDS); Return Values Returns the byte offset in the SQL statement text where the error occurred Usage Notes Call this function after a PARSE call, before any other DBMS_SQL procedures or functions are called.