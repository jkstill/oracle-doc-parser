---
id: 19c__DBMS_XMLDOM.CREATEDOCUMENT
name: DBMS_XMLDOM.CREATEDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATEDOCUMENT

This function creates a DOMDOCUMENT with specified namespace URI, root element name, DTD.

## Syntax

```sql
DBMS_XMLDOM.CREATEDOCUMENT(
   namespaceURI      IN     VARCHAR2,
   qualifiedName     IN     VARCHAR2,
   doctype           IN     DOMTYPE := NULL)
 RETURN DOMDOCUMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| namespaceURI | VARCHAR2 | IN | Namespace URI |
| qualifiedName | VARCHAR2 | IN | Root element name |
| doctype | DOMTYPE | IN | Document type |

**Returns:** `DOMDOCUMENT`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.CREATEDOCUMENT( namespaceURI IN VARCHAR2, qualifiedName IN VARCHAR2, doctype IN DOMTYPE := NULL) RETURN DOMDOCUMENT; Parameters Table 204-29 CREATEDOCUMENT Function Parameters Parameter Description namespaceURI Namespace URI qualifiedName Root element name doctype Document type