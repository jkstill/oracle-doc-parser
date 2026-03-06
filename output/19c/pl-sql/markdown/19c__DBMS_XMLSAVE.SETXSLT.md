---
id: 19c__DBMS_XMLSAVE.SETXSLT
name: DBMS_XMLSAVE.SETXSLT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETXSLT

SETXSLT registers an XSL transform to be applied to the XML to be saved.

## Syntax

```sql
PROCEDURE setXSLT(
  ctxHdl IN ctxType,
  uri IN VARCHAR2,
  ref IN VARCHAR2 := null);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| uri | VARCHAR2 | IN | (IN) |
| ref | VARCHAR2 | IN | (IN) |
| stylesheet |  |  | (IN) |

## Usage Notes

If a stylesheet was already registered, it gets replaced by the new one. To un-register the stylesheet, pass in null for the URI. The options are described in the following table. Syntax Table 209-23 SETXSLT Procedure Syntax Syntax Description PROCEDURE setXSLT( ctxHdl IN ctxType, uri IN VARCHAR2, ref IN VARCHAR2 := null); Passes in the stylesheet through a URI. PROCEDURE setXSLT( ctxHdl IN ctxType, stylesheet IN CLOB, ref IN VARCHAR2 := null); Passes in the stylesheet through a CLOB . Parameters Table 209-24 SETXSLT Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. uri (IN) URI to the stylesheet to register. ref (IN) URL for include, import, and external entities. stylesheet (IN) CLOB containing the stylesheet to register.