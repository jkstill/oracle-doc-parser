---
id: 19c__DBMS_XMLSAVE.DELETEXML
name: DBMS_XMLSAVE.DELETEXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSAVE
tags: [dbms_xmlsave]
source_file: DBMS_XMLSAVE.html
---

# DBMS_XMLSAVE.DELETEXML

The DELETEXML function deletes records specified by data from the XML document from the table specified at the context creation time, and returns the number of rows deleted.

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

Syntax The options are described in the following table. FUNCTION deleteXML( ctxHdl IN ctxPType, xDoc IN VARCHAR2) RETURN NUMBER; FUNCTION deleteXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; Paramters Table 209-7 DELETEXML Function Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. xDoc (IN) String containing the XML document.