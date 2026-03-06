---
id: 19c__DBMS_XMLQUERY.SETROWIDATTRVALUE
name: DBMS_XMLQUERY.SETROWIDATTRVALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.SETROWIDATTRVALUE

This procedure specifies the scalar column whose value is to be assigned to the id attribute of the row enclosing tag.

## Syntax

```sql
PROCEDURE SETROWIDATTRVALUE(
ctxHdl IN ctxType,
colName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| colName | VARCHAR2) | IN | (IN) |

## Usage Notes

Passing NULL or an empty string for the colName assigns the row count value (0, 1, 2 and so on) to the row id attribute. PROCEDURE SETROWIDATTRVALUE( ctxHdl IN ctxType, colName IN VARCHAR2);