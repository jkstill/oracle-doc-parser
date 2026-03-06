---
id: 19c__DBMS_XDBRESOURCE.ISNULL
name: DBMS_XDBRESOURCE.ISNULL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.ISNULL

This function returns TRUE if input resource is NULL .

## Syntax

```sql
DBMS_XDBRESOURCE.ISNULL (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | Input resource |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBRESOURCE.ISNULL ( res IN XDBResource) RETURN BOOLEAN; Parameters Table 200-42 ISNULL Function Parameters Parameter Description res Input resource