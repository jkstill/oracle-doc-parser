---
id: 19c__DBMS_XDBRESOURCE.GETCONTENTXML
name: DBMS_XDBRESOURCE.GETCONTENTXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCONTENTXML

This function returns the contents of the resource as an XMLTypeRef .

## Syntax

```sql
DBMS_XDBRESOURCE.GETCONTENTXML (
   res   IN    XDBResource) 
 RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `XMLType`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCONTENTXML ( res IN XDBResource) RETURN XMLType; Parameters Table 200-12 GETCONTENTXML Function Parameters Parameter Description res XDBResource