---
id: 19c__DBMS_XMLDOM.GETPUBLICID
name: DBMS_XMLDOM.GETPUBLICID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETPUBLICID

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETPUBLICID(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dt | DOMDOCUMENTTYPE) | IN | The DTD |
| ent |  |  | DOMENTITY |
| n |  |  | DOMNOTATION |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Returns the public identifier of the specified DTD (See Also: DOMDocumentType Subprograms ): DBMS_XMLDOM.GETPUBLICID( dt IN DOMDOCUMENTTYPE) RETURN VARCHAR2; Returns the public identifier of the DOMENTITY (See Also: DOMEntity Subprograms ): DBMS_XMLDOM.GETPUBLICID( ent IN DOMENTITY) RETURN VARCHAR2; Returns the public identifier of the DOMNOTATION (See Also: DOMNotation Subprograms ): DBMS_XMLDOM.GETPUBLICID( n IN DOMNOTATION) RETURN VARCHAR2; Parameters Table 204-77 GETPUBLICID Function Parameters Parameter Description dt The DTD ent DOMENTITY n DOMNOTATION