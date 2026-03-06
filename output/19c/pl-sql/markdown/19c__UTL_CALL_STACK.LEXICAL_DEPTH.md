---
id: 19c__UTL_CALL_STACK.LEXICAL_DEPTH
name: UTL_CALL_STACK.LEXICAL_DEPTH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.LEXICAL_DEPTH

This function returns the lexical nesting level of the subprogram at the specified dynamic depth.

## Syntax

```sql
UTL_CALL_STACK.LEXICAL_DEPTH (
   dynamic_depth    IN    PLS_INTEGER) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dynamic_depth | PLS_INTEGER) | IN | Depth in the call stack |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_CALL_STACK.LEXICAL_DEPTH ( dynamic_depth IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 259-9 LEXICAL_DEPTH Function Parameters Parameter Description dynamic_depth Depth in the call stack Return Values The lexical nesting level of the subprogram at the specified dynamic depth