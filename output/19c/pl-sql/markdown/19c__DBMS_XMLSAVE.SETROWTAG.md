---
id: 19c__DBMS_XMLSAVE.SETROWTAG
name: DBMS_XMLSAVE.SETROWTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETROWTAG

This procedure names the tag used in the XML document to enclose the XML elements corresponding to db. records.

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

Syntax PROCEDURE setRowTag( ctxHdl IN ctxType, tag IN VARCHAR2); Parameters Table 209-20 SETROWTAG Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. tag (IN) Tag name.