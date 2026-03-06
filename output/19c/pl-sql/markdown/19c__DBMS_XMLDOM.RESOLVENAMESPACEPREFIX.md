---
id: 19c__DBMS_XMLDOM.RESOLVENAMESPACEPREFIX
name: DBMS_XMLDOM.RESOLVENAMESPACEPREFIX
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.RESOLVENAMESPACEPREFIX

This function resolves the specified namespace prefix, and returns the resolved namespace.

## Syntax

```sql
DBMS_XMLDOM.RESOLVENAMESPACEPREFIX(
   elem       IN     DOMELEMENT,
   prefix     IN     VARCHAR2) 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| elem | DOMELEMENT | IN | The DOMELEMENT |
| prefix | VARCHAR2) | IN | Namespace prefix |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DOMElement Subprograms See Also: DOMElement Subprograms Syntax DBMS_XMLDOM.RESOLVENAMESPACEPREFIX( elem IN DOMELEMENT, prefix IN VARCHAR2) RETURN VARCHAR2; Parameters Table 204-118 RESOLVENAMESPACEPREFIX Function Parameters Parameter Description elem The DOMELEMENT prefix Namespace prefix