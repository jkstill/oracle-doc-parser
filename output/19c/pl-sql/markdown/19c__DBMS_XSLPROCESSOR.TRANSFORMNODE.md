---
id: 19c__DBMS_XSLPROCESSOR.TRANSFORMNODE
name: DBMS_XSLPROCESSOR.TRANSFORMNODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.TRANSFORMNODE

This function transforms a node in a DOM tree using the given stylesheet, and returns the result of the transformation as a DOMDocumentFragment .

## Syntax

```sql
DBMS_XSLPROCESSOR.TRANSFORMNODE(
   n    IN  DOMNODE,
   ss   IN  Stylesheet)
 RETURN DOMDocumentFragment;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNode to transform |
| ss | Stylesheet) | IN | Stylesheet to use |

**Returns:** `DOMDocumentFragment`

## Usage Notes

Syntax DBMS_XSLPROCESSOR.TRANSFORMNODE( n IN DOMNODE, ss IN Stylesheet) RETURN DOMDocumentFragment; Parameters Table 216-15 TRANSFORMNODE Function Parameters Parameter Description n DOMNode to transform ss Stylesheet to use