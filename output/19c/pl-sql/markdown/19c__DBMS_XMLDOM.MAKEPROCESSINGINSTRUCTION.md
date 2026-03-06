---
id: 19c__DBMS_XMLDOM.MAKEPROCESSINGINSTRUCTION
name: DBMS_XMLDOM.MAKEPROCESSINGINSTRUCTION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.MAKEPROCESSINGINSTRUCTION

This function casts a specified DOMNODE to a DOMPROCESSINGINSTRUCTION , and returns the Domprocessinginstruction .

## Syntax

```sql
DBMS_XMLDOM.MAKEPROCESSINGINSTRUCTION(
   n       IN     DOMNODE)
 RETURN DOMPROCESSINGINSTRUCTION;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DOMNODE) | IN | DOMNODE to cast |

**Returns:** `DOMPROCESSINGINSTRUCTION`

## Usage Notes

See Also: DOMNode Subprograms See Also: DOMNode Subprograms Syntax DBMS_XMLDOM.MAKEPROCESSINGINSTRUCTION( n IN DOMNODE) RETURN DOMPROCESSINGINSTRUCTION; Parameters Table 204-108 MAKEPROCESSINGINSTRUCTION Function Parameters Parameter Description n DOMNODE to cast