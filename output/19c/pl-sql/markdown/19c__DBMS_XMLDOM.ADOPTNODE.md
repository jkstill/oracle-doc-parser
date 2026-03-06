---
id: 19c__DBMS_XMLDOM.ADOPTNODE
name: DBMS_XMLDOM.ADOPTNODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.ADOPTNODE

This function adopts a node from another document, and returns this new node.

## Syntax

```sql
DBMS_XMLDOM.ADOPTNODE(
   doc            IN   DOMDocument,
   importedNode   IN   DOMNode)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDocument | IN | Document that is adopting the node |
| importedNode | DOMNode) | IN | Node to adopt |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms for other subprograms in this group See Also: DOMNode Subprograms for other subprograms in this group Syntax DBMS_XMLDOM.ADOPTNODE( doc IN DOMDocument, importedNode IN DOMNode) RETURN DOMNODE; Parameters Table 204-22 ADOPTNODE Function Parameters Parameter Description doc Document that is adopting the node importedNode Node to adopt Usage Notes Note that the ADOPTNODE Function removes the node from the source document while the IMPORTNODE Function clones the node in the source document.