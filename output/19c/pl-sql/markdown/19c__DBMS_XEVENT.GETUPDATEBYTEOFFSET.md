---
id: 19c__DBMS_XEVENT.GETUPDATEBYTEOFFSET
name: DBMS_XEVENT.GETUPDATEBYTEOFFSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETUPDATEBYTEOFFSET

If the current operation is a byte-range write, the GETUPDATEBYTEOFFSET function returns the byte offset at which the range begins. It is only valid for the inconsistent-update event.

## Syntax

```sql
DBMS_XEVENT.GETUPDATEBYTEOFFSET (
    ev   IN   XDBRepositoryEvent) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `NUMBER`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETUPDATEBYTEOFFSET ( ev IN XDBRepositoryEvent) RETURN NUMBER; Parameters Table 203-38 GETUPDATEBYTEOFFSET Function Parameters Parameter Description ev Event of XDBRepositoryEvent type