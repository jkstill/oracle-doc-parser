---
id: 19c__DBMS_XDBRESOURCE.HASLANGUAGECHANGED
name: DBMS_XDBRESOURCE.HASLANGUAGECHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASLANGUAGECHANGED

This function returns TRUE if the language of the given resource has changed, FALSE otherwise.

## Syntax

```sql
DBMS_XDBRESOURCE.HASLANGUAGECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASLANGUAGECHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-35 HASLANGUAGECHANGED Function Parameters Parameter Description res XDBResource