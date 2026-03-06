---
id: 19c__DBMS_XEVENT.GETNEXT
name: DBMS_XEVENT.GETNEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETNEXT

This function returns the next handler in the list.

## Syntax

```sql
DBMS_XEVENT.GETNEXT (
    hl   IN   XDBHandlerList) 
  RETURN XDBHandler;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| hl | XDBHandlerList) | IN | Handler list |

**Returns:** `XDBHandler`

## Usage Notes

See Also: XDBHandlerList Type Subprograms for other subprograms in this group See Also: XDBHandlerList Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETNEXT ( hl IN XDBHandlerList) RETURN XDBHandler; Parameters Table 203-23 GETNEXT Function Parameters Parameter Description hl Handler list