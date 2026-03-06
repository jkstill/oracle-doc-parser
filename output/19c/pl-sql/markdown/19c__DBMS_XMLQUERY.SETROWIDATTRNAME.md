---
id: 19c__DBMS_XMLQUERY.SETROWIDATTRNAME
name: DBMS_XMLQUERY.SETROWIDATTRNAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETROWIDATTRNAME

This procedure sets the name of the id attribute of the row enclosing tag. Passing NULL or an empty string for the tag causes the row id attribute to be omitted.

## Syntax

```sql
PROCEDURE SETROWIDATTRNAME(
ctxHdl IN ctxType,
attrName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| attrName | VARCHAR2) | IN | (IN) |

## Usage Notes

PROCEDURE SETROWIDATTRNAME( ctxHdl IN ctxType, attrName IN VARCHAR2);