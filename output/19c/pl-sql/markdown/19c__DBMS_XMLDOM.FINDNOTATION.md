---
id: 19c__DBMS_XMLDOM.FINDNOTATION
name: DBMS_XMLDOM.FINDNOTATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.FINDNOTATION

This function finds the notation in the specified DTD, and returns it, if found.

## Syntax

```sql
DBMS_XMLDOM.FINDNOTATION(
   dt        IN     DOMDocumentType,
   name      IN     VARCHAR2) 
 RETURN DOMNOTATION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dt | DOMDocumentType | IN | The DTD |
| name | VARCHAR2) | IN | The notation to find |

**Returns:** `DOMNOTATION`

## Usage Notes

See Also: DOMDocumentType Subprograms See Also: DOMDocumentType Subprograms Syntax DBMS_XMLDOM.FINDNOTATION( dt IN DOMDocumentType, name IN VARCHAR2) RETURN DOMNOTATION; Parameters Table 204-37 FINDNOTATION Function Parameters Parameter Description dt The DTD name The notation to find