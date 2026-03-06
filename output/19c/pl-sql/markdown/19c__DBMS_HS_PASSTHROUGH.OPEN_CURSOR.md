---
id: 19c__DBMS_HS_PASSTHROUGH.OPEN_CURSOR
name: DBMS_HS_PASSTHROUGH.OPEN_CURSOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HS_PASSTHROUGH
tags: [dbms_hs_passthrough]
source_file: DBMS_HS_PASSTHROUGH.html
---

# DBMS_HS_PASSTHROUGH.OPEN_CURSOR

This function opens a cursor for running a passthrough SQL statement at the non-Oracle system. This function must be called for any type of SQL statement.

## Syntax

```sql
DBMS_HS_PASSTHROUGH.OPEN_CURSOR 
  RETURN BINARY_INTEGER;
```

**Returns:** `BINARY_INTEGER`

## Usage Notes

The function returns a cursor, which must be used in subsequent calls. This call allocates memory. To deallocate the associated memory, call the procedure CLOSE_CURSOR . Syntax DBMS_HS_PASSTHROUGH.OPEN_CURSOR RETURN BINARY_INTEGER; Pragmas Purity level defined : WNDS, RNDS Return Values The cursor to be used on subsequent procedure and function calls. Exceptions Table 85-26 OPEN_CURSOR Function Exceptions Exception Description ORA-28554 Maximum number of open cursor has been exceeded. Increase Heterogeneous Services' OPEN_CURSORS initialization parameter.