---
id: 19c__DBMS_XMLDOM.MAKEDOCUMENTTYPE
name: DBMS_XMLDOM.MAKEDOCUMENTTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEDOCUMENTTYPE

This function casts a specified DOMNODE to a DOMDOCUMENTTYPE and returns the DOMDOCUMENTTYPE .

## Syntax

```sql
DBMS_XMLDOM.MAKEDOCUMENTTYPE(
   n       IN     DOMNODE)
 RETURN DOMDOCUMENTTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast. |

**Returns:** `DOMDOCUMENTTYPE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEDOCUMENTTYPE( n IN DOMNODE) RETURN DOMDOCUMENTTYPE; Parameters Table 204-102 MAKEDOCUMENTTYPE Function Parameters Parameter Description n DOMNODE to cast.