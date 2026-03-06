---
id: 19c__DBMS_XMLGEN.GETXMLTYPE
name: DBMS_XMLGEN.GETXMLTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.GETXMLTYPE

This function gets the XML document and returns it as an XMLTYPE . XMLTYPE operations can be performed on the results. This function is overloaded.

## Syntax

```sql
DBMS_XMLGEN.GETXMLTYPE (
   ctx           IN ctxhandle,
   dtdOrSchema   IN number := NONE)
 RETURN sys.XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| ctx | ctxhandle | IN | The context handle obtained from the newContext call. |
| sqlQuery |  |  | The SQL query string. |
| dtdOrSchema | number | IN | Generate a DTD or a schema? Only NONE is supported. |

**Returns:** `sys.XMLType`

## Usage Notes

Syntax Generates the XML document and returns it as a sys.XMLType: DBMS_XMLGEN.GETXMLTYPE ( ctx IN ctxhandle, dtdOrSchema IN number := NONE) RETURN sys.XMLType; Converts the results from the SQL query string to XML format, and returns the XML as a sys.XMLType : DBMS_XMLGEN.GETXMLTYPE ( sqlQuery IN VARCHAR2, dtdOrSchema IN number := NONE) RETURN sys.XMLType Parameters Table 205-6 GETXMLTYPE Function Parameters Parameter Description ctx The context handle obtained from the newContext call. sqlQuery The SQL query string. dtdOrSchema Generate a DTD or a schema? Only NONE is supported.