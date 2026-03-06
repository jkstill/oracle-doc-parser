---
id: 19c__DBMS_XMLQUERY.NEWCONTEXT
name: DBMS_XMLQUERY.NEWCONTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.NEWCONTEXT

NEWCONTEXT creates a save context and returns the context handle.

## Syntax

```sql
FUNCTION NEWCONTEXT(
  sqlQuery IN VARCHAR2)
RETURN ctxType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlQuery | VARCHAR2) | IN | (IN) |

**Returns:** `ctxType`

## Usage Notes

Syntax FUNCTION NEWCONTEXT( sqlQuery IN VARCHAR2) RETURN ctxType; FUNCTION NEWCONTEXT( sqlQuery IN CLOB) RETURN ctxType;