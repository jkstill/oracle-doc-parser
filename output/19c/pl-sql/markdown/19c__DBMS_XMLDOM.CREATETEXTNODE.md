---
id: 19c__DBMS_XMLDOM.CREATETEXTNODE
name: DBMS_XMLDOM.CREATETEXTNODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATETEXTNODE

This function creates a DOMTEXT node.

## Syntax

```sql
DBMS_XMLDOM.CREATETEXTNODE(
   doc      IN     DOMDocument,
   data     IN     VARCHAR2)
 RETURN DOMTEXT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDocument | IN | DOMDOCUMENT |
| data | VARCHAR2) | IN | Content of the DOMText node |

**Returns:** `DOMTEXT`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.CREATETEXTNODE( doc IN DOMDocument, data IN VARCHAR2) RETURN DOMTEXT; Parameters Table 204-34 CREATETEXTNODE Function Parameters Parameter Description doc DOMDOCUMENT data Content of the DOMText node