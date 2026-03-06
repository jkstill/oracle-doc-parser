---
id: 19c__DBMS_XMLSTORE.UPDATEXML
name: DBMS_XMLSTORE.UPDATEXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.UPDATEXML

Updates the table specified at the context creation time with data from the XML document, and returns the number of rows updated.

## Syntax

```sql
FUNCTION updateXML(
  ctxHdl IN ctxType,
  xDoc IN VARCHAR2)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxType | IN | (IN) |
| xDoc | VARCHAR2) | IN | (IN) |

**Returns:** `NUMBER`

## Usage Notes

The options are described in the following table. Syntax The following syntax passes the xDoc parameter as a VARCHAR2 . FUNCTION updateXML( ctxHdl IN ctxType, xDoc IN VARCHAR2) RETURN NUMBER; The following syntax passes the xDoc parameter as a CLOB . FUNCTION updateXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; The following syntax passes the xDoc parameter as a XMLType . FUNCTION updateXML( ctxHdl IN ctxType, xDoc IN XMLType) RETURN NUMBER; Parameters Table 214-12 UPDATEXML Function Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. xDoc (IN) String containing the XML document.