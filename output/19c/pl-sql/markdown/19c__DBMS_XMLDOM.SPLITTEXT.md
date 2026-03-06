---
id: 19c__DBMS_XMLDOM.SPLITTEXT
name: DBMS_XMLDOM.SPLITTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SPLITTEXT

This function breaks this DOMTEXT node into two DOMTEXT nodes at the specified offset.

## Syntax

```sql
DBMS_XMLDOM.SPLITTEXT(
   t        IN     DOMTEXT,
   offset   IN     NUMBER)
 RETURN DOMText;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| t | DOMTEXT | IN | DOMTEXT |
| offset | NUMBER) | IN | Offset at which to split |

**Returns:** `DOMText`

## Usage Notes

See Also: DBMS_XMLDOM DOMText Subprograms See Also: DBMS_XMLDOM DOMText Subprograms Syntax DBMS_XMLDOM.SPLITTEXT( t IN DOMTEXT, offset IN NUMBER) RETURN DOMText; Parameters Table 204-132 SPLITTEXT Function Parameters Parameter Description t DOMTEXT offset Offset at which to split