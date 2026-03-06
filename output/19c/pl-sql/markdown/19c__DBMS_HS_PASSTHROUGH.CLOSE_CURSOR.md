---
id: 19c__DBMS_HS_PASSTHROUGH.CLOSE_CURSOR
name: DBMS_HS_PASSTHROUGH.CLOSE_CURSOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.CLOSE_CURSOR

This function closes the cursor and releases associated memory after the SQL statement has been run at the non-Oracle system. If the cursor was not open, then the operation is a "no operation".

## Syntax

```sql
DBMS_HS_PASSTHROUGH.CLOSE_CURSOR (
   c IN BINARY_INTEGER NOT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | BINARY_INTEGER | IN | Cursor to be released. |

## Usage Notes

Syntax DBMS_HS_PASSTHROUGH.CLOSE_CURSOR ( c IN BINARY_INTEGER NOT NULL); Pragmas Purity level defined : WNDS, RNDS Parameters Table 85-14 CLOSE_CURSOR Procedure Parameters Parameter Description c Cursor to be released. Exceptions Table 85-15 CLOSE_CURSOR Procedure Exceptions Exception Description ORA-28555 A NULL value was passed for a NOT NULL parameter.