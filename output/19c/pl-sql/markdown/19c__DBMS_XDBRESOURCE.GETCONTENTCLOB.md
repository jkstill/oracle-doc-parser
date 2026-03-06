---
id: 19c__DBMS_XDBRESOURCE.GETCONTENTCLOB
name: DBMS_XDBRESOURCE.GETCONTENTCLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCONTENTCLOB

This function returns the contents of the resource as a CLOB .

## Syntax

```sql
DBMS_XDBRESOURCE.GETCONTENTCLOB (
   res   IN    XDBResource) 
 RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCONTENTCLOB ( res IN XDBResource) RETURN CLOB; Parameters Table 200-9 GETCONTENTCLOB Function Parameters Parameter Description res XDBResource