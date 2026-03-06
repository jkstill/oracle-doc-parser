---
id: 19c__UTL_CALL_STACK.ERROR_MSG
name: UTL_CALL_STACK.ERROR_MSG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.ERROR_MSG

This function returns the error message of the error at the specified error depth.

## Syntax

```sql
UTL_CALL_STACK.ERROR_MSG (
   error_depth    IN    PLS_INTEGER) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| error_depth | PLS_INTEGER) | IN | Depth in the error stack |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_CALL_STACK.ERROR_MSG ( error_depth IN PLS_INTEGER) RETURN VARCHAR2; Parameters Table 259-7 ERROR_MSG Function Parameters Parameter Description error_depth Depth in the error stack Return Values The error message of the error at the specified error depth.