---
id: 19c__DBMS_XMLDOM.GETSTANDALONE
name: DBMS_XMLDOM.GETSTANDALONE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETSTANDALONE

This function returns the standalone property associated with the DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.GETSTANDALONE(
   doc       IN     DOMDOCUMENT)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT) | IN | DOMDOCUMENT . |

**Returns:** `VARCHAR2`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.GETSTANDALONE( doc IN DOMDOCUMENT) RETURN VARCHAR2; Parameters Table 204-81 GETSTANDALONE Function Parameters Parameter Description doc DOMDOCUMENT .