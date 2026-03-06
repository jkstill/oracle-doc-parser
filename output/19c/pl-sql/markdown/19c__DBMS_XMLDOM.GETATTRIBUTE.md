---
id: 19c__DBMS_XMLDOM.GETATTRIBUTE
name: DBMS_XMLDOM.GETATTRIBUTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETATTRIBUTE

This function returns the value of an attribute of an DOMELEMENT by name.

## Syntax

```sql
DBMS_XMLDOM.GETATTRIBUTE(
   elem       IN      DOMELEMENT,
   name       IN      VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT |
| name | VARCHAR2) | IN | Attribute name |
| ns |  |  | Namespace |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Returns the value of a DOMELEMENT 's attribute by name: DBMS_XMLDOM.GETATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2) RETURN VARCHAR2; Returns the value of a DOMELEMENT 's attribute by name and namespace URI: DBMS_XMLDOM.GETATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2, ns IN VARCHAR2) RETURN VARCHAR2; Parameters Table 204-43 GETATTRIBUTE Function Parameters Parameter Description elem The DOMELEMENT name Attribute name ns Namespace