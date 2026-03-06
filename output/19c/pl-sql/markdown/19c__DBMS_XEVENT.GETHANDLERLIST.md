---
id: 19c__DBMS_XEVENT.GETHANDLERLIST
name: DBMS_XEVENT.GETHANDLERLIST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETHANDLERLIST

This function returns an XDBHandlerList object containing the list of handlers that will be executed after the currently executing handler.

## Syntax

```sql
DBMS_XEVENT.GETHANDLERLIST (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBHandlerList;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBHandlerList`

## Usage Notes

The current handler can then filter out some of the subsequent handlers if necessary, subject to security checks. An insufficient privilege exception is raised if the executing user does not have the required access privilege to any of the resource configuration associating with a handler in the list. See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETHANDLERLIST ( ev IN XDBRepositoryEvent) RETURN XDBHandlerList; Parameters Table 203-15 GETHANDLERLIST Function Parameters Parameter Description ev Event of XDBRepositoryEvent type