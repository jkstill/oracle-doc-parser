---
id: 19c__DBMS_XMLQUERY.SETROWTAG
name: DBMS_XMLQUERY.SETROWTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETROWTAG

This procedure sets the tag to be used to enclose the XML element corresponding to a db.record .

## Syntax

```sql
PROCEDURE SETROWTAG(
ctxHdl IN ctxType,
tag IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| tag | VARCHAR2) | IN | (IN) |

## Usage Notes

PROCEDURE SETROWTAG( ctxHdl IN ctxType, tag IN VARCHAR2);