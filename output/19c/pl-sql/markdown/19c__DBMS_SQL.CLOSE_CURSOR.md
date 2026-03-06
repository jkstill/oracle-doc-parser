---
id: 19c__DBMS_SQL.CLOSE_CURSOR
name: DBMS_SQL.CLOSE_CURSOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.CLOSE_CURSOR

This procedure closes a given cursor.

## Syntax

```sql
DBMS_SQL.CLOSE_CURSOR (
   c    IN OUT INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | INTEGER) | IN OUT | IN |
| c | INTEGER) | IN OUT | OUT |

## Usage Notes

Syntax DBMS_SQL.CLOSE_CURSOR ( c IN OUT INTEGER); Pragmas pragma restrict_references(close_cursor,RNDS,WNDS); Parameters Table 162-10 CLOSE_CURSOR Procedure Parameters Parameter Mode Description c IN ID number of the cursor that you want to close. c OUT Cursor is set to null. After you call CLOSE_CURSOR , the memory allocated to the cursor is released and you can no longer fetch from that cursor.