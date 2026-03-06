---
id: 19c__DBMS_SQL.IS_OPEN
name: DBMS_SQL.IS_OPEN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.IS_OPEN

This function checks to see if the given cursor is currently open.

## Syntax

```sql
DBMS_SQL.IS_OPEN (
   c              IN INTEGER)
  RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER) | IN | Cursor ID number of the cursor to check. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_SQL.IS_OPEN ( c IN INTEGER) RETURN BOOLEAN; Pragmas pragma restrict_references(is_open,RNDS,WNDS); Parameters Table 162-27 IS_OPEN Function Parameters Parameter Description c Cursor ID number of the cursor to check. Return Values Returns TRUE for any cursor number that has been opened but not closed, and FALSE for a NULL cursor number. Note that the CLOSE_CURSOR Procedure Procedure NULL s out the cursor variable passed to it. Exceptions ORA-29471 DBMS_SQL access denied: This is raised if an invalid cursor ID number is detected. Once a session has encountered and reported this error, every subsequent DBMS_SQL call in the same session will raise this error, meaning that DBMS_SQL is non-operational for this session.