---
id: 19c__DBMS_XMLDOM.SETPREFIX
name: DBMS_XMLDOM.SETPREFIX
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETPREFIX

This procedure sets the namespace prefix for this node to the specified value.

## Syntax

```sql
DBMS_XMLDOM.SETPREFIX(
   n       IN     DOMNODE,
   prefix  IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE | IN | DOMNODE |
| prefix | VARCHAR2) | IN | The value for the namespace prefix of the node |

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.SETPREFIX( n IN DOMNODE, prefix IN VARCHAR2); Parameters Table 204-128 SETPREFIX Procedure Parameters Parameter Description n DOMNODE prefix The value for the namespace prefix of the node