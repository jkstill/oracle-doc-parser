---
id: 19c__DBMS_DEBUG.DISABLE_BREAKPOINT
name: DBMS_DEBUG.DISABLE_BREAKPOINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.DISABLE_BREAKPOINT

This function makes an existing breakpoint inactive but leaves it in place.

## Syntax

```sql
DBMS_DEBUG.DISABLE_BREAKPOINT (
   breakpoint IN BINARY_INTEGER)
  RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| breakpoint | BINARY_INTEGER) | IN | Breakpoint number from a previous call to SET_BREAKPOINT |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.DISABLE_BREAKPOINT ( breakpoint IN BINARY_INTEGER) RETURN BINARY_INTEGER; Parameters Table 57-20 DISABLE_BREAKPOINT Function Parameters Parameter Description breakpoint Breakpoint number from a previous call to SET_BREAKPOINT Return Values Table 57-21 DISABLE_BREAKPOINT Function Return Values Returns Description success error_no_such_breakpt No such breakpoint exists error_idle_breakpt Cannot disable an unused breakpoint