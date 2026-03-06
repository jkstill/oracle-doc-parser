---
id: 19c__DBMS_XDBRESOURCE.GETCREATIONDATE
name: DBMS_XDBRESOURCE.GETCREATIONDATE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCREATIONDATE

Given an XDBResource, this function returns its creation date.

## Syntax

```sql
DBMS_XDBRESOURCE.GETCREATIONDATE (
   res   IN    XDBResource) 
 RETURN TIMESTAMP;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `TIMESTAMP`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCREATIONDATE ( res IN XDBResource) RETURN TIMESTAMP; Parameters Table 200-14 GETCREATIONDATE Function Parameters Parameter Description res XDBResource