---
id: 19c__DBMS_XEVENT.GETOUTPUTSTREAM
name: DBMS_XEVENT.GETOUTPUTSTREAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETOUTPUTSTREAM

This function returns the output BLOB in which the handler can write the rendered data. It is only valid for the render event.

## Syntax

```sql
DBMS_XEVENT.GETOUTPUTSTREAM (
    ev   IN   XDBRepositoryEvent) 
  RETURN BLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ev | XDBRepositoryEvent) | IN | Event of XDBRepositoryEvent type |

**Returns:** `BLOB`

## Usage Notes

See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group See Also: XDBRepositoryEvent Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETOUTPUTSTREAM ( ev IN XDBRepositoryEvent) RETURN BLOB; Parameters Table 203-27 GETOUTPUTSTREAM Function Parameters Parameter Description ev Event of XDBRepositoryEvent type