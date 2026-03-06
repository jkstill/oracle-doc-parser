---
id: 19c__DBMS_XMLSTORE.SETROWTAG
name: DBMS_XMLSTORE.SETROWTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.SETROWTAG

This procedure names the tag used in the XML document, to enclose the XML elements corresponding to database records.

## Syntax

```sql
PROCEDURE setRowTag(
   ctxHdl IN ctxType,
   tag IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| tag | VARCHAR2) | IN | (IN) |

## Usage Notes

PROCEDURE setRowTag( ctxHdl IN ctxType, tag IN VARCHAR2);