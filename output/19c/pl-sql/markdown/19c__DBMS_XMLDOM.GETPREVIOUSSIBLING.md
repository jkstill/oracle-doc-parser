---
id: 19c__DBMS_XMLDOM.GETPREVIOUSSIBLING
name: DBMS_XMLDOM.GETPREVIOUSSIBLING
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETPREVIOUSSIBLING

This function retrieves the node immediately preceding this node. If there is no such node, this returns NULL .

## Syntax

```sql
DBMS_XMLDOM.GETPREVIOUSSIBLING(
   n       IN     DOMNODE)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETPREVIOUSSIBLING( n IN DOMNODE) RETURN DOMNODE; Parameters Table 204-76 GETPREVIOUSSIBLING Function Parameters Parameter Description n DOMNODE