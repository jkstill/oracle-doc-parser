---
id: 19c__DBMS_XMLDOM.GETNOTATIONS
name: DBMS_XMLDOM.GETNOTATIONS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNOTATIONS

This function retrieves a DOMNAMEDNODEMAP containing the notations declared in the DTD.

## Syntax

```sql
DBMS_XMLDOM.GETNOTATIONS(
   dt       IN     DOMDOCUMENTTYPE)
 RETURN DOMNAMEDNODEMAP;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dt | DOMDOCUMENTTYPE) | IN | DOMDOCUMENTTYPE |

**Returns:** `DOMNAMEDNODEMAP`

## Usage Notes

See Also: DOMDocumentType Subprograms See Also: DOMDocumentType Subprograms Syntax DBMS_XMLDOM.GETNOTATIONS( dt IN DOMDOCUMENTTYPE) RETURN DOMNAMEDNODEMAP; Parameters Table 204-70 GETNOTATIONS Function Parameters Parameter Description dt DOMDOCUMENTTYPE