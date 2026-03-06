---
id: 19c__DBMS_XMLDOM.GETDOCTYPE
name: DBMS_XMLDOM.GETDOCTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETDOCTYPE

This function returns the DTD associated to the DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.GETDOCTYPE(
   doc      IN     DOMDOCUMENT)
RETURN DOMDOCUMENTTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT) | IN | DOMDOCUMENT |

**Returns:** `DOMDOCUMENTTYPE`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.GETDOCTYPE( doc IN DOMDOCUMENT) RETURN DOMDOCUMENTTYPE; Parameters Table 204-50 GETDOCTYPE Function Parameters Parameter Description doc DOMDOCUMENT