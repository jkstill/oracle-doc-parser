---
id: 19c__DBMS_XDBRESOURCE.GETREFCOUNT
name: DBMS_XDBRESOURCE.GETREFCOUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETREFCOUNT

Given an XDBResource, this function returns its reference count.

## Syntax

```sql
DBMS_XDBRESOURCE.GETREFCOUNT (
   res   IN    XDBResource) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETREFCOUNT ( res IN XDBResource) RETURN PLS_INTEGER; Parameters Table 200-22 GETREFCOUNT Function Parameters Parameter Description res XDBResource