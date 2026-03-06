---
id: 19c__DBMS_XEVENT.GETXDBEVENT
name: DBMS_XEVENT.GETXDBEVENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETXDBEVENT

This function converts an XDBRepositoryEvent object to an XDBEvent type.

## Syntax

```sql
DBMS_XEVENT.GETXDBETEVENT (
    ev   IN   XDBRepositoryEvent) 
  RETURN XDBEvent;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XDBEvent`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETXDBETEVENT ( ev IN XDBRepositoryEvent) RETURN XDBEvent; Parameters Table 203-39 GETXDBEVENT Function Parameters Parameter Description ev Event of XDBRepositoryEvent type