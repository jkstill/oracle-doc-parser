---
id: 19c__DBMS_XMLDOM.MAKEENTITY
name: DBMS_XMLDOM.MAKEENTITY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEENTITY

This function casts a specified DOMNODE to a DOMENTITY , and returns the DOMENTITY .

## Syntax

```sql
DBMS_XMLDOM.MAKEENTITY(
   n       IN     DOMNODE)
 RETURN DOMENTITY;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMENTITY`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEENTITY( n IN DOMNODE) RETURN DOMENTITY; Parameters Table 204-104 MAKEENTITY Function Parameters Parameter Description n DOMNODE to cast