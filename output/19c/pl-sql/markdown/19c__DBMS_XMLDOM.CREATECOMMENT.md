---
id: 19c__DBMS_XMLDOM.CREATECOMMENT
name: DBMS_XMLDOM.CREATECOMMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATECOMMENT

This function creates a DOMCOMMENT node.

## Syntax

```sql
DBMS_XMLDOM.CREATECOMMENT(
   doc      IN      DOMDOCUMENT,
   data     IN      VARCHAR2)
 RETURN DOMCOMMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| data | VARCHAR2) | IN | Content of the DOMComment node |

**Returns:** `DOMCOMMENT`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.CREATECOMMENT( doc IN DOMDOCUMENT, data IN VARCHAR2) RETURN DOMCOMMENT; Parameters Table 204-28 CREATECOMMENT Function Parameters Parameter Description doc DOMDOCUMENT data Content of the DOMComment node