---
id: 19c__DBMS_XMLDOM.CREATEELEMENT
name: DBMS_XMLDOM.CREATEELEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATEELEMENT

This function creates a DOMELEMENT .

## Syntax

```sql
DBMS_XMLDOM.CREATEELEMENT(
   doc        IN      DOMDOCUMENT,
   tagName    IN      VARCHAR2)
 RETURN DOMELEMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| tagName | VARCHAR2) | IN | Tagname for new DOMELEMENT |
| ns |  |  | Namespace |

**Returns:** `DOMELEMENT`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax Creates a DOMElement with specified name: DBMS_XMLDOM.CREATEELEMENT( doc IN DOMDOCUMENT, tagName IN VARCHAR2) RETURN DOMELEMENT; Creates a DOMElement with specified name and namespace URI: DBMS_XMLDOM.CREATEELEMENT( doc IN DOMDOCUMENT, tagName IN VARCHAR2, ns IN VARCHAR2) RETURN DOMELEMENT; Parameters Table 204-31 CREATEELEMENT Function Parameters Parameter Description doc DOMDOCUMENT tagName Tagname for new DOMELEMENT ns Namespace