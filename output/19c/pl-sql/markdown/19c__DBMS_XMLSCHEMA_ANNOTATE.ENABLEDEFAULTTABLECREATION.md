---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION
name: DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION

This procedure enables the creation of ALL top level tables by removing the empty default table name annotation.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION (
   xmlschema            IN OUT  XMLTYPE);

DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION (
   xmlschema            IN OUT  XMLTYPE,
   globalElementName    IN      VARCHAR2););
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE) | IN OUT | The XML schema to be annotated |
| gloablElementName |  |  | Name of the global element in the schema |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION ( xmlschema IN OUT XMLTYPE); DBMS_XMLSCHEMA_ANNOTATE.ENABLEDEFAULTTABLECREATION ( xmlschema IN OUT XMLTYPE, globalElementName IN VARCHAR2);); Parameters Table 211-5 ENABLEDEFAULTTABLECREATION Procedure Parameters Parameter Description xmlschema The XML schema to be annotated gloablElementName Name of the global element in the schema Usage Notes This procedure does not affect elements that have a default table name.