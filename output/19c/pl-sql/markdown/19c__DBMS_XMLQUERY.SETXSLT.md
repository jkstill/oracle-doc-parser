---
id: 19c__DBMS_XMLQUERY.SETXSLT
name: DBMS_XMLQUERY.SETXSLT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETXSLT

SETXSLT registers a stylesheet to be applied to generated XML. If a stylesheet was already registered, it is replaced by the new one. Passing NULL for the uri argument, or NULL or an empty string for the stylesheet argument, unsets the stylesheet header and type.

## Syntax

```sql
PROCEDURE SETXSLT(
  ctxHdl IN ctxType,
  uri IN VARCHAR2,
  ref IN VARCHAR2 := null);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| uri | VARCHAR2 | IN | (IN) |
| stylesheet |  |  | (IN) |
| ref | VARCHAR2 | IN | (IN) |

## Usage Notes

Syntax To unregister the stylesheet, pass in NULL for the URI. PROCEDURE SETXSLT( ctxHdl IN ctxType, uri IN VARCHAR2, ref IN VARCHAR2 := null); To unregister the stylesheet pass in NULL or an empty string for the stylesheet. PROCEDURE SETXSLT( ctxHdl IN ctxType, stylesheet CLOB, ref IN VARCHAR2 := null); Parameters Table 208-30 SETXSLT Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. uri (IN) Stylesheet URI. stylesheet (IN) Stylesheet. ref (IN) URL to include, imported and external entities.