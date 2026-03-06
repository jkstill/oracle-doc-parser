---
id: 19c__DBMS_XMLQUERY.SETSKIPROWS
name: DBMS_XMLQUERY.SETSKIPROWS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETSKIPROWS

SETSKIPROWS sets the number of rows to skip. By default, 0 rows are skipped.

## Syntax

```sql
PROCEDURE SETSKIPROWS(
ctxHdl IN ctxType,
rows IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| rows | NUMBER) | IN | (IN) |

## Usage Notes

PROCEDURE SETSKIPROWS( ctxHdl IN ctxType, rows IN NUMBER);