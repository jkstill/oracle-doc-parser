---
id: 19c__DBMS_XMLDOM.MAKEDOCUMENT
name: DBMS_XMLDOM.MAKEDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEDOCUMENT

This function casts a specified DOMNODE to a DOMDOCUMENT , and returns the DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.MAKEDOCUMENT(
   n       IN     DOMNODE)
 RETURN DOMDocument;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMDocument`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEDOCUMENT( n IN DOMNODE) RETURN DOMDocument; Parameters Table 204-100 MAKEDOCUMENT Function Parameters Parameter Description n DOMNODE to cast