---
id: 19c__DBMS_XMLDOM.MAKECDATASECTION
name: DBMS_XMLDOM.MAKECDATASECTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKECDATASECTION

This function casts a specified DOMNODE to a DOMCDATASECTION .

## Syntax

```sql
DBMS_XMLDOM.MAKECDATASECTION(
   n       IN     DOMNODE)
 RETURN DOMCDATASECTION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMCDATASECTION`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKECDATASECTION( n IN DOMNODE) RETURN DOMCDATASECTION; Parameters Table 204-97 MAKECDATASECTION Function Parameters Parameter Description n DOMNODE to cast