---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVEANYSTORAGE
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVEANYSTORAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVEANYSTORAGE

This procedure removes the setting of the SQL type from the ANY child of the complex type with the given name.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVEANYSTORAGE (
   xmlschema       IN OUT XMLType, 
   complexTypeName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | The XML schema to be annotated. |
| complexTypeName | VARCHAR2) | IN | The name of the complex type. |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVEANYSTORAGE ( xmlschema IN OUT XMLType, complexTypeName IN VARCHAR2); Parameters Table 211-10 REMOVEANYSTORAGE Procedure Parameters Parameter Description xmlschema The XML schema to be annotated. complexTypeName The name of the complex type. Usage Notes This procedure reverses the SETANYSTORAGE Procedure .