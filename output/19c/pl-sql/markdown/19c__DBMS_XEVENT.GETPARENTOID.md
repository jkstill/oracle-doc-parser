---
id: 19c__DBMS_XEVENT.GETPARENTOID
name: DBMS_XEVENT.GETPARENTOID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETPARENTOID

This function returns the link's parent folder's OID.

## Syntax

```sql
DBMS_XEVENT.GETPARENTOID (
    link   IN   XDBLink) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| link | XDBLink) | IN | Link |

**Returns:** `RAW`

## Usage Notes

See Also: XDBLink Type Subprograms for other subprograms in this group See Also: XDBLink Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETPARENTOID ( link IN XDBLink) RETURN RAW; Parameters Table 203-31 GETPARENTOID Function Parameters Parameter Description link Link