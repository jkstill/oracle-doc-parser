---
id: 19c__DBMS_XDBRESOURCE.HASOWNERCHANGED
name: DBMS_XDBRESOURCE.HASOWNERCHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASOWNERCHANGED

This function returns TRUE if the owner of the given resource has changed, FALSE otherwise.

## Syntax

```sql
DBMS_XDBRESOURCE.HASOWNERCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASOWNERCHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-38 HASOWNERCHANGED Function Parameters Parameter Description res XDBResource