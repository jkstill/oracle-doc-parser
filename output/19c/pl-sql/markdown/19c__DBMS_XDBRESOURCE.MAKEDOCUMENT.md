---
id: 19c__DBMS_XDBRESOURCE.MAKEDOCUMENT
name: DBMS_XDBRESOURCE.MAKEDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBRESOURCE
tags: [dbms_xdbresource]
source_file: DBMS_XDBRESOURCE.html
---

# DBMS_XDBRESOURCE.MAKEDOCUMENT

This function converts the XDBResource to a DOMDocument which can be operated on using the XMLDOM interface.

## Syntax

```sql
DBMS_XDBRESOURCE.MAKEDOCUMENT (
   res   IN    XDBResource) 
 RETURN DBMS_XMLDOM.DOMDocument;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res | XDBResource) | IN | XDBResource |

**Returns:** `DBMS_XMLDOM.DOMDocument`

## Usage Notes

See Also: The DBMS_XMLDOM package See Also: The DBMS_XMLDOM package Syntax DBMS_XDBRESOURCE.MAKEDOCUMENT ( res IN XDBResource) RETURN DBMS_XMLDOM.DOMDocument; Parameters Table 200-43 MAKEDOCUMENT Function Parameters Parameter Description res XDBResource