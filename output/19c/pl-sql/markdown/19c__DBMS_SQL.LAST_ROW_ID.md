---
id: 19c__DBMS_SQL.LAST_ROW_ID
name: DBMS_SQL.LAST_ROW_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.LAST_ROW_ID

This function returns the ROWID of the last row processed.

## Syntax

```sql
DBMS_SQL.LAST_ROW_ID 
   RETURN ROWID;
```

**Returns:** `ROWID`

## Usage Notes

Syntax DBMS_SQL.LAST_ROW_ID RETURN ROWID; Pragmas pragma restrict_references(last_row_id,RNDS,WNDS); Return Values Returns the ROWID of the last row processed Usage Notes Call this function after a FETCH_ROWS or an EXECUTE_AND_FETCH call.