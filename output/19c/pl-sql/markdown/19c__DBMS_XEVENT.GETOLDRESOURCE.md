---
id: 19c__DBMS_XEVENT.GETOLDRESOURCE
name: DBMS_XEVENT.GETOLDRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETOLDRESOURCE

This function returns the original XDBResource object before the operation was executed.

## Syntax

```sql
DBMS_XEVENT.GETOLDRESOURCE (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBResource;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBResource`

## Usage Notes

This method applies only to update event. For other events, an error is returned. This is a read-only object, and consequently none of the modifier methods will work on this object. See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETOLDRESOURCE ( ev IN XDBRepositoryEvent) RETURN XDBResource; Parameters Table 203-24 GETOLDRESOURCE Function Parameters Parameter Description ev Event of XDBRepositoryEvent type