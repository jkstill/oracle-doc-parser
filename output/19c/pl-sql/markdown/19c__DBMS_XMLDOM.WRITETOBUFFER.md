---
id: 19c__DBMS_XMLDOM.WRITETOBUFFER
name: DBMS_XMLDOM.WRITETOBUFFER
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.WRITETOBUFFER

WRITETOBUFFER is an overloaded procedure that writes an XML node, XML document, or a document fragment to a specified buffer.

## Syntax

```sql
DBMS_XMLDOM.WRITETOBUFFER( 
   n        IN      DOMNODE, 
   buffer   IN OUT  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| buffer | VARCHAR2) | IN OUT | Buffer to which to write |
| doc |  |  | DOMDOCUMENT |
| df |  |  | DOM document fragment |

## Usage Notes

This procedure is overloaded. The specific forms of functionality are described along with the syntax declarations. Syntax Writes XML node to specified buffer using the database character set (See Also: DOMNode Subprograms ): DBMS_XMLDOM.WRITETOBUFFER( n IN DOMNODE, buffer IN OUT VARCHAR2); Writes XML document to a specified buffer using database character set (See Also: DOMDocument Subprograms ): DBMS_XMLDOM.WRITETOBUFFER( doc IN DOMDOCUMENT, buffer IN OUT VARCHAR2); Writes the contents of the specified document fragment into a buffer using the database character set (See Also: DOMDocumentFragment Subprograms ): DBMS_XMLDOM.WRITETOBUFFER( df IN DOMDOCUMENTFRAGMENT, buffer IN OUT VARCHAR2); Parameters Table 204-135 WRITETOBUFFER Procedure Parameters Parameter Description n DOMNODE buffer Buffer to which to write doc DOMDOCUMENT df DOM document fragment