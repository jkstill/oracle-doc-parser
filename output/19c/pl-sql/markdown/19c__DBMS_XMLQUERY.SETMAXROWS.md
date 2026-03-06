---
id: 19c__DBMS_XMLQUERY.SETMAXROWS
name: DBMS_XMLQUERY.SETMAXROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETMAXROWS

This procedure sets the maximum number of rows to be converted to XML. By default, there is no set maximum.

## Syntax

```sql
PROCEDURE SETMAXROWS (
ctxHdl IN ctxType,
rows IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| rows | NUMBER) | IN | (IN) |

## Usage Notes

PROCEDURE SETMAXROWS ( ctxHdl IN ctxType, rows IN NUMBER);