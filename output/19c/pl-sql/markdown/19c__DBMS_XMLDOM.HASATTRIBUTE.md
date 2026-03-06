---
id: 19c__DBMS_XMLDOM.HASATTRIBUTE
name: DBMS_XMLDOM.HASATTRIBUTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.HASATTRIBUTE

Verifies whether an attribute has been defined for DOMELEMENT , or has a default value.

## Syntax

```sql
DBMS_XMLDOM.HASATTRIBUTE(
   elem     IN  DOMELEMENT,
   name     IN  VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT |
| name | VARCHAR2) | IN | Attribute name; * matches any attribute |
| ns |  |  | Namespace |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Verifies whether an attribute with the specified name has been defined for DOMElement : DBMS_XMLDOM.HASATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2) RETURN VARCHAR2; Verifies whether an attribute with specified name and namespace URI has been defined for DOMELEMENT ; namespace enabled: DBMS_XMLDOM.HASATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2, ns IN VARCHAR2) RETURN VARCHAR2; Parameters Table 204-87 HASATTRIBUTE Function Parameters Parameter Description elem The DOMELEMENT name Attribute name; * matches any attribute ns Namespace