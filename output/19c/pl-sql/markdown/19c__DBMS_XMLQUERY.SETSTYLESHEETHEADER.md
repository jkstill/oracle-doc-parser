---
id: 19c__DBMS_XMLQUERY.SETSTYLESHEETHEADER
name: DBMS_XMLQUERY.SETSTYLESHEETHEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETSTYLESHEETHEADER

SETSTYLESHEETHEADER sets the stylesheet header (the stylesheet processing instructions) in the generated XML document.

## Syntax

```sql
PROCEDURE SETSTYLESHEETHEADER(
ctxHdl IN ctxType,
uri IN VARCHAR2,
type IN VARCHAR2 := 'text/xsl');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| uri | VARCHAR2 | IN | (IN) |
| type | VARCHAR2 | IN | (IN) |

## Usage Notes

Passing NULL for the uri argument will unset the stylesheet header and the stylesheet type. PROCEDURE SETSTYLESHEETHEADER( ctxHdl IN ctxType, uri IN VARCHAR2, type IN VARCHAR2 := 'text/xsl');