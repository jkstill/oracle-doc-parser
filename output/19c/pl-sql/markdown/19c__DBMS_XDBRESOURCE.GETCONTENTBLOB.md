---
id: 19c__DBMS_XDBRESOURCE.GETCONTENTBLOB
name: DBMS_XDBRESOURCE.GETCONTENTBLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.GETCONTENTBLOB

This function returns the contents of the resource as a BLOB .

## Syntax

```sql
DBMS_XDBRESOURCE.GETCONTENTBLOB (
   res    IN     XDBResource,
   csid   OUT    PLS_INTEGER) 
 RETURN BLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource | IN | XDBResource |
| csid | PLS_INTEGER) | OUT | Character set ID of the BLOB returned |

**Returns:** `BLOB`

## Usage Notes

Syntax DBMS_XDBRESOURCE.GETCONTENTBLOB ( res IN XDBResource, csid OUT PLS_INTEGER) RETURN BLOB; Parameters Table 200-8 GETCONTENTBLOB Function Parameters Parameter Description res XDBResource csid Character set ID of the BLOB returned