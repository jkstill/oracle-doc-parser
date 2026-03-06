---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLCOLLTYPE
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLCOLLTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLCOLLTYPE

This procedure removes a SQL collection type.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLCOLLTYPE (
   xmlschema   IN OUT XMLType, 
   elementName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | The XML schema to be annotated |
| elementName | VARCHAR2) | IN | The element name |
| globalObject |  |  | The global object (global complex type or global element) |
| globalName |  |  | The name of the global object |
| localElementName |  |  | The name of a local element that descends from the global element |

## Usage Notes

The first overload removes the SQL collection type corresponding to the named element and the second overload removes the type from the XML element inside the complex type. Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLCOLLTYPE ( xmlschema IN OUT XMLType, elementName IN VARCHAR2); DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLCOLLTYPE ( xmlschema IN OUT XMLType, globalObject IN VARCHAR2, globalName IN VARCHAR2, localElementName IN VARCHAR2); Parameters Table 211-14 REMOVESQLCOLLTYPE Procedure Parameters Parameter Description xmlschema The XML schema to be annotated elementName The element name globalObject The global object (global complex type or global element) globalName The name of the global object localElementName The name of a local element that descends from the global element Usage Notes This procedure reverses the SETSQLCOLLTYPE Procedure .