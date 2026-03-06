---
id: 19c__DBMS_XMLQUERY.SETXSLTPARAM
name: DBMS_XMLQUERY.SETXSLTPARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETXSLTPARAM

SETXSLTPARAM sets the value of a top-level stylesheet parameter.

## Syntax

```sql
PROCEDURE SETXSLTPARAM(
ctxHdl IN ctxType,
name IN VARCHAR2,
value IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| name | VARCHAR2 | IN | (IN) |
| value | VARCHAR2) | IN | (IN) |

## Usage Notes

The parameter value is expected to be a valid XPath expression; the string literal values would therefore have to be quoted explicitly. If no stylesheet is registered, this method is not operational. PROCEDURE SETXSLTPARAM( ctxHdl IN ctxType, name IN VARCHAR2, value IN VARCHAR2);