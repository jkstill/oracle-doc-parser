---
id: 19c__DBMS_XMLSAVE.GETEXCEPTIONCONTENT
name: DBMS_XMLSAVE.GETEXCEPTIONCONTENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.GETEXCEPTIONCONTENT

Through its arguments, this method returns the thrown exception's error code and error message, SQL error code.

## Syntax

```sql
PROCEDURE getExceptionContent(
   ctxHdl IN ctxType,
   errNo OUT NUMBER,
   errMsg OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| errNo | NUMBER | OUT | (IN) |
| errMsg | VARCHAR2) | OUT | (IN) |

## Usage Notes

This is to get around the fact that the JVM throws an exception on top of whatever exception was raised, rendering PL/SQL unable to access the original exception. Syntax PROCEDURE getExceptionContent( ctxHdl IN ctxType, errNo OUT NUMBER, errMsg OUT VARCHAR2); Parameters Table 209-8 GETEXCEPTIONCONTENT Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. errNo (IN) Error number. errMsg (IN) Error message.