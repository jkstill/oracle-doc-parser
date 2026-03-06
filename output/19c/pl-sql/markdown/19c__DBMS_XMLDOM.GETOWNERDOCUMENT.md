---
id: 19c__DBMS_XMLDOM.GETOWNERDOCUMENT
name: DBMS_XMLDOM.GETOWNERDOCUMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETOWNERDOCUMENT

This function retrieves the Document object associated with this node. This is also the Document object used to create new nodes. When this node is a Document or a Document Type that is not used with any Document yet, this is NULL .

## Syntax

```sql
DBMS_XMLDOM.GETOWNERDOCUMENT(
   n       IN     DOMNODE)
 RETURN DOMDOCUMENT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE |

**Returns:** `DOMDOCUMENT`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.GETOWNERDOCUMENT( n IN DOMNODE) RETURN DOMDOCUMENT; Parameters Table 204-72 GETOWNERDOCUMENT Function Parameters Parameter Description n DOMNODE