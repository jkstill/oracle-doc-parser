---
id: 19c__DBMS_XMLDOM.REMOVEATTRIBUTENODE
name: DBMS_XMLDOM.REMOVEATTRIBUTENODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.REMOVEATTRIBUTENODE

This function removes the specified attribute node from the DOMELEMENT . The method returns the removed node.

## Syntax

```sql
DBMS_XMLDOM.REMOVEATTRIBUTENODE(
   elem       IN     DOMELEMENT,
   oldAttr    IN     DOMATTR)
  RETURN DOMAttr;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT . |
| oldAttr | DOMATTR) | IN | The old DOMATTR . |

**Returns:** `DOMAttr`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax DBMS_XMLDOM.REMOVEATTRIBUTENODE( elem IN DOMELEMENT, oldAttr IN DOMATTR) RETURN DOMAttr; Parameters Table 204-113 REMOVEATTRIBUTENODE Function Parameters Parameter Description elem The DOMELEMENT . oldAttr The old DOMATTR .