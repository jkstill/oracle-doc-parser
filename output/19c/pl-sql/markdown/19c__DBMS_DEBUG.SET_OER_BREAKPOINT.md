---
id: 19c__DBMS_DEBUG.SET_OER_BREAKPOINT
name: DBMS_DEBUG.SET_OER_BREAKPOINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.SET_OER_BREAKPOINT

This function sets an OER breakpoint.

## Syntax

```sql
DBMS_DEBUG.SET_OER_BREAKPOINT (
   oer  IN PLS_INTEGER) 
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oer | PLS_INTEGER) | IN | The OER (positive 4-byte number) to set |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.SET_OER_BREAKPOINT ( oer IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 57-45 SET_OER_BREAKPOINT Function Parameters Parameter Description oer The OER (positive 4-byte number) to set Return Values Table 57-46 SET_OER_BREAKPOINT Function Return Values Return Description success A successful completion error_no_such_breakpt No such OER breakpoint exists