---
id: 19c__DBMS_XSLPROCESSOR.SELECTNODES
name: DBMS_XSLPROCESSOR.SELECTNODES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.SELECTNODES

This function selects nodes which match the supplied path expression from a DOM tree, and returns the result of the selection.

## Syntax

```sql
DBMS_XSLPROCESSOR.SELECTNODES( 
   n           IN   DBMS_XMLDOM.DOMNODE,
   pattern     IN   VARCHAR2,
   namespace   IN VARCHAR2 := NULL)
 RETURN DBMS_XMLDOM.DOMNODELIST;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DBMS_XMLDOM.DOMNODE | IN | Root DOMNode of the tree |
| pattern | VARCHAR2 | IN | Pattern to use |
| namespace | VARCHAR2 | IN | Namespace declared |

**Returns:** `DBMS_XMLDOM.DOMNODELIST`

## Usage Notes

Syntax DBMS_XSLPROCESSOR.SELECTNODES( n IN DBMS_XMLDOM.DOMNODE, pattern IN VARCHAR2, namespace IN VARCHAR2 := NULL) RETURN DBMS_XMLDOM.DOMNODELIST; Parameters Table 216-10 SELECTNODES Function Parameters Parameter Description n Root DOMNode of the tree pattern Pattern to use namespace Namespace declared