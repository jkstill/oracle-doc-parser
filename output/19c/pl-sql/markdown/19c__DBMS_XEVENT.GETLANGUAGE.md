---
id: 19c__DBMS_XEVENT.GETLANGUAGE
name: DBMS_XEVENT.GETLANGUAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETLANGUAGE

This function returns the implementation language of the handler.

## Syntax

```sql
DBMS_XEVENT.GETLANGUAGE (
    handler   IN   XDBHandler) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handler | XDBHandler) | IN | Handler |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBHandler Type Subprograms for other subprograms in this group See Also: XDBHandler Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETLANGUAGE ( handler IN XDBHandler) RETURN VARCHAR2; Parameters Table 203-21 GETLANGUAGE Function Parameters Parameter Description handler Handler