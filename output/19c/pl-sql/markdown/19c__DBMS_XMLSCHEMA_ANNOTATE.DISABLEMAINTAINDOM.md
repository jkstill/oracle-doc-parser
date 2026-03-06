---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.DISABLEMAINTAINDOM
name: DBMS_XMLSCHEMA_ANNOTATE.DISABLEMAINTAINDOM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.DISABLEMAINTAINDOM

This procedure sets the DOM fidelity attribute to FALSE .

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.DISABLEMAINTAINDOM (
   xmlschema       IN OUT XMLType, 
   overwrite       IN BOOLEAN default TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | The XML schema to be annotated |
| complexTypeName |  |  | The name of the complex type |
| overwrite | BOOLEAN | IN | A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE |

## Usage Notes

There are two overloads. The first sets DOM fidelity attribute to FALSE for all complex types, and the second sets it to FALSE for the named complex type. This is equivalent to adding xdb:maintainDOM="false" on all or specified complex types respectively. Syntax DBMS_XMLSCHEMA_ANNOTATE.DISABLEMAINTAINDOM ( xmlschema IN OUT XMLType, overwrite IN BOOLEAN default TRUE); DBMS_XMLSCHEMA_ANNOTATE.DISABLEMAINTAINDOM ( xmlschema IN OUT XMLType, complexTypeName IN VARCHAR2, overwrite IN BOOLEAN default TRUE); Parameters Table 211-4 DISABLEMAINTAINDOM Procedure Parameters Parameter Description xmlschema The XML schema to be annotated complexTypeName The name of the complex type overwrite A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE