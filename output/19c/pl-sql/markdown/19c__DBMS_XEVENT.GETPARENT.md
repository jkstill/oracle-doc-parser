---
id: 19c__DBMS_XEVENT.GETPARENT
name: DBMS_XEVENT.GETPARENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETPARENT

This function returns the resource object corresponding to a parent folder of the target resource. Note that this could be any folder that contains a link to the target resource. This is a read-only object, and consequently none of the modifier methods will work on this object. For a link* or unlink* event, this method returns the link's parent folder.

## Syntax

```sql
DBMS_XEVENT.GETPARENT (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBResource;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBResource`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETPARENT ( ev IN XDBRepositoryEvent) RETURN XDBResource; Parameters Table 203-29 GETPARENT Function Parameters Parameter Description ev Event of XDBRepositoryEvent type