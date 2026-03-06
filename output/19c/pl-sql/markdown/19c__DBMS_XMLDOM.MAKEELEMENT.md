---
id: 19c__DBMS_XMLDOM.MAKEELEMENT
name: DBMS_XMLDOM.MAKEELEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEELEMENT

This function casts a specified DOMNODE to a DOMELEMENT , and returns the DOMELEMENT .

## Syntax

```sql
DBMS_XMLDOM.MAKEELEMENT(
   n       IN     DOMNODE)
 RETURN DOMELEMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMELEMENT`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEELEMENT( n IN DOMNODE) RETURN DOMELEMENT; Parameters Table 204-103 MAKEELEMENT Function Parameters Parameter Description n DOMNODE to cast