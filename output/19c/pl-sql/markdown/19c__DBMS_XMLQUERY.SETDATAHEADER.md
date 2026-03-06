---
id: 19c__DBMS_XMLQUERY.SETDATAHEADER
name: DBMS_XMLQUERY.SETDATAHEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETDATAHEADER

This procedure sets the XML data header.

## Syntax

```sql
PROCEDURE SETDATAHEADER(
ctxHdl IN ctxType,
header IN CLOB := null,
tag IN VARCHAR2 := null);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| header | CLOB | IN | (IN) |
| tag | VARCHAR2 | IN | (IN) |

## Usage Notes

The data header is an XML entity that is appended at the beginning of the query-generated XML entity, the rowset . The two entities are enclosed by the docTag argument. The last data header specified is used. Passing in NULL for the header parameter unsets the data header. PROCEDURE SETDATAHEADER( ctxHdl IN ctxType, header IN CLOB := null, tag IN VARCHAR2 := null);