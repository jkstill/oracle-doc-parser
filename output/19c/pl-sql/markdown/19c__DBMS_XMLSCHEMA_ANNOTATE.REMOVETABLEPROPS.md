---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVETABLEPROPS
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVETABLEPROPS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVETABLEPROPS

This procedure removes the table storage properties from the CREATE TABLE statement.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVETABLEPROPS (
   xmlschema            IN OUT  XMLTYPE,
   globalElementName    IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN OUT | XML schema to be annotated |
| globalElementName | VARCHAR2) | IN | Name of the global element in the schema |
| globalObject |  |  | Global object (global complex type or global element) |
| globalObjectName |  |  | Name of the global object |
| localElementName |  |  | Name of a local element that descends from the global element |

## Usage Notes

This procedure is overloaded. Each overload has different parameter requirements as indicated. Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVETABLEPROPS ( xmlschema IN OUT XMLTYPE, globalElementName IN VARCHAR2); DBMS_XMLSCHEMA_ANNOTATE.REMOVETABLEPROPS ( xmlschema IN OUT XMLTYPE, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localElementName IN VARCHAR2); Parameters Table 211-18 REMOVETABLEPROPS Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalElementName Name of the global element in the schema globalObject Global object (global complex type or global element) globalObjectName Name of the global object localElementName Name of a local element that descends from the global element Usage Notes This procedure reverses the SETTABLEPROPS Procedure .