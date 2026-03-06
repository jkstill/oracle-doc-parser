---
id: 19c__DBMS_XMLDOM.MAKETEXT
name: DBMS_XMLDOM.MAKETEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKETEXT

This function casts a specified DOMNODE to a DOMTEXT , and returns the DOMTEXT .

## Syntax

```sql
DBMS_XMLDOM.MAKETEXT(
   n       IN     DOMNODE)
 RETURN DOMTEXT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMTEXT`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKETEXT( n IN DOMNODE) RETURN DOMTEXT; Parameters Table 204-109 MAKETEXT Function Parameters Parameter Description n DOMNODE to cast