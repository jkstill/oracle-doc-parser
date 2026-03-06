---
id: 19c__DBMS_XEVENT.GETPARENTPATH
name: DBMS_XEVENT.GETPARENTPATH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETPARENTPATH

This function returns the parent's path. The level indicates the number of levels up the hierarchy. This value must be greater than zero. Level 1 means the immediate parent. If level exceeds the height of the tree then a NULL is returned.

## Syntax

```sql
DBMS_XEVENT.GETPARENTPATH (
    path   IN   XDBPath,
   level   IN   INTEGER) 
  RETURN XDBPath;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | XDBPath | IN | Path |
| level | INTEGER) | IN | Number of levels up the hierarchy |

**Returns:** `XDBPath`

## Usage Notes

See Also: XDBPath Type Subprograms for other subprograms in this group See Also: XDBPath Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETPARENTPATH ( path IN XDBPath, level IN INTEGER) RETURN XDBPath; Parameters Table 203-32 GETPARENTPATH Function Parameters Parameter Description path Path level Number of levels up the hierarchy