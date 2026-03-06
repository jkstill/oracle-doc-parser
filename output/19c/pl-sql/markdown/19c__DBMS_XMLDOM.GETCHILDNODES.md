---
id: 19c__DBMS_XMLDOM.GETCHILDNODES
name: DBMS_XMLDOM.GETCHILDNODES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETCHILDNODES

This function retrieves a DOMNODELIST that contains all children of this node. If there are no children, this is a DOMNODELIST containing no nodes.

## Syntax

```sql
DBMS_XMLDOM.GETCHILDNODES(
   n      IN    DOMNode)
 RETURN DOMNodeList;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNode) | IN | DOMNODE |

**Returns:** `DOMNodeList`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETCHILDNODES( n IN DOMNode) RETURN DOMNodeList; Parameters Table 204-47 GETCHILDNODES Function Parameters Parameter Description n DOMNODE