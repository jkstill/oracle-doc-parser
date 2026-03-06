---
id: 19c__DBMS_XMLDOM.MAKEENTITYREFERENCE
name: DBMS_XMLDOM.MAKEENTITYREFERENCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEENTITYREFERENCE

This function casts a specified DOMNODE to a DOMENTITYREFERENCE , and returns the DOMENTITYREFERENCE .

## Syntax

```sql
DBMS_XMLDOM.MAKEENTITYREFERENCE(
   n       IN     DOMNODE)
 RETURN DOMENTITYREFERENCE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMENTITYREFERENCE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEENTITYREFERENCE( n IN DOMNODE) RETURN DOMENTITYREFERENCE; Parameters Table 204-105 MAKEENTITYREFERENCE Function Parameters Parameter Description n DOMNODE to cast