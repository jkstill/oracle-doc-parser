---
id: 19c__DBMS_XEVENT.GETEVENT
name: DBMS_XEVENT.GETEVENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETEVENT

This function returns the name of the user executing the operation that triggers the event.

## Syntax

```sql
DBMS_XEVENT.GETEVENT (
    ev   IN   XDBEvent) 
  RETURN XDBEventID;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBEvent) | IN | Event of XDBEvent type |

**Returns:** `XDBEventID`

## Usage Notes

See Also: XDBEvent Type Subprograms for other subprograms in this group See Also: XDBEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETEVENT ( ev IN XDBEvent) RETURN XDBEventID; Parameters Table 203-13 GETEVENT Function Parameters Parameter Description ev Event of XDBEvent type