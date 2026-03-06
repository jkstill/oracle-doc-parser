---
id: 19c__DBMS_XMLDOM.MAKENOTATION
name: DBMS_XMLDOM.MAKENOTATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKENOTATION

This function casts a specified DOMNODE to a DOMNOTATION , and returns the DOMNOTATION .

## Syntax

```sql
DBMS_XMLDOM.MAKENOTATION(
   n       IN     DOMNODE)
 RETURN DOMNOTATION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMNOTATION`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKENOTATION( n IN DOMNODE) RETURN DOMNOTATION; Parameters Table 204-107 MAKENOTATION Function Parameters Parameter Description n DOMNODE to cast