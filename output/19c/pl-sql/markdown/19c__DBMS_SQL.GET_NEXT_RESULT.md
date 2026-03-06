---
id: 19c__DBMS_SQL.GET_NEXT_RESULT
name: DBMS_SQL.GET_NEXT_RESULT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.GET_NEXT_RESULT

This procedure gets the statement of the next result returned to the caller of the recursive statement or, if this caller sets itself as the client for the recursive statement, the next result returned to this caller as client.

## Syntax

```sql
DBMS_SQL.GET_NEXT_RESULT(
   c            IN          INTEGER,
   rc           OUT         SYS_REFCURSOR);

DBMS_SQL.GET_NEXT_RESULT(
   c            IN          INTEGER,
   rc           OUT         INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER | IN | Recursive statement cursor |
| rc | SYS_REFCURSOR) | OUT | Cursor or ref cursor of the statement of the next returned result |

## Usage Notes

The statements are returned in same order as they are returned by the RETURN_RESULT Procedures . Syntax DBMS_SQL.GET_NEXT_RESULT( c IN INTEGER, rc OUT SYS_REFCURSOR); DBMS_SQL.GET_NEXT_RESULT( c IN INTEGER, rc OUT INTEGER); Parameters Table 162-26 GET_NEXT_RESULT Procedure Parameters Parameter Description c Recursive statement cursor rc Cursor or ref cursor of the statement of the next returned result Exceptions ORA-01403 no_data_found: This is raised when there is no further returned statement result. Usage Notes After the cursor of a statement result is retrieved, the caller must close the cursor properly when it is no longer needed. The cursors for all unretrieved returned statements will be closed after the cursor of the recursive statement is closed.