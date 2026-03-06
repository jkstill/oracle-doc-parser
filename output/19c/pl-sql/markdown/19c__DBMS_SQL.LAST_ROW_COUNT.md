---
id: 19c__DBMS_SQL.LAST_ROW_COUNT
name: DBMS_SQL.LAST_ROW_COUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.LAST_ROW_COUNT

This function returns the cumulative count of the number of rows fetched.

## Syntax

```sql
DBMS_SQL.LAST_ROW_COUNT 
   RETURN INTEGER;
```

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_SQL.LAST_ROW_COUNT RETURN INTEGER; Pragmas pragma restrict_references(last_row_count,RNDS,WNDS); Return Values Returns the cumulative count of the number of rows fetched Usage Notes Call this function after a FETCH_ROWS or an EXECUTE_AND_FETCH call. If called after an EXECUTE call, then the value returned is zero.