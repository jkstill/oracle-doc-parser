---
id: 19c__DBMS_XMLDOM.SETATTRIBUTE
name: DBMS_XMLDOM.SETATTRIBUTE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETATTRIBUTE

This procedure sets the value of a DOMELEMENT 's attribute by name.

## Syntax

```sql
DBMS_XMLDOM.SETATTRIBUTE(
   elem       IN  DOMELEMENT,
   name       IN  VARCHAR2,
   newvalue   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT |
| name | VARCHAR2 | IN | Attribute name |
| newvalue | VARCHAR2) | IN | Attribute value |
| ns |  |  | Namespace |

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Sets the value of a DOMELEMENT 's attribute by name: DBMS_XMLDOM.SETATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2, newvalue IN VARCHAR2); Sets the value of a DOMElement 's attribute by name and namespace URI: DBMS_XMLDOM.SETATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2, newvalue IN VARCHAR2, ns IN VARCHAR2); Parameters Table 204-119 SETATTRIBUTE Procedure Parameters Parameter Description elem The DOMELEMENT name Attribute name newvalue Attribute value ns Namespace