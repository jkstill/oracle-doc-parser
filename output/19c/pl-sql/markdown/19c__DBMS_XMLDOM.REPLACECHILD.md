---
id: 19c__DBMS_XMLDOM.REPLACECHILD
name: DBMS_XMLDOM.REPLACECHILD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.REPLACECHILD

This function replaces the child node oldchild with newchild in the list of children, and returns the oldchild node.

## Syntax

```sql
DBMS_XMLDOM.REPLACECHILD(
   n           IN     DOMNode,
   newchild    IN     DOMNode,
   oldchild    IN     DOMNode)
 RETURN DOMNode;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNode | IN | DOMNode |
| newchild | DOMNode | IN | The new child which is to replace the old child |
| oldchild | DOMNode) | IN | The child of the node n which is to be replaced |

**Returns:** `DOMNode`

## Usage Notes

If newchild is a DocumentFragment object, oldchild is replaced by all of the DocumentFragment children, which are inserted in the same order. If the newchild is already in the tree, it is first removed. See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.REPLACECHILD( n IN DOMNode, newchild IN DOMNode, oldchild IN DOMNode) RETURN DOMNode; Parameters Table 204-116 REPLACECHILD Function Parameters Parameter Description n DOMNode newchild The new child which is to replace the old child oldchild The child of the node n which is to be replaced