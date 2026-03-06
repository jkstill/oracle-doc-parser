---
id: 19c__DBMS_SQL.EXECUTE
name: DBMS_SQL.EXECUTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.EXECUTE

This function executes a given cursor. This function accepts the ID number of the cursor and returns the number of rows processed.

## Syntax

```sql
DBMS_SQL.EXECUTE (
   c   IN INTEGER)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER) | IN | Cursor ID number of the cursor to execute. |

**Returns:** `INTEGER`

## Usage Notes

The return value is only valid for INSERT , UPDATE , and DELETE statements; for other types of statements, including DDL, the return value is undefined and must be ignored. Syntax DBMS_SQL.EXECUTE ( c IN INTEGER) RETURN INTEGER; Parameters Table 162-23 EXECUTE Function Parameters Parameter Description c Cursor ID number of the cursor to execute. Return Values Returns number of rows processed Usage Notes The DBMS_SQL cursor that is returned by the TO_CURSOR_NUMBER Function performs in the same way as a DBMS_SQL cursor that has already been executed. Consequently, calling EXECUTE for this cursor will cause an error.