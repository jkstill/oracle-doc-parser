---
id: 19c__DBMS_XMLSTORE.INSERTXML
name: DBMS_XMLSTORE.INSERTXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSTORE
tags: [dbms_xmlstore]
source_file: DBMS_XMLSTORE.html
---

# DBMS_XMLSTORE.INSERTXML

Inserts the XML document into the table specified at the context creation time, and returns the number of rows inserted.

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

Note that if a user passes an XML file for insertXML to DBMS_XMLSTORE that contains extra elements (elements that do not match any columns in the table), Oracle tries to insert into those columns unless SETUPDATECOLUMN is used. The use of setUpdateColumn is optional only if the elements in the XML file match up to the columns in the table. Syntax FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN VARCHAR2) RETURN NUMBER; FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN CLOB) RETURN NUMBER; FUNCTION insertXML( ctxHdl IN ctxType, xDoc IN XMLType) RETURN NUMBER; Parameters Table 214-7 INSERTXML Function Parameters Parameter IN / OUT Description ctxHdl (IN) Context handle. xDoc (IN) String containing the XML document.