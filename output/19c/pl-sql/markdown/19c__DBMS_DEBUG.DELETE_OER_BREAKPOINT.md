---
id: 19c__DBMS_DEBUG.DELETE_OER_BREAKPOINT
name: DBMS_DEBUG.DELETE_OER_BREAKPOINT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DEBUG
tags: [dbms_debug]
source_file: DBMS_DEBUG.html
---

# DBMS_DEBUG.DELETE_OER_BREAKPOINT

This function deletes an OER breakpoint.

## Syntax

```sql
DBMS_DEBUG.DELETE_OER_BREAKPOINT (
   oer  IN PLS_INTEGER) 
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| oer | PLS_INTEGER) | IN | The OER (positive 4-byte number) to delete |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_DEBUG.DELETE_OER_BREAKPOINT ( oer IN PLS_INTEGER) RETURN PLS_INTEGER; Parameters Table 57-19 DELETE_OER_BREAKPOINT Function Parameters Parameter Description oer The OER (positive 4-byte number) to delete