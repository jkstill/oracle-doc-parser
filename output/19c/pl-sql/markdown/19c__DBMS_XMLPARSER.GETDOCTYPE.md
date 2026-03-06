---
id: 19c__DBMS_XMLPARSER.GETDOCTYPE
name: DBMS_XMLPARSER.GETDOCTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.GETDOCTYPE

The GETDOCTYPE function returns the parsed DTD. This function must be called only after a DTD is parsed.

## Syntax

```sql
FUNCTION getDoctype(
  p Parser)
RETURN DOMDocumentType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser) | IN | (IN) |

**Returns:** `DOMDocumentType`

## Usage Notes

FUNCTION getDoctype( p Parser) RETURN DOMDocumentType; Parameters Table 207-3 GETDOCTYPE Function Parameters Parameter IN / OUT Description p (IN) Parser instance.