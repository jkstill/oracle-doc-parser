---
id: 19c__DBMS_XMLSAVE.INSERTXML
name: DBMS_XMLSAVE.INSERTXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.INSERTXML

Inserts the XML document into the table specified at the context creation time, and returns the number of rows inserted. The options are described in the following table.

## Syntax

```sql
FUNCTION insertXML(
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

Syntax Table 209-9 INSERTXML Function Syntax Syntax Description FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN VARCHAR2) RETURN NUMBER; Passes in the xDoc parameter as a VARCHAR2 . FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; Passes in the xDoc parameter as a CLOB . Parameters Table 209-10 INSERTXML Function Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. xDoc (IN) String containing the XML document.