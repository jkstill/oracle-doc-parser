---
id: 19c__DBMS_XMLQUERY.SETRAISEEXCEPTION
name: DBMS_XMLQUERY.SETRAISEEXCEPTION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETRAISEEXCEPTION

This procedure specifies whether to throw raised exceptions.

## Syntax

```sql
PROCEDURE SETRAISEEXCEPTION(
ctxHdl IN ctxType,
flag IN BOOLEAN:=true);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN | IN | (IN) |

## Usage Notes

If this call isn't made or if FALSE is passed to the flag argument, the XSU catches the SQL exceptions and generates an XML document from the exception message. PROCEDURE SETRAISEEXCEPTION( ctxHdl IN ctxType, flag IN BOOLEAN:=true);