---
id: 19c__DBMS_XMLDOM.MAKEATTR
name: DBMS_XMLDOM.MAKEATTR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEATTR

This function casts a specified DOMNODE to a DOMATTR , and returns the DOMATTR .

## Syntax

```sql
DBMS_XMLDOM.MAKEATTR(
   n       IN     DOMNODE)
 RETURN DOMATTR;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMATTR`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEATTR( n IN DOMNODE) RETURN DOMATTR; Parameters Table 204-96 MAKEATTR Function Parameters Parameter Description n DOMNODE to cast