---
id: 19c__DBMS_XMLQUERY.GETNUMROWSPROCESSED
name: DBMS_XMLQUERY.GETNUMROWSPROCESSED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.GETNUMROWSPROCESSED

Return the number of rows processed for the query.

## Syntax

```sql
FUNCTION GETNUMROWSPROCESSED(
ctxHdl IN ctxType)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType) | IN | (IN) |

**Returns:** `NUMBER`

## Usage Notes

FUNCTION GETNUMROWSPROCESSED( ctxHdl IN ctxType) RETURN NUMBER;