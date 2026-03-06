---
id: 19c__UTL_CALL_STACK.SUBPROGRAM
name: UTL_CALL_STACK.SUBPROGRAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.SUBPROGRAM

This function returns the unit-qualified name of the subprogram at the specified dynamic depth.

## Syntax

```sql
UTL_CALL_STACK.SUBPROGRAM (
   dynamic_depth    IN    PLS_INTEGER) 
 RETURN UNIT_QUALIFIED_NAME;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dynamic_depth | PLS_INTEGER) | IN | Depth in the call stack |

**Returns:** `UNIT_QUALIFIED_NAME`

## Usage Notes

Syntax UTL_CALL_STACK.SUBPROGRAM ( dynamic_depth IN PLS_INTEGER) RETURN UNIT_QUALIFIED_NAME; Parameters Table 259-12 SUBPROGRAM Function Parameters Parameter Description dynamic_depth Depth in the call stack Return Values Returns the unit-qualified name of the subprogram at the specified dynamic depth