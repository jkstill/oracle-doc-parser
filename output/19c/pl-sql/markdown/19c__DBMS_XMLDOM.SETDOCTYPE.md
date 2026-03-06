---
id: 19c__DBMS_XMLDOM.SETDOCTYPE
name: DBMS_XMLDOM.SETDOCTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETDOCTYPE

Given a DOM document, this procedure creates a new DTD with the specified name, system id and public id and sets it in the document.

## Syntax

```sql
DBMS_XMLDOM.SETDOCTYPE(
  doc     IN   DOMDocument, 
  name    IN   VARCHAR2,
  sysid   IN   VARCHAR2, 
  pubid   IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDocument | IN | The document whose DTD has to be set |
| name | VARCHAR2 | IN | The name that the doctype needs to be initialized with |
| sysid | VARCHAR2 | IN | The system ID that the doctype needs to be initialized with |
| pubid | VARCHAR2) | IN | The public ID that the doctype needs to be initialized with |

## Usage Notes

This DTD can later be retrieved using the GETDOCTYPE Function . Syntax DBMS_XMLDOM.SETDOCTYPE( doc IN DOMDocument, name IN VARCHAR2, sysid IN VARCHAR2, pubid IN VARCHAR2); Parameters Table 204-123 SETDOCTYPE Procedure Parameters Parameter Description doc The document whose DTD has to be set name The name that the doctype needs to be initialized with sysid The system ID that the doctype needs to be initialized with pubid The public ID that the doctype needs to be initialized with