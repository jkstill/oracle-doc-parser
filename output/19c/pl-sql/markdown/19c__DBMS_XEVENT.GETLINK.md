---
id: 19c__DBMS_XEVENT.GETLINK
name: DBMS_XEVENT.GETLINK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETLINK

This function returns an XDBLink object for the target resource.

## Syntax

```sql
DBMS_XEVENT.GETLINK (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBLink;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBLink`

## Usage Notes

For a link* or unlink* event, this will be the link involved in the operation. For other events, an error is returned. Using this object the handler can access link properties, such as, ParentName , ParentOID , ChildOID and LinkName . See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETLINK ( ev IN XDBRepositoryEvent) RETURN XDBLink; Parameters Table 203-18 GETLINK Function Parameters Parameter Description ev Event of XDBRepositoryEvent type