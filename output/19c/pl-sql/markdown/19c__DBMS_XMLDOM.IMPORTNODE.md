---
id: 19c__DBMS_XMLDOM.IMPORTNODE
name: DBMS_XMLDOM.IMPORTNODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.IMPORTNODE

This function imports a node from an external document and returns this new node.

## Syntax

```sql
DBMS_XMLDOM.IMPORTNODE(
   doc            IN  DOMDOCUMENT,
   importedNode   IN  DOMNODE,
   deep           IN  BOOLEAN)
  RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | Document from which the node is imported |
| importedNode | DOMNODE | IN | Node to import |
| deep | BOOLEAN) | IN | Setting for recursive import. If this value is TRUE, the entire subtree of the node will be imported with the node. If this value is FALSE , only the node itself will be imported. |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.IMPORTNODE( doc IN DOMDOCUMENT, importedNode IN DOMNODE, deep IN BOOLEAN) RETURN DOMNODE; Parameters Table 204-91 IMPORTNODE Function Parameters Parameter Description doc Document from which the node is imported importedNode Node to import deep Setting for recursive import. If this value is TRUE, the entire subtree of the node will be imported with the node. If this value is FALSE , only the node itself will be imported. Usage Notes Note that the ADOPTNODE Function removes the node from the source document while the IMPORTNODE Function clones the node in the source document.