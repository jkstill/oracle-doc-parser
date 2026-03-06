---
id: 19c__DBMS_XMLDOM.MAKEDOCUMENTFRAGMENT
name: DBMS_XMLDOM.MAKEDOCUMENTFRAGMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEDOCUMENTFRAGMENT

This function casts a specified DOMNODE to a DOMDOCUMENTFRAGMENT , and returns the DOMDOCUMENTFRAGMENT .

## Syntax

```sql
DBMS_XMLDOM.MAKEDOCUMENTFRAGMENT(
   n       IN     DOMNODE)
 RETURN DOMDOCUMENTFRAGMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMDOCUMENTFRAGMENT`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEDOCUMENTFRAGMENT( n IN DOMNODE) RETURN DOMDOCUMENTFRAGMENT; Parameters Table 204-101 MAKEDOCUMENTFRAGMENT Function Parameters Parameter Description n DOMNODE to cast