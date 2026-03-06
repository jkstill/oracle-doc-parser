---
id: 19c__DBMS_XMLSAVE.SETXSLTPARAM
name: DBMS_XMLSAVE.SETXSLTPARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETXSLTPARAM

SETXSLTPARAM sets the value of a top-level stylesheet parameter.

## Syntax

```sql
PROCEDURE setXSLTParam(
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

The parameter is expected to be a valid XPath expression; literal values would therefore have to be explicitly quoted. Syntax PROCEDURE setXSLTParam( ctxHdl IN ctxType, name IN VARCHAR2, value IN VARCHAR2); Parameters Table 209-25 SETXSLTPARAM Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. name (IN) Parameter name. value (IN) Parameter value as an XPath expression