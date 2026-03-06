---
id: 19c__DBMS_XMLDOM.REMOVECHILD
name: DBMS_XMLDOM.REMOVECHILD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.REMOVECHILD

This function removes the child node indicated by oldchild from the list of children, and returns it.

## Syntax

```sql
DBMS_XMLDOM.REMOVECHILD(
   n          IN     DOMNode,
   oldchild   IN     DOMNode)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNode | IN | DOMNODE |
| oldCHild | DOMNode) | IN | The child of the node n to be removed |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.REMOVECHILD( n IN DOMNode, oldchild IN DOMNode) RETURN DOMNODE; Parameters Table 204-114 REMOVECHILD Function Parameters Parameter Description n DOMNODE oldCHild The child of the node n to be removed