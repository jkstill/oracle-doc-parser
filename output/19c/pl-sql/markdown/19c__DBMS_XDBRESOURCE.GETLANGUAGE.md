---
id: 19c__DBMS_XDBRESOURCE.GETLANGUAGE
name: DBMS_XDBRESOURCE.GETLANGUAGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETLANGUAGE

Given an XDBResource, this function returns its language.

## Syntax

```sql
DBMS_XDBRESOURCE.GETLANGUAGE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETLANGUAGE ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-18 GETLANGUAGE Function Parameters Parameter Description res XDBResource