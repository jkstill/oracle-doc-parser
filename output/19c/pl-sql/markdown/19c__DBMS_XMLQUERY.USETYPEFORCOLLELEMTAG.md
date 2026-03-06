---
id: 19c__DBMS_XMLQUERY.USETYPEFORCOLLELEMTAG
name: DBMS_XMLQUERY.USETYPEFORCOLLELEMTAG
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.USETYPEFORCOLLELEMTAG

This procedure specifies whether to use the collection element's type name as its element tag name.

## Syntax

```sql
PROCEDURE USETYPEFORCOLLELEMTAG(
ctxHdl IN ctxType,
flag IN BOOLEAN := true);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| flag | BOOLEAN | IN | (IN) |

## Usage Notes

By default, the tag name for elements of a collection is the collection's tag name followed by _item . PROCEDURE USETYPEFORCOLLELEMTAG( ctxHdl IN ctxType, flag IN BOOLEAN := true);