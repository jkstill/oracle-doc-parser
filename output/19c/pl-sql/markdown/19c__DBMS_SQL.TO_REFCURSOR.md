---
id: 19c__DBMS_SQL.TO_REFCURSOR
name: DBMS_SQL.TO_REFCURSOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.TO_REFCURSOR

This function takes an OPEN ed, PARSE d, and EXECUTE d cursor and transforms/migrates it into a PL/SQL manageable REF CURSOR (a weakly-typed cursor) that can be consumed by PL/SQL native dynamic SQL switched to use native dynamic SQL.

## Syntax

```sql
DBMS_SQL.TO_REFCURSOR(
   cursor_number IN OUT INTEGER)
  RETURN SYS_REFCURSOR;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cursor_number | INTEGER) | IN OUT | Cursor number of the cursor to be transformed into REF CURSOR |

**Returns:** `SYS_REFCURSOR`

## Usage Notes

This subprogram is only used with SELECT cursors. Syntax DBMS_SQL.TO_REFCURSOR( cursor_number IN OUT INTEGER) RETURN SYS_REFCURSOR; Parameters Table 162-32 TO_REFCURSOR Function Parameters Parameter Description cursor_number Cursor number of the cursor to be transformed into REF CURSOR Return Values Returns a PL/SQL REF CURSOR transformed from a DBMS_SQL cursor number Usage Notes The cursor passed in by the cursor_number has to be OPEN ed, PARSE d, and EXECUTE d; otherwise an error is raised. Once the cursor_number is transformed into a REF CURSOR , the cursor_number is no longer accessible by any DBMS_SQL operations. After a cursor_number is transformed into a REF CURSOR , using DBMS_SQL . IS_OPEN to check to see if the cursor_number is still open results in an error. If the cursor number was last parsed with a valid container parameter, it cannot be converted to a REF CURSOR .