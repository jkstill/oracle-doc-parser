---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPEMAPPING
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPEMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPEMAPPING

This procedure removes the SQL type mapping for the given schema type.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPEMAPPING (
   xmlschema        IN OUT  XMLTYPE,
   schemaTypeName   IN      VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN OUT | XML schema to be annotated |
| schemaTypeName | VARCHAR2) | IN | Name of the schema type |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLTYPEMAPPING ( xmlschema IN OUT XMLTYPE, schemaTypeName IN VARCHAR2); Parameters Table 211-17 REMOVESQLTYPEMAPPING Procedure Parameters Parameter Description xmlschema XML schema to be annotated schemaTypeName Name of the schema type Usage Notes This procedure reverses the SETSQLTYPEMAPPING Procedure .