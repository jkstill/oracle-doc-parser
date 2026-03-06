---
id: 19c__DBMS_XMLDOM.GETNAME
name: DBMS_XMLDOM.GETNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNAME

This function is overloaded. The specific forms of functionality are described with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETNAME(
   a       IN     DOMATTR)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| a | DOMATTR) | IN | DOMATTR |
| dt |  |  | DOMDOCUMENTTYPE |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Returns the name of this attribute (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.GETNAME( a IN DOMATTR) RETURN VARCHAR2; Retrieves the name of DTD, or the name immediately following the DOCTYPE keyword (See Also: DOMDocumentType Subprograms ): DBMS_XMLDOM.GETNAME( dt IN DOMDOCUMENTTYPE) RETURN VARCHAR2; Parameters Table 204-60 GETNAME Function Parameters Parameter Description a DOMATTR dt DOMDOCUMENTTYPE