---
id: 19c__DBMS_XMLDOM.GETNAMESPACE
name: DBMS_XMLDOM.GETNAMESPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNAMESPACE

This subprogram is overloaded as a procedure and two functions. The specific forms of functionality are described alongside the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETNAMESPACE(
   n       IN     DOMNODE,
   data    OUT    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| data | VARCHAR2) | OUT | Returned namespace URI |
| a |  |  | DOMATTR |
| elem |  |  | DOMELEMENT |

## Usage Notes

Syntax Retrieves the namespace URI associated with the node (See Also: DOMNode Subprograms ): DBMS_XMLDOM.GETNAMESPACE( n IN DOMNODE, data OUT VARCHAR2); Retrieves the namespace of the DOMATTR (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.GETNAMESPACE( a IN DOMATTR) RETURN VARCHAR2; Retrieves the namespace of the DOMELEMENT (See Also: DOMElement Subprograms ): DBMS_XMLDOM.GETNAMESPACE( elem IN DOMELEMENT) RETURN VARCHAR2; Parameters Table 204-62 GETNAMESPACE Procedure and Function Parameters Parameter Description n DOMNODE data Returned namespace URI a DOMATTR elem DOMELEMENT