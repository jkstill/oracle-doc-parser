---
id: 19c__DBMS_XDBRESOURCE.GETVERSIONID
name: DBMS_XDBRESOURCE.GETVERSIONID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETVERSIONID

Given an XDBResource, this function returns its version ID.

## Syntax

```sql
DBMS_XDBRESOURCE.GETVERSIONID (
   res   IN    XDBResource) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETVERSIONID ( res IN XDBResource) RETURN PLS_INTEGER; Parameters Table 200-23 GETVERSIONID Function Parameters Parameter Description res XDBResource