---
id: 19c__DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED
name: DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED

This function returns TRUE if the modification date of the given resource has changed, FALSE otherwise

## Syntax

```sql
DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-37 HASMODIFICATIONDATECHANGED Function Parameters Parameter Description res XDBResource