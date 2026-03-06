---
id: 19c__DBMS_XMLDOM.GETNAMEDITEM
name: DBMS_XMLDOM.GETNAMEDITEM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETNAMEDITEM

GETNAMEDITEM retrieves a node specified by name.

## Syntax

```sql
DBMS_XMLDOM.GETNAMEDITEM(
   nnm    IN  DOMNAMEDNODEMAP,
   name   IN  VARCHAR2)
 RETURN DOMNODE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| nnm | DOMNAMEDNODEMAP | IN | DOMNAMEDNODEMAP |
| name | VARCHAR2) | IN | Name of the item to be retrieved |
| ns |  |  | Namespace |

**Returns:** `DOMNODE`

## Usage Notes

See Also: DOMNamedNodeMap Subprograms See Also: DOMNamedNodeMap Subprograms Syntax Retrieves a node specified by name: DBMS_XMLDOM.GETNAMEDITEM( nnm IN DOMNAMEDNODEMAP, name IN VARCHAR2) RETURN DOMNODE; Retrieves a node specified by name and namespace URI: DBMS_XMLDOM.GETNAMEDITEM( nnm IN DOMNAMEDNODEMAP, name IN VARCHAR2, ns IN VARCHAR2) RETURN DOMNODE; Parameters Table 204-61 GETNAMEDITEM Function Parameters Parameter Description nnm DOMNAMEDNODEMAP name Name of the item to be retrieved ns Namespace