---
id: 19c__DBMS_XMLDOM.SETNODEVALUE
name: DBMS_XMLDOM.SETNODEVALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETNODEVALUE

This procedure sets the value of this node, depending on its type. When it is defined to be NULL , setting it has no effect.

## Syntax

```sql
DBMS_XMLDOM.SETNODEVALUE(
   n         IN     DOMNODE,
   nodeValue IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNode |
| nodeValue | VARCHAR2) | IN | The value to which node is set |

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.SETNODEVALUE( n IN DOMNODE, nodeValue IN VARCHAR2); Parameters Table 204-125 SETNODEVALUE Procedure Parameters Parameter Description n DOMNode nodeValue The value to which node is set