---
id: 19c__DBMS_XMLPARSER.GETDOCUMENT
name: DBMS_XMLPARSER.GETDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.GETDOCUMENT

GETDOCUMENT returns the document node of a DOM tree document built by the parser. This function must be called only after a document is parsed.

## Syntax

```sql
FUNCTION GETDOCUMENT(
  p Parser)
RETURN DOMDocument;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser) | IN | (IN) |

**Returns:** `DOMDocument`

## Usage Notes

Syntax FUNCTION GETDOCUMENT( p Parser) RETURN DOMDocument; Parameters Table 207-4 GETDOCUMENT Function Parameters Parameter IN / OUT Description p (IN) Parser instance.