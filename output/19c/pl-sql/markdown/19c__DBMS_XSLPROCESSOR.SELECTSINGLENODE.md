---
id: 19c__DBMS_XSLPROCESSOR.SELECTSINGLENODE
name: DBMS_XSLPROCESSOR.SELECTSINGLENODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.SELECTSINGLENODE

This function selects the first node from the tree that match the supplied path expression, and returns that node.

## Syntax

```sql
DBMS_XSLPROCESSOR.SELECTSINGLENODE(
   n           IN   DBMS_XMLDOM.DOMNODE,
   pattern     IN   VARCHAR2,
   namespace   IN VARCHAR2 := NULL)
 RETURN DBMS_XMLDOM.DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DBMS_XMLDOM.DOMNODE | IN | Root DOMNode of the tree |
| pattern | VARCHAR2 | IN | Pattern to use |
| namespace | VARCHAR2 | IN | Namespace declared |

**Returns:** `DBMS_XMLDOM.DOMNODE`

## Usage Notes

Syntax DBMS_XSLPROCESSOR.SELECTSINGLENODE( n IN DBMS_XMLDOM.DOMNODE, pattern IN VARCHAR2, namespace IN VARCHAR2 := NULL) RETURN DBMS_XMLDOM.DOMNODE; Parameters Table 216-11 SELECTSINGLENODE Function Parameters Parameter Description n Root DOMNode of the tree pattern Pattern to use namespace Namespace declared