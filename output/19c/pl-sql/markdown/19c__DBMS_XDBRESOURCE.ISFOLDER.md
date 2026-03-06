---
id: 19c__DBMS_XDBRESOURCE.ISFOLDER
name: DBMS_XDBRESOURCE.ISFOLDER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.ISFOLDER

This function returns TRUE if the given resource is a folder, FALSE otherwise.

## Syntax

```sql
DBMS_XDBRESOURCE.ISFOLDER (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.ISFOLDER ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-41 ISFOLDER Function Parameters Parameter Description res XDBResource