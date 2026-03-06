---
id: 19c__DBMS_XMLDOM.GETENTITIES
name: DBMS_XMLDOM.GETENTITIES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETENTITIES

This function retrieves a DOMNAMEDNODEMAP containing the general entities, both external and internal, declared in the DTD.

## Syntax

```sql
DBMS_XMLDOM.GETENTITIES(
   dt      IN     DOMDocumentType)
 RETURN DOMNAMEDNODEMAP;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dt | DOMDocumentType) | IN | DOMDOCUMENTTYPE |

**Returns:** `DOMNAMEDNODEMAP`

## Usage Notes

See Also: DOMDocumentType Subprograms See Also: DOMDocumentType Subprograms Syntax DBMS_XMLDOM.GETENTITIES( dt IN DOMDocumentType) RETURN DOMNAMEDNODEMAP; Parameters Table 204-53 GETENTITIES Function Parameters Parameter Description dt DOMDOCUMENTTYPE