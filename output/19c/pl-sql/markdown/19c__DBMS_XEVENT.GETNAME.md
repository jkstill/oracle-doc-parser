---
id: 19c__DBMS_XEVENT.GETNAME
name: DBMS_XEVENT.GETNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETNAME

This function returns the string representation of the path.

## Syntax

```sql
DBMS_XEVENT.GETNAME (
    path   IN   XDBPath) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | XDBPath) | IN | Path |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBPath Type Subprograms for other subprograms in this group See Also: XDBPath Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETNAME ( path IN XDBPath) RETURN VARCHAR2; Parameters Table 203-22 GETNAME Function Parameters Parameter Description path Path