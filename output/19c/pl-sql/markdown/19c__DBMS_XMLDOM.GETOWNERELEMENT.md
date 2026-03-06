---
id: 19c__DBMS_XMLDOM.GETOWNERELEMENT
name: DBMS_XMLDOM.GETOWNERELEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETOWNERELEMENT

This function retrieves the Element node to which the specified Attribute is attached.

## Syntax

```sql
DBMS_XMLDOM.GETOWNERELEMENT(
   a       IN     DOMATTR)
 RETURN DOMElement;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| a | DOMATTR) | IN | Attribute |

**Returns:** `DOMElement`

## Usage Notes

See Also: DOMAttr Subprograms See Also: DOMAttr Subprograms Syntax DBMS_XMLDOM.GETOWNERELEMENT( a IN DOMATTR) RETURN DOMElement; Parameters Table 204-73 GETOWNERELEMENT Function Parameters Parameter Description a Attribute