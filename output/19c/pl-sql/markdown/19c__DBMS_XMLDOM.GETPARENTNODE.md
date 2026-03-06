---
id: 19c__DBMS_XMLDOM.GETPARENTNODE
name: DBMS_XMLDOM.GETPARENTNODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETPARENTNODE

This function retrieves the parent of this node. All nodes, except Attr , Document , DocumentFragment , Entity , and Notation may have a parent. However, if a node has just been created and not yet added to the tree, or if it has been removed from the tree, this is NULL .

## Syntax

```sql
DBMS_XMLDOM.GETPARENTNODE(
   n       IN     DOMNODE)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETPARENTNODE( n IN DOMNODE) RETURN DOMNODE; Parameters Table 204-74 GETPARENTNODE Function Parameters Parameter Description n DOMNODE