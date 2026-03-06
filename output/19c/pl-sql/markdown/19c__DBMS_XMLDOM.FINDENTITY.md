---
id: 19c__DBMS_XMLDOM.FINDENTITY
name: DBMS_XMLDOM.FINDENTITY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.FINDENTITY

This function finds an entity in the specified DTD, and returns that entity if found.

## Syntax

```sql
DBMS_XMLDOM.FINDENTITY(
   dt     IN     DOMDOCUMENTTYPE,
   name   IN     VARCHAR2,
   par    IN     BOOLEAN) 
 RETURN  DOMENTITY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dt | DOMDOCUMENTTYPE | IN | The DTD |
| name | VARCHAR2 | IN | Entity to find |
| par | BOOLEAN) | IN | Flag to indicate type of entity; TRUE for parameter entity and FALSE for normal entity |

**Returns:** `DOMENTITY`

## Usage Notes

See Also: DOMDocumentType Subprograms See Also: DOMDocumentType Subprograms Syntax DBMS_XMLDOM.FINDENTITY( dt IN DOMDOCUMENTTYPE, name IN VARCHAR2, par IN BOOLEAN) RETURN DOMENTITY; Parameters Table 204-36 FINDENTITY Function Parameters Parameter Description dt The DTD name Entity to find par Flag to indicate type of entity; TRUE for parameter entity and FALSE for normal entity