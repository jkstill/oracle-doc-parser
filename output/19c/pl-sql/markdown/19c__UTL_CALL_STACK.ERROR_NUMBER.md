---
id: 19c__UTL_CALL_STACK.ERROR_NUMBER
name: UTL_CALL_STACK.ERROR_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.ERROR_NUMBER

This function returns the error number of the error at the specified error depth.

## Syntax

```sql
UTL_CALL_STACK.ERROR_NUMBER (
   error_depth    IN    PLS_INTEGER) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| error_depth | PLS_INTEGER) | IN | Depth in the call stack |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_CALL_STACK.ERROR_NUMBER ( error_depth IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 259-8 ERROR_NUMBER Function Parameters Parameter Description error_depth Depth in the call stack Return Values The error number of the error at the specified error depth