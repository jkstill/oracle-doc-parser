---
id: 19c__DBMS_XMLDOM.GETNEXTSIBLING
name: DBMS_XMLDOM.GETNEXTSIBLING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNEXTSIBLING

This function retrieves the node immediately following this node. If there is no such node, this returns NULL .

## Syntax

```sql
DBMS_XMLDOM.GETNEXTSIBLING(
   n       IN     DOMNODE)
 RETURN DOMNode;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |

**Returns:** `DOMNode`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETNEXTSIBLING( n IN DOMNODE) RETURN DOMNode; Parameters Table 204-63 GETNEXTSIBLING Function Parameters Parameter Description n DOMNODE