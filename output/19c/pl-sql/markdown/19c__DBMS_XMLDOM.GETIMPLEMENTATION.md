---
id: 19c__DBMS_XMLDOM.GETIMPLEMENTATION
name: DBMS_XMLDOM.GETIMPLEMENTATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETIMPLEMENTATION

This function returns the DOMIMPLEMENTATION object that handles this DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.GETIMPLEMENTATION(
   doc      IN     DOMDOCUMENT)
 RETURN DOMIMPLEMENTATION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT) | IN | DOMDOCUMENT |

**Returns:** `DOMIMPLEMENTATION`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.GETIMPLEMENTATION( doc IN DOMDOCUMENT) RETURN DOMIMPLEMENTATION; Parameters Table 204-56 GETIMPLEMENTATION Function Parameters Parameter Description doc DOMDOCUMENT