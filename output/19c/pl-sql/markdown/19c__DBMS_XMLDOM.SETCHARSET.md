---
id: 19c__DBMS_XMLDOM.SETCHARSET
name: DBMS_XMLDOM.SETCHARSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETCHARSET

This function sets the characterset of the DOM document.

## Syntax

```sql
DBMS_XMLDOM.SETCHARSET(
   doc      IN    DOMDocument,
   charset  IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDocument | IN | DOM document |
| charset | VARCHAR2) | IN | Characterset |

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.SETCHARSET( doc IN DOMDocument, charset IN VARCHAR2); Parameters Table 204-121 SETCHARSET Procedure Parameters Parameter Description doc DOM document charset Characterset Usage Notes This is used for WRITETOFILE Procedures if not explicitly specified at that time.