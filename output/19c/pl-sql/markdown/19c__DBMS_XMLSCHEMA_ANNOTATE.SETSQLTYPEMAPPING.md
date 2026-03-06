---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPEMAPPING
name: DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPEMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPEMAPPING

This procedure defines a mapping of schema type and SQL type.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPEMAPPING (
   xmlschema         IN OUT   XMLType, 
   schemaTypeName    IN       VARCHAR2, 
   sqlTypeName       IN       VARCHAR2, 
   overwrite         IN       BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | XML schema to be annotated |
| schemaTypeName | VARCHAR2 | IN | Schema type |
| sqlType Name |  |  | Name of the SQL type |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE |

## Usage Notes

If you use this procedure, you do not need to call the SETSQLTYPE procedure on all instances of the schema type; instead the procedure traverses the schema and assigns the SQL type automatically. Syntax DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPEMAPPING ( xmlschema IN OUT XMLType, schemaTypeName IN VARCHAR2, sqlTypeName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-27 SETSQLTYPEMAPPING Procedure Parameters Parameter Description xmlschema XML schema to be annotated schemaTypeName Schema type sqlType Name Name of the SQL type overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE Example The attribute orderDate will have an annotation similar to xdb:SQLType="DATE" . declare xml_schema xmltype;beginSELECT out INTO xml_schema FROM annotation_tab;DBMS_XMLSCHEMA_ANNOTATE.setSQLTypeMapping (xml_schema, 'date', 'DATE');UPDATE annotation_tab SET out = xml_schema;end; /