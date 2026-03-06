---
id: 19c__DBMS_XMLSAVE.UPDATEXML
name: DBMS_XMLSAVE.UPDATEXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.UPDATEXML

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

The options are described in the following table. Syntax FUNCTION updateXML( ctxHdl IN ctxType, xDoc IN VARCHAR2) RETURN NUMBER; FUNCTION updateXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; Parameters Table 209-26 UPDATEXML Function Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. xDoc (IN) String containing the XML document.