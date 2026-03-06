---
id: 19c__DBMS_XMLDOM.CREATEPROCESSINGINSTRUCTION
name: DBMS_XMLDOM.CREATEPROCESSINGINSTRUCTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.CREATEPROCESSINGINSTRUCTION

This function creates a DOMPROCESSINGINSTRUCTION node.

## Syntax

```sql
DBMS_XMLDOM.CREATEPROCESSINGINSTRUCTION(
   doc       IN      DOMDocument,
   target    IN      VARCHAR2,
   data      IN      VARCHAR2)
 RETURN DOMPROCESSINGINSTRUCTION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDocument | IN | DOMDOCUMENT |
| target | VARCHAR2 | IN | Target of the new processing instruction |
| data | VARCHAR2) | IN | Content data of the new processing instruction |

**Returns:** `DOMPROCESSINGINSTRUCTION`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.CREATEPROCESSINGINSTRUCTION( doc IN DOMDocument, target IN VARCHAR2, data IN VARCHAR2) RETURN DOMPROCESSINGINSTRUCTION; Parameters Table 204-33 CREATEPROCESSINGINSTRUCTION Function Parameters Parameter Description doc DOMDOCUMENT target Target of the new processing instruction data Content data of the new processing instruction