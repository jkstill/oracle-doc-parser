---
id: 19c__DBMS_DEBUG.ENABLE_BREAKPOINT
name: DBMS_DEBUG.ENABLE_BREAKPOINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.ENABLE_BREAKPOINT

This function is the reverse of disabling. This enables a previously disabled breakpoint.

## Syntax

```sql
DBMS_DEBUG.ENABLE_BREAKPOINT (
   breakpoint IN BINARY_INTEGER)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| breakpoint | BINARY_INTEGER) | IN | Breakpoint number from a previous call to SET_BREAKPOINT |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.ENABLE_BREAKPOINT ( breakpoint IN BINARY_INTEGER) RETURN BINARY_INTEGER; Parameters Table 57-22 ENABLE_BREAKPOINT Function Parameters Parameter Description breakpoint Breakpoint number from a previous call to SET_BREAKPOINT Return Values Table 57-23 ENABLE_BREAKPOINT Function Return Values Return Description success Success error_no_such_breakpt No such breakpoint exists error_idle_breakpt Cannot enable an unused breakpoint