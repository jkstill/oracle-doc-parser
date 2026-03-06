---
id: 19c__DBMS_XMLSAVE.SETIGNORECASE
name: DBMS_XMLSAVE.SETIGNORECASE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETIGNORECASE

This function tells the XSU whether to ignore case when the XSU maps XML elements to database columns/attributes. This matching is based on the element names (XML tags).

## Syntax

```sql
PROCEDURE setIgnoreCase(
   ctxHdl IN ctxType,
   flag IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | NUMBER) | IN | (IN) |

## Usage Notes

Syntax PROCEDURE setIgnoreCase( ctxHdl IN ctxType, flag IN NUMBER); Parameters Table 209-17 SETIGNORECASE Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. flag (IN) Ignore tag case in the XML doc? 0= FALSE , 1= TRUE .