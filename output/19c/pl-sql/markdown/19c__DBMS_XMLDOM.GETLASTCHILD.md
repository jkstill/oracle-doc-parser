---
id: 19c__DBMS_XMLDOM.GETLASTCHILD
name: DBMS_XMLDOM.GETLASTCHILD
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETLASTCHILD

This function retrieves the last child of this node. If there is no such node, this returns NULL .

## Syntax

```sql
DBMS_XMLDOM.GETLASTCHILD(
   n     IN   DOMNODE)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETLASTCHILD( n IN DOMNODE) RETURN DOMNODE; Parameters Table 204-57 GETLASTCHILD Function Parameters Parameter Description n DOMNODE