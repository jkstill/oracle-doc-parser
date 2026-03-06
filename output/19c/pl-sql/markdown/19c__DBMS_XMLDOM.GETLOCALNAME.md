---
id: 19c__DBMS_XMLDOM.GETLOCALNAME
name: DBMS_XMLDOM.GETLOCALNAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETLOCALNAME

This function is overloaded as a procedure and two functions. The specific forms of functionality are described alongside the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETLOCALNAME(
   n       IN     DOMNODE,
   data    OUT    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNode |
| data | VARCHAR2) | OUT | Returned local name. |
| a |  |  | DOMAttr . |
| elem |  |  | DOMElement . |

## Usage Notes

Syntax Retrieves the local part of the node's qualified name (See Also: DOMNode Subprograms ): DBMS_XMLDOM.GETLOCALNAME( n IN DOMNODE, data OUT VARCHAR2); Returns the local name of the DOMAttr (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.GETLOCALNAME( a IN DOMATTR) RETURN VARCHAR2; Returns the local name of the DOMElement (See Also: DOMElement Subprograms ) DBMS_XMLDOM.GETLOCALNAME( elem IN DOMELEMENT) RETURN VARCHAR2; Parameters Table 204-59 GETLOCALNAME Procedure and Function Parameters Parameter Description n DOMNode data Returned local name. a DOMAttr . elem DOMElement .