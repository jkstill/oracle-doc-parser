---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETANYSTORAGE
name: DBMS_XMLSCHEMA_ANNOTATE.SETANYSTORAGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETANYSTORAGE

This procedure assigns a SQL datatype to the ANY child of the complex type with the given name.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETANYSTORAGE )
   xmlschema       IN OUT  XMLType,
   complexTypeName IN      VARCHAR2,
   sqlTypeName     IN      VARCHAR2, 
   overwrite       IN      BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | XML schema to be annotated |
| complexTypeName | VARCHAR2 | IN | Name of the complex type |
| sqlTypeName | VARCHAR2 | IN | Name of the SQL type |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.SETANYSTORAGE ) xmlschema IN OUT XMLType, complexTypeName IN VARCHAR2, sqlTypeName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-20 SETANYSTORAGE Procedure Parameters Parameter Description xmlschema XML schema to be annotated complexTypeName Name of the complex type sqlTypeName Name of the SQL type overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Example The xsd:any child of complex type Items is assigned an annotation similar to xdb:SQLType="VARCHAR" . DECLARE xml_schema XMLTYPE;BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.setAnyStorage (xml_schema, 'Items', 'VARCHAR'); UPDATE annotation_tab SET out = xml_schema;END; /