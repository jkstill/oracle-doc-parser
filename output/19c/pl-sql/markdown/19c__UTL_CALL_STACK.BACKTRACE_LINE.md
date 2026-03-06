---
id: 19c__UTL_CALL_STACK.BACKTRACE_LINE
name: UTL_CALL_STACK.BACKTRACE_LINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.BACKTRACE_LINE

This function returns the line number of the unit at the specified backtrace depth.

## Syntax

```sql
UTL_CALL_STACK.BACKTRACE_LINE (
   backtrace_depth   IN   PLS_INTEGER)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| backtrace_depth | PLS_INTEGER) | IN | Depth in backtrace |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_CALL_STACK.BACKTRACE_LINE ( backtrace_depth IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 259-3 BACKTRACE_LINE Function Parameters Parameter Description backtrace_depth Depth in backtrace Return Values The line number of the unit at the specified backtrace depth