---
id: 19c__DBMS_XMLDOM.GETXMLTYPE
name: DBMS_XMLDOM.GETXMLTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETXMLTYPE

This function returns the XMLType associated with the DOMDOCUMENT .

## Syntax

```sql
DBMS_XMLDOM.GETXMLTYPE(
   doc       IN     DOMDOCUMENT)
 RETURN SYS.XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| doc | DOMDOCUMENT) | IN | DOMDOCUMENT |

**Returns:** `SYS.XMLTYPE`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax DBMS_XMLDOM.GETXMLTYPE( doc IN DOMDOCUMENT) RETURN SYS.XMLTYPE; Parameters Table 204-86 GETXMLTYPE Function Parameters Parameter Description doc DOMDOCUMENT