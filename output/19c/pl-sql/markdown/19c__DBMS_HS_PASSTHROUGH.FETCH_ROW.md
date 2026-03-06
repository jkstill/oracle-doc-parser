---
id: 19c__DBMS_HS_PASSTHROUGH.FETCH_ROW
name: DBMS_HS_PASSTHROUGH.FETCH_ROW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.FETCH_ROW

This function fetches rows from a result set.

## Syntax

```sql
DBMS_HS_PASSTHROUGH.FETCH_ROW (
   c   IN BINARY_INTEGER NOT NULL,
   f   IN BOOLEAN)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | BINARY_INTEGER | IN | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. |
| first |  |  | (Optional) Reexecutes SELECT statement. Possible values: - TRUE : reexecute SELECT statement. - FALSE : fetch the next row, or if run for the first time, then execute and fetch rows (default). |

**Returns:** `BINARY_INTEGER`

## Usage Notes

The result set is defined with a SQL SELECT statement. When there are no more rows to be fetched, the exception NO_DATA_FOUND is raised. Before the rows can be fetched, a cursor has to be opened, and the SQL statement has to be parsed. Syntax DBMS_HS_PASSTHROUGH.FETCH_ROW ( c IN BINARY_INTEGER NOT NULL, f IN BOOLEAN) RETURN BINARY_INTEGER; Pragmas Purity level defined : WNDS Parameters Table 85-20 FETCH_ROW Function Parameters Parameter Description c Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines OPEN_CURSOR and PARSE respectively. first (Optional) Reexecutes SELECT statement. Possible values: - TRUE : reexecute SELECT statement. - FALSE : fetch the next row, or if run for the first time, then execute and fetch rows (default). Return Values The returns the number of rows fetched. The function returns "0" if the last row was already fetched.