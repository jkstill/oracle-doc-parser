---
id: 19c__DBMS_XMLDOM.GETCHARSET
name: DBMS_XMLDOM.GETCHARSET
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETCHARSET

This function retrieves the characterset of the DOM document.

## Syntax

```sql
DBMS_XMLDOM.GETCHARSET(
   doc IN    DOMDocument)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDocument) | IN | DOM document |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.GETCHARSET( doc IN DOMDocument) RETURN VARCHAR2; Parameters Table 204-46 GETCHARSET Function Parameters Parameter Description doc DOM document Usage Notes For a newly parsed document, we return the database characterset. Once the SETCHARSET Procedure is called with a non- NULL value for charset , that charset is returned.