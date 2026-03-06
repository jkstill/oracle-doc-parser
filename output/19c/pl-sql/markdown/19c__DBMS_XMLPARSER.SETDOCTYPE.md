---
id: 19c__DBMS_XMLPARSER.SETDOCTYPE
name: DBMS_XMLPARSER.SETDOCTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLPARSER
tags: [dbms_xmlparser]
source_file: DBMS_XMLPARSER.html
---

# DBMS_XMLPARSER.SETDOCTYPE

This procedure sets a DTD to be used by the parser for validation. This call should be made before the document is parsed.

## Syntax

```sql
PROCEDURE setDoctype(
  p   Parser,
  dtd DOMDocumentType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p | Parser | IN | (IN) |
| dtd | DOMDocumentType) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE setDoctype( p Parser, dtd DOMDocumentType);