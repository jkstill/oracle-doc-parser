---
id: 19c__DBMS_XEVENT.GETOPENACCESSMODE
name: DBMS_XEVENT.GETOPENACCESSMODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETOPENACCESSMODE

This function returns the access mode for the open operation.

## Syntax

```sql
DBMS_XEVENT.GETOPENACCESSMODE (
    ev   IN   XDBRepositoryEvent) 
  RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `PLS_INTEGER`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETOPENACCESSMODE ( ev IN XDBRepositoryEvent) RETURN PLS_INTEGER; Parameters Table 203-25 GETOPENACCESSMODE Function Parameters Parameter Description ev Event of XDBRepositoryEvent type Return Values XDBRepositoryEvent . OPEN_ACCESS_READ (value 1) XDBRepositoryEvent . OPEN_ACCESS_WRITE (value 2) XDBRepositoryEvent . OPEN_ACCESS_READ_WRITE (value 3)