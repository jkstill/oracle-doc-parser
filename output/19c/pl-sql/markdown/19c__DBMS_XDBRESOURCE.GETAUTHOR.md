---
id: 19c__DBMS_XDBRESOURCE.GETAUTHOR
name: DBMS_XDBRESOURCE.GETAUTHOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETAUTHOR

Given an XDBResource, this function returns its author.

## Syntax

```sql
DBMS_XDBRESOURCE.GETAUTHOR (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETAUTHOR ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-5 GETAUTHOR Function Parameters Parameter Description res XDBResource