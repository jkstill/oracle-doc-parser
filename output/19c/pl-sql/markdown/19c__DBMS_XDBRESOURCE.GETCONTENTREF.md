---
id: 19c__DBMS_XDBRESOURCE.GETCONTENTREF
name: DBMS_XDBRESOURCE.GETCONTENTREF
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCONTENTREF

This function returns the contents of the resource as an XMLTypeRef .

## Syntax

```sql
DBMS_XDBRESOURCE.GETCONTENTREF (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCONTENTREF ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-10 GETCONTENTREF Function Parameters Parameter Description res XDBResource