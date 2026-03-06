---
id: 19c__DBMS_XMLDOM.GETATTRIBUTES
name: DBMS_XMLDOM.GETATTRIBUTES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETATTRIBUTES

This function retrieves a NAMEDNODEMAP containing the attributes of this node (if it is an Element) or NULL otherwise.

## Syntax

```sql
DBMS_XMLDOM.GETATTRIBUTES(
   n      IN      DOMNode)
 RETURN DOMNAMEDNODEMAP;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNode) | IN | DOMNODE |

**Returns:** `DOMNAMEDNODEMAP`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETATTRIBUTES( n IN DOMNode) RETURN DOMNAMEDNODEMAP; Parameters Table 204-45 GETATTRIBUTES Function Parameters Parameter Description n DOMNODE