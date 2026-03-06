---
id: 19c__DBMS_SQL.EXECUTE_AND_FETCH
name: DBMS_SQL.EXECUTE_AND_FETCH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.EXECUTE_AND_FETCH

This function executes the given cursor and fetches rows.

## Syntax

```sql
DBMS_SQL.EXECUTE_AND_FETCH (
   c              IN INTEGER,
   exact          IN BOOLEAN DEFAULT FALSE)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | ID number of the cursor to execute and fetch. |
| exact | BOOLEAN | IN | Set to TRUE to raise an exception if the number of rows actually matching the query differs from one. Note: Oracle does not support the exact fetch TRUE option with LONG columns. Even if an exception is raised, the rows are still fetched and available. |

**Returns:** `INTEGER`

## Usage Notes

This function provides the same functionality as calling EXECUTE and then calling FETCH_ROWS . Calling EXECUTE_AND_FETCH instead, however, may reduce the number of network round-trips when used against a remote database. The EXECUTE_AND_FETCH function returns the number of rows actually fetched. Syntax DBMS_SQL.EXECUTE_AND_FETCH ( c IN INTEGER, exact IN BOOLEAN DEFAULT FALSE) RETURN INTEGER; Pragmas pragma restrict_references(execute_and_fetch,WNDS); Parameters Table 162-24 EXECUTE_AND_FETCH Function Parameters Parameter Description c ID number of the cursor to execute and fetch. exact Set to TRUE to raise an exception if the number of rows actually matching the query differs from one. Note: Oracle does not support the exact fetch TRUE option with LONG columns. Even if an exception is raised, the rows are still fetched and available. Return Values Returns designated rows