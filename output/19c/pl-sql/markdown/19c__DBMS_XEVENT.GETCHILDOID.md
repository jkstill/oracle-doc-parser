---
id: 19c__DBMS_XEVENT.GETCHILDOID
name: DBMS_XEVENT.GETCHILDOID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETCHILDOID

This function returns the OID of the resource to which the link is pointing.

## Syntax

```sql
DBMS_XEVENT.GETCHILDOID (
    link   IN   XDBLink) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| link | XDBLink) | IN | Link |

**Returns:** `RAW`

## Usage Notes

See Also: XDBLink Type Subprograms for other subprograms in this group See Also: XDBLink Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETCHILDOID ( link IN XDBLink) RETURN RAW; Parameters Table 203-11 GETCHILDOID Function Parameters Parameter Description link Link