---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPE
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPE

This procedure removes a SQL type.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPE (
   xmlschema in out XMLType,  
   globalElementName   IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | in out | XML schema to be annotated. |
| globalObject |  |  | Global object (global complex type or global element) |
| globalElementName | VARCHAR2) | IN | Name of the global element. |
| globalObjectName |  |  | Name of the global object |
| localObject |  |  | Object descended from the global object |
| localObjectName |  |  | Name of the local object |

## Usage Notes

The first overload removes a SQL type from a global element and the second overload removes the type from a global element inside the complex type. Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPE ( xmlschema in out XMLType, globalElementName IN VARCHAR2); DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPE ( xmlschema IN OUT XMLTYPE, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localObject IN VARCHAR2, localObjectName IN VARCHAR2); Parameters Table 211-16 REMOVESQLTYPE Procedure Parameters Parameter Description xmlschema XML schema to be annotated. globalObject Global object (global complex type or global element) globalElementName Name of the global element. globalObjectName Name of the global object localObject Object descended from the global object localObjectName Name of the local object Usage Notes This procedure reverses the SETSQLTYPE Procedure .