---
id: 19c__DBMS_XMLDOM.APPENDCHILD
name: DBMS_XMLDOM.APPENDCHILD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.APPENDCHILD

This function adds the node newchild to the end of the list of children of this node, and returns the newly added node. If the newchild is already in the tree, it is first removed.

## Syntax

```sql
DBMS_XMLDOM.APPENDCHILD(
   n          IN    DOMNode,
   newchild   IN    DOMNode)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNode | IN | DOMNode |
| newchild | DOMNode) | IN | The child to be appended to the list of children of node n |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.APPENDCHILD( n IN DOMNode, newchild IN DOMNode) RETURN DOMNODE; Parameters Table 204-23 APPENDCHILD Function Parameters Parameter Description n DOMNode newchild The child to be appended to the list of children of node n