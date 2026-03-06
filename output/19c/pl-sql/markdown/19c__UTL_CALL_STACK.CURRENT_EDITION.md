---
id: 19c__UTL_CALL_STACK.CURRENT_EDITION
name: UTL_CALL_STACK.CURRENT_EDITION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_CALL_STACK
tags: [utl_call_stack]
source_file: UTL_CALL_STACK.html
---

# UTL_CALL_STACK.CURRENT_EDITION

This function returns the current edition name of the unit of the subprogram at the specified dynamic depth.

## Syntax

```sql
UTL_CALL_STACK.CURRENT_EDITION (
   dynamic_depth    IN    PLS_INTEGER) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dynamic_depth | PLS_INTEGER) | IN | Depth in the error stack |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax UTL_CALL_STACK.CURRENT_EDITION ( dynamic_depth IN PLS_INTEGER) RETURN VARCHAR2; Parameters Table 259-5 CURRENT_EDITION Function Parameters Parameter Description dynamic_depth Depth in the error stack Return Values The current edition name of the unit of the subprogram at the specified dynamic depth