---
id: 19c__UTL_CALL_STACK.BACKTRACE_DEPTH
name: UTL_CALL_STACK.BACKTRACE_DEPTH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.BACKTRACE_DEPTH

This function returns the number of backtrace items in the backtrace.

## Syntax

```sql
UTL_CALL_STACK.BACKTRACE_DEPTH 
 RETURN PLS_INTEGER;
```

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_CALL_STACK.BACKTRACE_DEPTH RETURN PLS_INTEGER; Return Values The number of backtrace items in the backtrace, zero in the absence of an exception.