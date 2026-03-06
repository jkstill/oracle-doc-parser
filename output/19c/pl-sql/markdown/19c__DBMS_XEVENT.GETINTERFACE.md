---
id: 19c__DBMS_XEVENT.GETINTERFACE
name: DBMS_XEVENT.GETINTERFACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETINTERFACE

This function returns the top-level interface used to initiate the operation that triggered the event. This could be HTTP, FTP or SQL.

## Syntax

```sql
DBMS_XEVENT.GETINTERFACE (
    ev   IN   XDBRepositoryEvent) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETINTERFACE ( ev IN XDBRepositoryEvent) RETURN VARCHAR2; Parameters Table 203-16 GETINTERFACE Function Parameters Parameter Description ev Event of XDBRepositoryEvent type