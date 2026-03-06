---
id: 19c__DBMS_XMLDOM.GETATTRIBUTENODE
name: DBMS_XMLDOM.GETATTRIBUTENODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETATTRIBUTENODE

This function returns an attribute node from the DOMELEMENT by name. The function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETATTRIBUTENODE(
   elem      IN     DOMElement,
   name      IN     VARCHAR2)
 RETURN DOMATTR;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMElement | IN | The DOMELEMENT |
| name | VARCHAR2) | IN | Attribute name; * matches any attribute |
| ns |  |  | Namespace |

**Returns:** `DOMATTR`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Returns an attribute node from the DOMELEMENT by name: DBMS_XMLDOM.GETATTRIBUTENODE( elem IN DOMElement, name IN VARCHAR2) RETURN DOMATTR; Returns an attribute node from the DOMELEMENT by name and namespace URI: DBMS_XMLDOM.GETATTRIBUTENODE( elem IN DOMElement, name IN VARCHAR2, ns IN VARCHAR2) RETURN DOMATTR; Parameters Table 204-44 GETATTRIBUTENODE Function Parameters Parameter Description elem The DOMELEMENT name Attribute name; * matches any attribute ns Namespace