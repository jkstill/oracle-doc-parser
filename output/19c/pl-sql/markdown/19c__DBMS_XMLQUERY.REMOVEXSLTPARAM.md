---
id: 19c__DBMS_XMLQUERY.REMOVEXSLTPARAM
name: DBMS_XMLQUERY.REMOVEXSLTPARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.REMOVEXSLTPARAM

This procedure removes the value of a top-level stylesheet parameter. If no stylesheet is registered, this method is not operational.

## Syntax

```sql
PROCEDURE REMOVEXSLTPARAM(
ctxHdl IN ctxType,
name IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| name | VARCHAR2) | IN | (IN) |

## Usage Notes

PROCEDURE REMOVEXSLTPARAM( ctxHdl IN ctxType, name IN VARCHAR2);