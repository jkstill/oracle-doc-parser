---
id: 19c__DBMS_XMLDOM.SETVALUE
name: DBMS_XMLDOM.SETVALUE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.SETVALUE

This procedure sets the value of the attribute.

## Syntax

```sql
DBMS_XMLDOM.SETVALUE(
   a       IN     DOMATTR,
   value   IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| a | DOMATTR | IN | DOMATTR |
| value | VARCHAR2) | IN | The value to which to set the attribute |

## Usage Notes

See Also: DOMAttr Subprograms See Also: DOMAttr Subprograms Syntax DBMS_XMLDOM.SETVALUE( a IN DOMATTR, value IN VARCHAR2); Parameters Table 204-130 SETVALUE Procedure Parameters Parameter Description a DOMATTR value The value to which to set the attribute