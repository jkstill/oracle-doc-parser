---
id: 19c__DBMS_XMLDOM.MAKECHARACTERDATA
name: DBMS_XMLDOM.MAKECHARACTERDATA
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKECHARACTERDATA

This function casts a specified DOMNODE to a DOMCHARACTERDATA , and returns the DOMCHARACTERDATA .

## Syntax

```sql
DBMS_XMLDOM.MAKECHARACTERDATA(
   n       IN     DOMNode)
 RETURN DOMCharacterData;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNode) | IN | DOMNODE to cast |

**Returns:** `DOMCharacterData`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKECHARACTERDATA( n IN DOMNode) RETURN DOMCharacterData; Parameters Table 204-98 MAKECHARACTERDATA Function Parameters Parameter Description n DOMNODE to cast