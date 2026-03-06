---
id: 19c__DBMS_XDBRESOURCE.GETCREATOR
name: DBMS_XDBRESOURCE.GETCREATOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCREATOR

Given an XDBResource, this function returns its creator.

## Syntax

```sql
DBMS_XDBRESOURCE.GETCREATOR (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCREATOR ( res IN XDBResource) RETURN VARCHAR2; Parameters Table 200-15 GETCREATOR Function Parameters Parameter Description res XDBResource