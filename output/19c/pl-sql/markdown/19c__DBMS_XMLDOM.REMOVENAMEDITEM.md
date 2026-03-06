---
id: 19c__DBMS_XMLDOM.REMOVENAMEDITEM
name: DBMS_XMLDOM.REMOVENAMEDITEM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.REMOVENAMEDITEM

This function removes a node, specified by name, from the map and returns this node.

## Syntax

```sql
DBMS_XMLDOM.REMOVENAMEDITEM(
   nnm      IN     DOMNamedNodeMap,
   name     IN     VARCHAR2)
 RETURN DOMNode;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nnm | DOMNamedNodeMap | IN | DOMNamedNodeMap |
| name | VARCHAR2) | IN | The name of the item to be removed from the map |
| ns |  |  | Namespace |

**Returns:** `DOMNode`

## Usage Notes

When this map contains the attributes attached to an element, if the removed attribute is known to have a default value, an attribute immediately appears containing the default value as well as the corresponding namespace URI, local name, and prefix when applicable. See Also: DOMNamedNodeMap Subprograms See Also: DOMNamedNodeMap Subprograms Syntax Removes a node specified by name: DBMS_XMLDOM.REMOVENAMEDITEM( nnm IN DOMNamedNodeMap, name IN VARCHAR2) RETURN DOMNode; Removes a node specified by name and namespace URI: DBMS_XMLDOM.REMOVENAMEDITEM( nnm IN DOMNamedNodeMap, name IN VARCHAR2, ns IN VARCHAR2) RETURN DOMNode; Parameters Table 204-115 REMOVENAMEDITEM Function Parameters Parameter Description nnm DOMNamedNodeMap name The name of the item to be removed from the map ns Namespace