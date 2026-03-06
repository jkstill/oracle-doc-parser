---
id: 19c__DBMS_XSLPROCESSOR.VALUEOF
name: DBMS_XSLPROCESSOR.VALUEOF
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSLPROCESSOR
tags: [dbms_xslprocessor]
source_file: DBMS_XSLPROCESSOR.html
---

# DBMS_XSLPROCESSOR.VALUEOF

This subprogram retrieves the value of the first node from the tree that matches the given pattern. You can use either a function or a procedure.

## Syntax

```sql
DBMS_XSLPROCESSOR.VALUEOF(
  n           IN    DBMS_XMLDOM.DOMNODE,
  pattern     IN    VARCHAR2,
  namespace   IN    VARCHAR2 := NULL)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | DBMS_XMLDOM.DOMNODE | IN | Node whose value is being retrieved |
| pattern | VARCHAR2 | IN | Pattern to use |
| val |  |  | Retrieved value |
| namespace | VARCHAR2 | IN | Namespace to use |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XSLPROCESSOR.VALUEOF( n IN DBMS_XMLDOM.DOMNODE, pattern IN VARCHAR2, namespace IN VARCHAR2 := NULL) RETURN VARCHAR2; DBMS_XSLPROCESSOR.VALUEOF( n IN DBMS_XMLDOM.DOMNODE, pattern IN VARCHAR2, val OUT VARCHAR2, namespace IN VARCHAR2 := NULL); Parameters Table 216-16 VALUEOF Function and Procedure Parameters Parameter Description n Node whose value is being retrieved pattern Pattern to use val Retrieved value namespace Namespace to use