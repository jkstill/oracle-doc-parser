---
id: 19c__UTL_CALL_STACK.OWNER
name: UTL_CALL_STACK.OWNER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.OWNER

This function returns the owner name of the unit of the subprogram at the specified dynamic depth.

## Syntax

```sql
UTL_CALL_STACK.OWNER (
   dynamic_depth    IN    PLS_INTEGER) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dynamic_depth | PLS_INTEGER) | IN | Depth in the call stack |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_CALL_STACK.OWNER ( dynamic_depth IN PLS_INTEGER) RETURN VARCHAR2; Parameters Table 259-10 OWNER Function Parameters Parameter Description dynamic_depth Depth in the call stack Return Values The owner name of the unit of the subprogram at the specified dynamic depth