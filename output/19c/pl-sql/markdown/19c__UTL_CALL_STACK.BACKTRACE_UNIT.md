---
id: 19c__UTL_CALL_STACK.BACKTRACE_UNIT
name: UTL_CALL_STACK.BACKTRACE_UNIT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.BACKTRACE_UNIT

This function returns the name of the unit at the specified backtrace depth.

## Syntax

```sql
UTL_CALL_STACK.BACKTRACE_UNIT (
   backtrace_depth   IN   PLS_INTEGER)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| backtrace_depth | PLS_INTEGER) | IN | Depth in backtrace |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_CALL_STACK.BACKTRACE_UNIT ( backtrace_depth IN PLS_INTEGER) RETURN VARCHAR2; Parameters Table 259-4 BACKTRACE_UNIT Function Parameters Parameter Description backtrace_depth Depth in backtrace Return Values The name of the unit at the specified backtrace depth