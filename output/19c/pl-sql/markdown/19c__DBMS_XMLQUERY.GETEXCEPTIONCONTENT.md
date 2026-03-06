---
id: 19c__DBMS_XMLQUERY.GETEXCEPTIONCONTENT
name: DBMS_XMLQUERY.GETEXCEPTIONCONTENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.GETEXCEPTIONCONTENT

GETEXCEPTIONCONTENT returns the thrown exception's SQL error code and error message through the procedure's OUT parameters.

## Syntax

```sql
PROCEDURE GETEXCEPTIONCONTENT(
  ctxHdl IN ctxType,
  errNo OUT NUMBER,
  errMsg OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| errNo | NUMBER | OUT | (OUT) |
| errMsg | VARCHAR2) | OUT | (OUT) |

## Usage Notes

This procedure is a work around the JVM functionality that obscures the original exception by its own exception, rendering PL/SQL unable to access the original exception content. PROCEDURE GETEXCEPTIONCONTENT( ctxHdl IN ctxType, errNo OUT NUMBER, errMsg OUT VARCHAR2); Parameters Table 208-6 GETEXCEPTIONCONTENT Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. errNo (OUT) Error number. errMsg (OUT) Error message.