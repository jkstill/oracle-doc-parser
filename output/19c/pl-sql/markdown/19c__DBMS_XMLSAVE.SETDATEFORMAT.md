---
id: 19c__DBMS_XMLSAVE.SETDATEFORMAT
name: DBMS_XMLSAVE.SETDATEFORMAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.SETDATEFORMAT

This procedure sets the format of the generated dates in the XML document.

## Syntax

```sql
PROCEDURE setDateFormat(
   ctxHdl IN ctxType,
   mask IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| mask | VARCHAR2) | IN | (IN) |

## Usage Notes

The syntax of the date format pattern, the date mask, should conform to the requirements of the class java.text.SimpleDateFormat . Setting the mask to <code>null</code> or an empty string unsets the date mask. Syntax PROCEDURE setDateFormat( ctxHdl IN ctxType, mask IN VARCHAR2); Parameters Table 209-16 SETDATEFORMAT Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. mask (IN) Syntax of the date format pattern.