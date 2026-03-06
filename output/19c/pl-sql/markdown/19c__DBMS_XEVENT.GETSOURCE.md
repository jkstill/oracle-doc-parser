---
id: 19c__DBMS_XEVENT.GETSOURCE
name: DBMS_XEVENT.GETSOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETSOURCE

This function returns the name of the Java class, PL/SQL package or object type implementing the handler.

## Syntax

```sql
DBMS_XEVENT.GETSOURCE (
    handler   IN   XDBHandler) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handler | XDBHandler) | IN | Handler |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBHandler Type Subprograms for other subprograms in this group See Also: XDBHandler Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETSOURCE ( handler IN XDBHandler) RETURN VARCHAR2; Parameters Table 203-36 GETSOURCE Function Parameters Parameter Description handler Handler