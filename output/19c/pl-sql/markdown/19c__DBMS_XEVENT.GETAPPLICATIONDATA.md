---
id: 19c__DBMS_XEVENT.GETAPPLICATIONDATA
name: DBMS_XEVENT.GETAPPLICATIONDATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETAPPLICATIONDATA

This function returns the <applicationData> element extracted from the resource configuration that defines the invoking handler.

## Syntax

```sql
DBMS_XEVENT.GETAPPLICATIONDATA (
    ev   IN   XDBRepositoryEvent) 
  RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `XMLType`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETAPPLICATIONDATA ( ev IN XDBRepositoryEvent) RETURN XMLType; Parameters Table 203-10 GETAPPLICATIONDATA Function Parameters Parameter Description ev Event of XDBRepositoryEvent type