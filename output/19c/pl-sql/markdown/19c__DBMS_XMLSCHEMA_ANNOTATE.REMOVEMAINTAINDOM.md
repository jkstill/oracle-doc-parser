---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVEMAINTAINDOM
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVEMAINTAINDOM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVEMAINTAINDOM

This procedure removes all annotations used to maintain DOM from the given schema.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVEMAINTAINDOM (
   xmlschema    IN OUT XMLType);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType) | IN OUT | The XML schema to be annotated |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVEMAINTAINDOM ( xmlschema IN OUT XMLType); Parameters Table 211-12 REMOVEMAINTAINDOM Procedure Parameters Parameter Description xmlschema The XML schema to be annotated