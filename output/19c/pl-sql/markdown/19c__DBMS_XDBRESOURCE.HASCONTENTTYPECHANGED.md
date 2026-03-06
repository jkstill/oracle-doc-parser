---
id: 19c__DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED
name: DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED

This function returns TRUE if the content-type of the given resource has changed, FALSE otherwise

## Syntax

```sql
DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-30 HASCONTENTTYPECHANGED Function Parameters Parameter Description res XDBResource