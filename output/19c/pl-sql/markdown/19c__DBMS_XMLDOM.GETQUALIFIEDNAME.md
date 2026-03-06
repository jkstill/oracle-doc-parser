---
id: 19c__DBMS_XMLDOM.GETQUALIFIEDNAME
name: DBMS_XMLDOM.GETQUALIFIEDNAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLDOM
tags: [dbms_xmldom]
source_file: DBMS_XMLDOM.html
---

# DBMS_XMLDOM.GETQUALIFIEDNAME

This function is overloaded. The specific forms of functionality are described along with the syntax declarations.

## Syntax

```sql
DBMS_XMLDOM.GETQUALIFIEDNAME(
   a        IN     DOMATTR)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| a | DOMATTR) | IN | DOMATTR |
| elem |  |  | DOMELEMENT |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Returns the qualified name of the DOMATTR (See Also: DOMAttr Subprograms ): DBMS_XMLDOM.GETQUALIFIEDNAME( a IN DOMATTR) RETURN VARCHAR2; Returns the qualified name of the DOMElement (See Also: DOMElement Subprograms ): DBMS_XMLDOM.GETQUALIFIEDNAME( elem IN DOMELEMENT) RETURN VARCHAR2; Parameters Table 204-78 GETQUALIFIEDNAME Functions Parameters Parameter Description a DOMATTR elem DOMELEMENT