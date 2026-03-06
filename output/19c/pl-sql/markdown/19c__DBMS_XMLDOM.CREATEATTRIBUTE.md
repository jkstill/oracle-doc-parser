---
id: 19c__DBMS_XMLDOM.CREATEATTRIBUTE
name: DBMS_XMLDOM.CREATEATTRIBUTE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATEATTRIBUTE

This function creates a DOMATTR node.

## Syntax

```sql
DBMS_XMLDOM.CREATEATTRIBUTE(
   doc     IN    DOMDOCUMENT,
   name    IN    VARCHAR2)
 RETURN DOMATTR;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT | IN | DOMDOCUMENT |
| qname |  |  | New attribute qualified name |
| ns |  |  | Namespace |

**Returns:** `DOMATTR`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax Creates a DOMATTR with the specified name: DBMS_XMLDOM.CREATEATTRIBUTE( doc IN DOMDOCUMENT, name IN VARCHAR2) RETURN DOMATTR; Creates a DOMATTR with the specified name and namespace URI: DBMS_XMLDOM.CREATEATTRIBUTE( doc IN DOMDOCUMENT, qname IN VARCHAR2, ns IN VARCHAR2) RETURN DOMATTR; Parameters Table 204-26 CREATEATTRIBUTE Function Parameters Parameter Description doc DOMDOCUMENT qname New attribute qualified name ns Namespace