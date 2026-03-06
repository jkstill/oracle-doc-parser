---
id: 19c__DBMS_XDBRESOURCE.GETOWNER
name: DBMS_XDBRESOURCE.GETOWNER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETOWNER

Given an XDBResource, this function returns its owner.

## Syntax

```sql
DBMS_XDBRESOURCE.GETOWNER (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETOWNER ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-21 GETOWNER Function Parameters Parameter Description res XDBResource