---
id: 19c__DBMS_XMLQUERY.SETENCODINGTAG
name: DBMS_XMLQUERY.SETENCODINGTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETENCODINGTAG

This procedure sets the encoding processing instruction in the XML document.

## Syntax

```sql
PROCEDURE SETENCODINGTAG(
ctxHdl IN ctxType,
enc IN VARCHAR2 := DB_ENCODING);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| enc | VARCHAR2 | IN | (IN) |

## Usage Notes

PROCEDURE SETENCODINGTAG( ctxHdl IN ctxType, enc IN VARCHAR2 := DB_ENCODING);