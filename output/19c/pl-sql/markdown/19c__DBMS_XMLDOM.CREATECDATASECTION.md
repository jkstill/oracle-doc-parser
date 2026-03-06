---
id: 19c__DBMS_XMLDOM.CREATECDATASECTION
name: DBMS_XMLDOM.CREATECDATASECTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATECDATASECTION

This function creates a DOMCDATASECTION node.

## Syntax

```sql
DBMS_XMLDOM.CREATECDATASECTION(
   doc     IN      DOMDOCUMENT,
   data    IN      VARCHAR2)
 RETURN DOMCDATASECTION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| data | VARCHAR2) | IN | Content of the DOMCDATASECTION node |

**Returns:** `DOMCDATASECTION`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.CREATECDATASECTION( doc IN DOMDOCUMENT, data IN VARCHAR2) RETURN DOMCDATASECTION; Parameters Table 204-27 CREATECDATASECTION Function Parameters Parameter Description doc DOMDOCUMENT data Content of the DOMCDATASECTION node