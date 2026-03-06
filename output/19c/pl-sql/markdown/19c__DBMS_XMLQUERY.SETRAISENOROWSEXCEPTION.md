---
id: 19c__DBMS_XMLQUERY.SETRAISENOROWSEXCEPTION
name: DBMS_XMLQUERY.SETRAISENOROWSEXCEPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETRAISENOROWSEXCEPTION

This procedure specifies whether to throw an OracleXMLNoRowsException when the generated XML document is empty. By default, the exception is not thrown.

## Syntax

```sql
PROCEDURE SETRAISENOROWSEXCEPTION(
ctxHdl IN ctxType,
flag IN BOOLEAN:=false);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN | IN | (IN) |

## Usage Notes

PROCEDURE SETRAISENOROWSEXCEPTION( ctxHdl IN ctxType, flag IN BOOLEAN:=false);