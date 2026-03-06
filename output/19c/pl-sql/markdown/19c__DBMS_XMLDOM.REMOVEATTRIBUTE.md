---
id: 19c__DBMS_XMLDOM.REMOVEATTRIBUTE
name: DBMS_XMLDOM.REMOVEATTRIBUTE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.REMOVEATTRIBUTE

This procedure removes an attribute from the DOMELEMENT by name.

## Syntax

```sql
DBMS_XMLDOM.REMOVEATTRIBUTE(
   elem     IN    DOMELEMENT,
   name     IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT |
| name | VARCHAR2) | IN | Attribute name |
| ns |  |  | Namespace |

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax Removes the value of a DOMELEMENT 's attribute by name: DBMS_XMLDOM.REMOVEATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2); Removes the value of a DOMELEMENT 's attribute by name and namespace URI. DBMS_XMLDOM.REMOVEATTRIBUTE( elem IN DOMELEMENT, name IN VARCHAR2, ns IN VARCHAR2); Parameters Table 204-112 REMOVEATTRIBUTE Procedure Parameters Parameter Description elem The DOMELEMENT name Attribute name ns Namespace