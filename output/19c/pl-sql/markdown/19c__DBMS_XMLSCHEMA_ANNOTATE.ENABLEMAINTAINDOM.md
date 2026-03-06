---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.ENABLEMAINTAINDOM
name: DBMS_XMLSCHEMA_ANNOTATE.ENABLEMAINTAINDOM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.ENABLEMAINTAINDOM

This overloaded procedure sets the DOM fidelity attribute to TRUE .

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.ENABLEMAINTAINDOM (
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

There are two overloads. The first sets DOM fidelity attribute to TRUE for all complex types, and the second sets it to TRUE for the named complex type. Syntax DBMS_XMLSCHEMA_ANNOTATE.ENABLEMAINTAINDOM ( xmlschema IN OUT XMLType, overwrite IN BOOLEAN default TRUE); DBMS_XMLSCHEMA_ANNOTATE.ENABLEMAINTAINDOM ( xmlschema IN OUT XMLType, complexTypeName IN VARCHAR2, overwrite IN BOOLEAN default TRUE); Parameters Table 211-6 ENABLEMAINTAINDOM Procedure Parameters Parameter Description xmlschema The XML schema to be annotated complexTypeName The name of the complex type overwrite A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE