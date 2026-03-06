---
id: 19c__DBMS_XEVENT.GETLOCK
name: DBMS_XEVENT.GETLOCK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETLOCK

This function returns the lock object corresponding to the current operation.I t is only valid for lock and unlock events.

## Syntax

```sql
DBMS_XEVENT.GETLOCK  (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBLock;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBLock`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETLOCK ( ev IN XDBRepositoryEvent) RETURN XDBLock; Parameters Table 203-20 GETLOCK Function Parameters Parameter Description ev Event of XDBRepositoryEvent type