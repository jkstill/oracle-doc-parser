---
id: 19c__DBMS_XEVENT.GETCURRENTUSER
name: DBMS_XEVENT.GETCURRENTUSER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETCURRENTUSER

This function returns the name of the user executing the operation that triggers the event.

## Syntax

```sql
DBMS_XEVENT.GETCURRENTUSER (
    ev   IN   XDBEvent) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBEvent) | IN | Event of XDBEvent type |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBEvent Type Subprograms for other subprograms in this group See Also: XDBEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETCURRENTUSER ( ev IN XDBEvent) RETURN VARCHAR2; Parameters Table 203-12 GETCURRENTUSER Function Parameters Parameter Description ev Event of XDBEvent type