---
id: 19c__DBMS_XEVENT.GETPARENTNAME
name: DBMS_XEVENT.GETPARENTNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XEVENT
tags: [dbms_xevent]
source_file: DBMS_XEVENT.html
---

# DBMS_XEVENT.GETPARENTNAME

This function returns the link's parent folder's name.

## Syntax

```sql
DBMS_XEVENT.GETPARENTNAME (
    link   IN   XDBLink) 
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| link | XDBLink) | IN | Link |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: XDBLink Type Subprograms for other subprograms in this group See Also: XDBLink Type Subprograms for other subprograms in this group Syntax DBMS_XEVENT.GETPARENTNAME ( link IN XDBLink) RETURN VARCHAR2; Parameters Table 203-30 GETPARENTNAME Function Parameters Parameter Description link Link