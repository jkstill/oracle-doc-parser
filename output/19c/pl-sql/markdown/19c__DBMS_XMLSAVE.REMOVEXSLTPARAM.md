---
id: 19c__DBMS_XMLSAVE.REMOVEXSLTPARAM
name: DBMS_XMLSAVE.REMOVEXSLTPARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.REMOVEXSLTPARAM

This procedure removes the value of a top-level stylesheet parameter.

## Syntax

```sql
PROCEDURE removeXSLTParam(
   ctxHdl IN ctxType, 
   name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| name | VARCHAR2) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE removeXSLTParam( ctxHdl IN ctxType, name IN VARCHAR2); Parameters Table 209-13 REMOVEXSLTPARAM Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. name (IN) Parameter name.