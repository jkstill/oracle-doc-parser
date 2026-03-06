---
id: 19c__DBMS_XMLQUERY.GETXML
name: DBMS_XMLQUERY.GETXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLQUERY
tags: [dbms_xmlquery]
source_file: DBMS_XMLQUERY.html
---

# DBMS_XMLQUERY.GETXML

GETXML creates the new context, executes the query, gets the XML back and closes the context. This is a convenience function. The context does not need to be explicitly opened or closed.

## Syntax

```sql
FUNCTION GETXML(
  sqlQuery IN VARCHAR2,
  metaType IN NUMBER := NONE)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl |  |  | (IN) |
| metaType | NUMBER | IN | (IN) |
| sqlQuery | VARCHAR2 | IN | (IN) |
| xDoc |  |  | (IN) |

**Returns:** `CLOB`

## Usage Notes

Syntax This function uses a SQL query in string form. FUNCTION GETXML( sqlQuery IN VARCHAR2, metaType IN NUMBER := NONE) RETURN CLOB; This function uses a SQL query in CLOB form. FUNCTION GETXML( sqlQuery IN CLOB, metaType IN NUMBER := NONE) RETURN CLOB; This function generates the XML document based on a SQL query used to initialize the context. FUNCTION GETXML( ctxHdl IN ctxType, metaType IN NUMBER := NONE) RETURN CLOB; This procedure generates the XML document based on the SQL query used to initialize the context. PROCEDURE GETXML( ctxHdl IN ctxType, xDoc IN CLOB, metaType IN NUMBER := NONE); Parameters Table 208-8 GETXML Procedure Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. metaType (IN) XML metadatatype ( NONE , DTD , or SCHEMA ). sqlQuery (IN) SQL query. xDoc (IN) CLOB into which to write the generated XML document.