---
id: 19c__DBMS_XMLSTORE.DELETEXML
name: DBMS_XMLSTORE.DELETEXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.DELETEXML

DELETEXML deletes records specified by data from the XML document from the table specified at the context creation time, and returns the number of rows deleted.

## Syntax

```sql
FUNCTION deleteXML(
  ctxHdl IN ctxPType,
  xDoc IN VARCHAR2)
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctxHdl | ctxPType | IN | (IN) |
| xDoc | VARCHAR2) | IN | (IN) |

**Returns:** `NUMBER`

## Usage Notes

Syntax The following syntax uses a VARCHAR2 type for the xDoc parameter. FUNCTION deleteXML( ctxHdl IN ctxPType, xDoc IN VARCHAR2) RETURN NUMBER; The following syntax uses a CLOB type for the xDoc parameter. FUNCTION deleteXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; The following syntax uses an XMLType type for the xDoc parameter. FUNCTION deleteXML( ctxHdl IN ctxType, xDoc IN XMLType) RETURN NUMBER; Parameters Table 214-6 DELETEXML Function Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. xDoc (IN) String containing the XML document.