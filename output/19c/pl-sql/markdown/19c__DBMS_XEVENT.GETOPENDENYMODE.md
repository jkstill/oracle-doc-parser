---
id: 19c__DBMS_XEVENT.GETOPENDENYMODE
name: DBMS_XEVENT.GETOPENDENYMODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETOPENDENYMODE

This function returns the deny mode for the open operation. It is only valid for the open event.

## Syntax

```sql
DBMS_XEVENT.GETOPENDENYMODE (
    ev   IN   XDBRepositoryEvent) 
  RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `PLS_INTEGER`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETOPENDENYMODE ( ev IN XDBRepositoryEvent) RETURN PLS_INTEGER; Parameters Table 203-26 GETOPENDENYMODE Function Parameters Parameter Description ev Event of XDBRepositoryEvent type Return Values XDBRepositoryEvent . OPEN_DENY_NONE (value 0) XDBRepositoryEvent . OPEN_DENY_READ (value 1) XDBRepositoryEvent . OPEN_DENY_READ_WRITE (value 2)