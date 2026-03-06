---
id: 19c__DBMS_XEVENT.GETRESOURCE
name: DBMS_XEVENT.GETRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETRESOURCE

This function returns an XDBResource object that provides methods to access and modify the contents and metadata of the target resource. This object reflects any changes made by previous handlers to the resource.

## Syntax

```sql
DBMS_XEVENT.GETRESOURCE (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBResource;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBResource`

## Usage Notes

The modifier methods will work only in the pre-create and pre-update event handlers. For a link* or unlink* event, this method returns the resource that the link is pointing to. For a create event, this method returns the resource that is being created. See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETRESOURCE ( ev IN XDBRepositoryEvent) RETURN XDBResource; Parameters Table 203-34 GETRESOURCE Function Parameters Parameter Description ev Event of XDBRepositoryEvent type