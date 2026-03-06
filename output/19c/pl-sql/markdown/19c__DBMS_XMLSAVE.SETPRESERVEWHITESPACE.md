---
id: 19c__DBMS_XMLSAVE.SETPRESERVEWHITESPACE
name: DBMS_XMLSAVE.SETPRESERVEWHITESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETPRESERVEWHITESPACE

This procedure tells the XSU whether or not to preserve whitespace.

## Syntax

```sql
PROCEDURE setPreserveWhitespace(
   ctxHdl IN ctxType,
   flag IN BOOLEAN := true);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN | IN | (IN) |

## Usage Notes

Syntax PROCEDURE setPreserveWhitespace( ctxHdl IN ctxType, flag IN BOOLEAN := true); Parameters Table 209-19 SETPRESERVEWHITESPACE Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. flag (IN) Should XSU preserve whitespace?