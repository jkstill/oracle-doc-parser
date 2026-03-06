---
id: 19c__DBMS_XMLGEN.CONVERT
name: DBMS_XMLGEN.CONVERT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLGEN
tags: [dbms_xmlgen]
source_file: DBMS_XMLGEN.html
---

# DBMS_XMLGEN.CONVERT

This function converts the XML data into the escaped or unescapes XML equivalent, and returns XML CLOB data in encoded or decoded format. There are several version of the function.

## Syntax

```sql
DBMS_XMLGEN.CONVERT (
   xmlData IN VARCHAR2,
   flag    IN NUMBER := ENTITY_ENCODE)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlData | VARCHAR2 | IN | The XML CLOB data to be encoded or decoded. |
| flag | NUMBER | IN | The flag setting; ENTITY_ENCODE (default) for encode, and ENTITY_DECODE for decode. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Uses XMLDATA in string form ( VARCHAR2 ): DBMS_XMLGEN.CONVERT ( xmlData IN VARCHAR2, flag IN NUMBER := ENTITY_ENCODE) RETURN VARCHAR2; Uses XMLDATA in CLOB form: DBMS_XMLGEN.CONVERT ( xmlData IN CLOB, flag IN NUMBER := ENTITY_ENCODE) RETURN CLOB; Parameters Table 205-3 CONVERT Function Parameters Parameter Description xmlData The XML CLOB data to be encoded or decoded. flag The flag setting; ENTITY_ENCODE (default) for encode, and ENTITY_DECODE for decode. Usage Notes This function escapes the XML data if the ENTITY_ENCODE is specified. For example, the escaped form of the character < is &lt; . Unescaping is the reverse transformation.