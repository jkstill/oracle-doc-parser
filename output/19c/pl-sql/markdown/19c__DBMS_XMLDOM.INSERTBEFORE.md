---
id: 19c__DBMS_XMLDOM.INSERTBEFORE
name: DBMS_XMLDOM.INSERTBEFORE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.INSERTBEFORE

This function inserts the node newchild before the existing child node refchild . If refchild is NULL , insert newchild at the end of the list of children.

## Syntax

```sql
DBMS_XMLDOM.INSERTBEFORE(
   n          IN     DOMNODE,
   newchild   IN     DOMNODE,
   refchild   IN     DOMNODE)
  RETURN DOMNode;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| newChild | DOMNODE | IN | The child to be inserted in the DOMNODE |
| refChild | DOMNODE) | IN | The reference node before which the newchild is to be inserted |

**Returns:** `DOMNode`

## Usage Notes

If newchild is a DOCUMENTFRAGMENT object, all of its children are inserted, in the same order, before refchild . If the newchild is already in the tree, it is first removed. See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.INSERTBEFORE( n IN DOMNODE, newchild IN DOMNODE, refchild IN DOMNODE) RETURN DOMNode; Parameters Table 204-92 INSERTBEFORE Function Parameters Parameter Description n DOMNODE newChild The child to be inserted in the DOMNODE refChild The reference node before which the newchild is to be inserted