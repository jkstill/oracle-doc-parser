---
id: 19c__DBMS_XMLSAVE.CLOSECONTEXT
name: DBMS_XMLSAVE.CLOSECONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.CLOSECONTEXT

This procedure closes/deallocates a particular save context.

## Syntax

```sql
PROCEDURE closeContext(
   ctxHdl IN ctxType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE closeContext( ctxHdl IN ctxType); Parameters Table 209-6 CLOSECONTEXT Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle.