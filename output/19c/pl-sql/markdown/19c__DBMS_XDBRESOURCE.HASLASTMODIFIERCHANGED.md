---
id: 19c__DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED
name: DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED

This function returns TRUE if the last modifier of the given resource has changed, FALSE otherwise

## Syntax

```sql
DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-36 HASLASTMODIFIERCHANGED Function Parameters Parameter Description res XDBResource