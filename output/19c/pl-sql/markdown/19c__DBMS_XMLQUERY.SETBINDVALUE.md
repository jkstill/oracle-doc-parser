---
id: 19c__DBMS_XMLQUERY.SETBINDVALUE
name: DBMS_XMLQUERY.SETBINDVALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETBINDVALUE

This procedure sets a value for a particular bind name.

## Syntax

```sql
PROCEDURE SETBINDVALUE(
ctxHdl IN ctxType,
bindName IN VARCHAR2,
bindValue IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| bindName | VARCHAR2 | IN | (IN) |
| bindValue | VARCHAR2) | IN | (IN) |

## Usage Notes

PROCEDURE SETBINDVALUE( ctxHdl IN ctxType, bindName IN VARCHAR2, bindValue IN VARCHAR2);