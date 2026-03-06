---
id: 19c__DBMS_XDBRESOURCE.GETCONTENTVARCHAR2
name: DBMS_XDBRESOURCE.GETCONTENTVARCHAR2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCONTENTVARCHAR2

This function returns the contents of the resource as a string.

## Syntax

```sql
DBMS_XDBRESOURCE.GETCONTENTVARCHAR2 (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCONTENTVARCHAR2 ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-13 GETCONTENTVARCHAR2 Function Parameters Parameter Description res XDBResource