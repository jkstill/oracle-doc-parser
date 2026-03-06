---
id: 19c__DBMS_XMLQUERY.SETSQLTOXMLNAMEESCAPING
name: DBMS_XMLQUERY.SETSQLTOXMLNAMEESCAPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETSQLTOXMLNAMEESCAPING

This procedure turns on or off escaping of XML tags in the case that the SQL object name, which is mapped to a XML identifier, is not a valid XML identifier.

## Syntax

```sql
PROCEDURE SETSQLTOXMLNAMEESCAPING(
ctxHdl IN ctxType,
flag IN BOOLEAN := true);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN | IN | (IN) |

## Usage Notes

PROCEDURE SETSQLTOXMLNAMEESCAPING( ctxHdl IN ctxType, flag IN BOOLEAN := true);