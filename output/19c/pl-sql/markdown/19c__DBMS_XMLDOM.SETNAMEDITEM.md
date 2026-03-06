---
id: 19c__DBMS_XMLDOM.SETNAMEDITEM
name: DBMS_XMLDOM.SETNAMEDITEM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETNAMEDITEM

This function adds a node using its NodeName attribute.

## Syntax

```sql
DBMS_XMLDOM.SETNAMEDITEM(
   nnm     IN     DOMNAMEDNODEMAP,
   arg     IN     DOMNODE)
 RETURN DOMNode;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nnm | DOMNAMEDNODEMAP | IN | DOMNAMEDNODEMAP |
| arg | DOMNODE) | IN | The Node to be added using its NodeName attribute |
| ns |  |  | Namespace |

**Returns:** `DOMNode`

## Usage Notes

If a node with that name is already present in this map, it is replaced by the new one. The old node is returned on replacement; if no replacement is made, NULL is returned. As the NodeName attribute is used to derive the name under which the node must be stored, multiple nodes of certain types, those that have a "special" string value, cannot be stored because the names would clash. This is seen as preferable to allowing nodes to be aliased. See Also: DOMNamedNodeMap Subprograms See Also: DOMNamedNodeMap Subprograms Syntax Adds a node using its NodeName attribute: DBMS_XMLDOM.SETNAMEDITEM( nnm IN DOMNAMEDNODEMAP, arg IN DOMNODE) RETURN DOMNode; Adds a node using its NodeName attribute and namespace URI: DBMS_XMLDOM.SETNAMEDITEM( nnm IN DOMNAMEDNODEMAP, arg IN DOMNODE, ns IN VARCHAR2) RETURN DOMNode; Parameters Table 204-124 SETNAMEDITEM Function Parameters Parameter Description nnm DOMNAMEDNODEMAP arg The Node to be added using its NodeName attribute ns Namespace