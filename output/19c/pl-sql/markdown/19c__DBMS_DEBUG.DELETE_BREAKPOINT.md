---
id: 19c__DBMS_DEBUG.DELETE_BREAKPOINT
name: DBMS_DEBUG.DELETE_BREAKPOINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.DELETE_BREAKPOINT

This function deletes a breakpoint.

## Syntax

```sql
DBMS_DEBUG.DELETE_BREAKPOINT (
   breakpoint IN BINARY_INTEGER)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| breakpoint | BINARY_INTEGER) | IN | Breakpoint number from a previous call to SET_BREAKPOINT |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.DELETE_BREAKPOINT ( breakpoint IN BINARY_INTEGER) RETURN BINARY_INTEGER; Parameters Table 57-17 DELETE_BREAKPOINT Function Parameters Parameter Description breakpoint Breakpoint number from a previous call to SET_BREAKPOINT Return Values Table 57-18 DELETE_BREAKPOINT Function Return Values Return Description success error_no_such_breakpt No such breakpoint exists error_idle_breakpt Cannot delete an unused breakpoint error_stale_breakpt The program unit was redefined since the breakpoint was set