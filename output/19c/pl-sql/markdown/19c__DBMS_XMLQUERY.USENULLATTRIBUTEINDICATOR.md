---
id: 19c__DBMS_XMLQUERY.USENULLATTRIBUTEINDICATOR
name: DBMS_XMLQUERY.USENULLATTRIBUTEINDICATOR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.USENULLATTRIBUTEINDICATOR

This procedure specifies whether to use an XML attribute to indicate NULL ness, or to do this by omitting the particular entity in the XML document.

## Syntax

```sql
PROCEDURE SETNULLATTRIBUTEINDICATOR(
ctxHdl IN ctxType, 
flag IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN) | IN | (IN) |

## Usage Notes

PROCEDURE SETNULLATTRIBUTEINDICATOR( ctxHdl IN ctxType, flag IN BOOLEAN);