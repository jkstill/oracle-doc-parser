---
id: 19c__DBMS_XMLDOM.MAKECOMMENT
name: DBMS_XMLDOM.MAKECOMMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKECOMMENT

This function casts a specified DOMNODE to a DOMCOMMENT , and returns the DOMCOMMENT .

## Syntax

```sql
DBMS_XMLDOM.MAKECOMMENT(
   n       IN     DOMNODE)
 RETURN DOMCOMMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMCOMMENT`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKECOMMENT( n IN DOMNODE) RETURN DOMCOMMENT; Parameters Table 204-99 MAKECOMMENT Function Parameters Parameter Description n DOMNODE to cast