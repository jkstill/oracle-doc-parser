---
id: 19c__DBMS_XMLDOM.GETEXPANDEDNAME
name: DBMS_XMLDOM.GETEXPANDEDNAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETEXPANDEDNAME

This subprogram is overloaded as a procedure and two functions. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETEXPANDEDNAME(
   n       IN      DOMNODE
   data    OUT     VARCHAR);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| data | VARCHAR) | OUT | Returned expanded name of the Node |
| a |  |  | DOMATTR |
| elem |  |  | DOMELEMENT |

## Usage Notes

Syntax Retrieves the expanded name of the Node if is in an Element or Attribute type; otherwise, returns NULL (See Also: DOMNode Subprograms ) DBMS_XMLDOM.GETEXPANDEDNAME( n IN DOMNODE data OUT VARCHAR); Returns the expanded name of the DOMAttr (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.GETEXPANDEDNAME( a IN DOMAttr) RETURN VARCHAR2; Returns the expanded name of the DOMElement (See Also: DOMElement Subprograms ): DBMS_XMLDOM.GETEXPANDEDNAME( elem IN DOMELEMENT) RETURN VARCHAR2; Parameters Table 204-54 GETEXPANDEDNAME Procedure and Function Parameters Parameter Description n DOMNODE data Returned expanded name of the Node a DOMATTR elem DOMELEMENT