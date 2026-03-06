---
id: 19c__UTL_CALL_STACK.UNIT_LINE
name: UTL_CALL_STACK.UNIT_LINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.UNIT_LINE

This function returns the line number of the unit of the subprogram at the specified dynamic depth.

## Syntax

```sql
UTL_CALL_STACK.UNIT_LINE (
   dynamic_depth    IN    PLS_INTEGER) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dynamic_depth | PLS_INTEGER) | IN | Depth in the call stack |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_CALL_STACK.UNIT_LINE ( dynamic_depth IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 259-11 UNIT_LINE Function Parameters Parameter Description dynamic_depth Depth in the call stack Return Values The line number of the unit of the subprogram at the specified dynamic depth