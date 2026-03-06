---
id: 19c__DBMS_XMLDOM.GETSYSTEMID
name: DBMS_XMLDOM.GETSYSTEMID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETSYSTEMID

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETSYSTEMID(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dt | DOMDOCUMENTTYPE) | IN | The DTD. |
| ent |  |  | DOMEntity . |
| n |  |  | DOMNotation . |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Returns the system id of the specified DTD (See Also: DOMDocumentType Subprograms ): DBMS_XMLDOM.GETSYSTEMID( dt IN DOMDOCUMENTTYPE) RETURN VARCHAR2; Returns the system identifier of the DOMENTITY (See Also: DOMEntity Subprograms ): DBMS_XMLDOM.GETSYSTEMID( ent IN DOMENTITY) RETURN VARCHAR2; Returns the system identifier of the DOMNOTATION (See Also: DOMNotation Subprograms ): DBMS_XMLDOM.GETSYSTEMID( n IN DOMNOTATION) RETURN VARCHAR2; Parameters Table 204-82 GETSYSTEMID Function Parameters Parameter Description dt The DTD. ent DOMEntity . n DOMNotation .