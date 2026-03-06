---
id: 19c__DBMS_XMLDOM.NEWDOMDOCUMENT
name: DBMS_XMLDOM.NEWDOMDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.NEWDOMDOCUMENT

This function returns a new DOMDOCUMENT instance.

## Syntax

```sql
DBMS_XMLDOM.NEWDOMDOCUMENT
 RETURN DOMDOCUMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmldoc |  |  | XMLType source for the DOMDOCUMENT |
| cl |  |  | CLOB source for the DOMDOCUMENT |

**Returns:** `DOMDOCUMENT`

## Usage Notes

See Also: DOMDocument Subprograms See Also: DOMDocument Subprograms Syntax Returns a new DOMDOCUMENT instance: DBMS_XMLDOM.NEWDOMDOCUMENT RETURN DOMDOCUMENT; Returns a new DOMDOCUMENT instance created from the specified XMLType object: DBMS_XMLDOM.NEWDOMDOCUMENT( xmldoc IN SYS.XMLTYPE) RETURN DOMDOCUMENT; Returns a new DOMDOCUMENT instance created from the specified CLOB : DBMS_XMLDOM.NEWDOMDOCUMENT( cl IN CLOB) RETURN DOMDOCUMENT; Parameters Table 204-110 NEWDOMDOCUMENT Function Parameters Parameter Description xmldoc XMLType source for the DOMDOCUMENT cl CLOB source for the DOMDOCUMENT