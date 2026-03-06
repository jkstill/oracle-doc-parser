---
id: 19c__DBMS_XDBRESOURCE.HASCREATORCHANGED
name: DBMS_XDBRESOURCE.HASCREATORCHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASCREATORCHANGED

This function returns TRUE if the creator of the given resource has changed, FALSE otherwise

## Syntax

```sql
DBMS_XDBRESOURCE.HASCREATORCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASCREATORCHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-32 HASCREATORCHANGED Function Parameters Parameter Description res XDBResource