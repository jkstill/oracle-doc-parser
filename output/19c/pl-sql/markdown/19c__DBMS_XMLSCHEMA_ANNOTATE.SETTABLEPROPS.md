---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS
name: DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS

This procedure specifies properties in the TABLE storage clause that is appended to the default CREATE TABLE statement.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS (
   xmlschema            IN OUT  XMLType, 
   globalElementName    IN      VARCHAR2, 
   tableProps           IN      VARCHAR2,    
   overwrite            IN      BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | XML schema to be annotated |
| globalElementName | VARCHAR2 | IN | Name of the global element in the schema |
| tableProps | VARCHAR2 | IN | Table properties |
| globalObject |  |  | Global object (global complex type or global element) |
| globalObjectName |  |  | Name of the global object |
| localElementName |  |  | Name of a local element that descends from the global element |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

There are two overloads with different parameter requirements, as indicated: Syntax DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS ( xmlschema IN OUT XMLType, globalElementName IN VARCHAR2, tableProps IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS ( xmlschema IN OUT XMLTYPE, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localElementName IN VARCHAR2, tableProps IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-28 SETTABLEPROPS Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalElementName Name of the global element in the schema tableProps Table properties globalObject Global object (global complex type or global element) globalObjectName Name of the global object localElementName Name of a local element that descends from the global element overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Example The purchaseOrder element will have an annotation similar to xdb:tableProps="CACHE" . DECLARE xml_schema XMLTYPE;BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.SETTABLEPROPS(xml_schema, 'purchaseOrder' ,'CACHE'); UPDATE annotation_tab SET out = xml_schema;END; /