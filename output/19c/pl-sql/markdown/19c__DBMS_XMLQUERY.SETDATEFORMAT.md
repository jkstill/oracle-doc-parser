---
id: 19c__DBMS_XMLQUERY.SETDATEFORMAT
name: DBMS_XMLQUERY.SETDATEFORMAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETDATEFORMAT

This procedure sets the format of the generated dates in the XML document.

## Syntax

```sql
PROCEDURE SETDATEFORMAT(
ctxHdl IN ctxType,
mask IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| mask | VARCHAR2) | IN | (IN) |

## Usage Notes

The syntax of the date format pattern, the date mask, should conform to the requirements of the java.text.SimpleDateFormat class. Setting the mask to NULL or an empty string sets the default mask -- DEFAULT_DATE_FORMAT . PROCEDURE SETDATEFORMAT( ctxHdl IN ctxType, mask IN VARCHAR2);