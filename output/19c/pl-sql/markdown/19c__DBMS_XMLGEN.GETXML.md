---
id: 19c__DBMS_XMLGEN.GETXML
name: DBMS_XMLGEN.GETXML
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.GETXML

This function gets the XML document. The function is overloaded.

## Syntax

```sql
DBMS_XMLGEN.GETXML (
   ctx          IN ctxHandle, 
   tmpclob      IN OUT NCOPY CLOB,
   dtdOrSchema  IN number := NONE)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxHandle | IN | The context handle obtained from the newContext call. |
| tmpclob | NCOPY | IN OUT | The CLOB to which the XML document is appended. |
| sqlQuery |  |  | The SQL query string. |
| dtdOrSchema | number | IN | Generate a DTD or a schema? Only NONE is supported. |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax Gets the XML document by fetching the maximum number of rows specified. It appends the XML document to the CLOB passed in. Use this version of GETXML Functions to avoid any extra CLOB copies and to reuse the same CLOB for subsequent calls. Because of the CLOB reuse, this GETXML Functions call is potentially more efficient: DBMS_XMLGEN.GETXML ( ctx IN ctxHandle, tmpclob IN OUT NCOPY CLOB, dtdOrSchema IN number := NONE) RETURN BOOLEAN; Generates the XML document and returns it as a temporary CLOB . The temporary CLOB obtained from this function must be freed using the DBMS_LOB.FREETEMPORARY call: DBMS_XMLGEN.GETXML ( ctx IN ctxHandle, dtdOrSchema IN number := NONE) RETURN CLOB; Converts the results from the SQL query string to XML format, and returns the XML as a temporary CLOB , which must be subsequently freed using the DBMS_LOB.FREETEMPORARY call: DBMS_XMLGEN.GETXML ( sqlQuery IN VARCHAR2, dtdOrSchema IN number := NONE) RETURN CLOB; Parameters Table 205-5 GETXML Function Parameters Parameter Description ctx The context handle obtained from the newContext call. tmpclob The CLOB to which the XML document is appended. sqlQuery The SQL query string. dtdOrSchema Generate a DTD or a schema? Only NONE is supported. Usage Notes When the rows indicated by the SETSKIPROWS Procedure call are skipped, the maximum number of rows as specified by the SETMAXROWS Procedure call (or the entire result if not specified) is fetched and converted to XML. Use the GETNUMROWSPROCESSED Function to check if any rows were retrieved.