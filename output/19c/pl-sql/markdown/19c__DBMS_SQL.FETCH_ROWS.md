---
id: 19c__DBMS_SQL.FETCH_ROWS
name: DBMS_SQL.FETCH_ROWS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.FETCH_ROWS

This function fetches a row from a given cursor.

## Syntax

```sql
DBMS_SQL.FETCH_ROWS (
   c              IN INTEGER)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER) | IN | ID number. |

**Returns:** `INTEGER`

## Usage Notes

You can call FETCH_ROWS repeatedly as long as there are rows remaining to be fetched. These rows are retrieved into a buffer, and must be read by calling COLUMN_VALUE , for each column, after each call to FETCH_ROWS . The FETCH_ROWS function accepts the ID number of the cursor to fetch, and returns the number of rows actually fetched. Syntax DBMS_SQL.FETCH_ROWS ( c IN INTEGER) RETURN INTEGER; Pragmas pragma restrict_references(fetch_rows,WNDS); Parameters Table 162-25 FETCH_ROWS Function Parameters Parameter Description c ID number. Return Values Returns a row from a given cursor