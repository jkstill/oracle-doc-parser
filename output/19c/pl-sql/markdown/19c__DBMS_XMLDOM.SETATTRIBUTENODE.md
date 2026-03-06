---
id: 19c__DBMS_XMLDOM.SETATTRIBUTENODE
name: DBMS_XMLDOM.SETATTRIBUTENODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETATTRIBUTENODE

This function adds a new attribute node to the DOMELEMENT .

## Syntax

```sql
DBMS_XMLDOM.SETATTRIBUTENODE(
   elem      IN  DOMELEMENT,
   newAttr   IN  DOMATTR)
 RETURN DOMATTR;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT |
| newAttr | DOMATTR) | IN | The new DOMATTR |
| ns |  |  | The namespace |

**Returns:** `DOMATTR`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Adds a new attribute node to the DOMELEMENT : DBMS_XMLDOM.SETATTRIBUTENODE( elem IN DOMELEMENT, newAttr IN DOMATTR) RETURN DOMATTR; Adds a new attribute node to the DOMElement ; namespace enabled: DBMS_XMLDOM.SETATTRIBUTENODE( elem IN DOMELEMENT, newAttr IN DOMATTR, ns IN VARCHAR2) RETURN DOMATTR; Parameters Table 204-120 SETATTRIBUTENODE Function Parameters Parameter Description elem The DOMELEMENT newAttr The new DOMATTR ns The namespace