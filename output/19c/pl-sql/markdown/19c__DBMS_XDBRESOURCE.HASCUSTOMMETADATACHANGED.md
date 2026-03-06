---
id: 19c__DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED
name: DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED

This function checks whether the custom-metadata for a given resource has changed.

## Syntax

```sql
DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-33 HASCUSTOMMETADATACHANGED Function Parameters Parameter Description res XDBResource