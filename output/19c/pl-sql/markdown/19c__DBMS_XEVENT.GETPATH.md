---
id: 19c__DBMS_XEVENT.GETPATH
name: DBMS_XEVENT.GETPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETPATH

This function returns the XDBPath object representing the path of the resource for which the event was fired. From this object, functions are provided to get the different path segments.

## Syntax

```sql
DBMS_XEVENT.GETPATH (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBPath;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBPath`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETPATH ( ev IN XDBRepositoryEvent) RETURN XDBPath; Parameters Table 203-33 GETPATH Function Parameters Parameter Description ev Event of XDBRepositoryEvent type