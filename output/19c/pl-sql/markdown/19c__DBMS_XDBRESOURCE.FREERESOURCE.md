---
id: 19c__DBMS_XDBRESOURCE.FREERESOURCE
name: DBMS_XDBRESOURCE.FREERESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.FREERESOURCE

This procedure frees any memory associated with an XDBResource.

## Syntax

```sql
DBMS_XDBRESOURCE.FREERESOURCE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource to free |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.FREERESOURCE ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-2 FREERESOURCE Procedure Parameters Parameter Description res XDBResource to free