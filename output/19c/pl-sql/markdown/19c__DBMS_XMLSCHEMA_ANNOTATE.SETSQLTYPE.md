---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPE
name: DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPE

This procedure assigns a SQL type to a global object.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPE (
   xmlschema            IN OUT   XMLTYPE,
   globalElementName    IN       VARCHAR2, 
   sqlType              IN       VARCHAR2, 
   overwrite            IN       BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN OUT | XML schema to be annotated |
| globalObject |  |  | Global object (global complex type or global element) |
| globalObjectName |  |  | Name of the global object |
| globalElementName | VARCHAR2 | IN | Name of the global element |
| localObject |  |  | Object descended from the global object |
| localObjectName |  |  | Name of the local object |
| sqlType | VARCHAR2 | IN | SQL type assigned to the named global element |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

There are two overloads. The first overload assigns a SQL Type to a global object, such as a global element or global complex type and the second to a local object. Syntax DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPE ( xmlschema IN OUT XMLTYPE, globalElementName IN VARCHAR2, sqlType IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); DBMS_XMLSCHEMA_ANNOTATE.SETSQLTYPE ( xmlschema IN OUT XMLTYPE, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localObject IN VARCHAR2, localObjectName IN VARCHAR2, sqlType IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-26 SETSQLTYPE Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalObject Global object (global complex type or global element) globalObjectName Name of the global object globalElementName Name of the global element localObject Object descended from the global object localObjectName Name of the local object sqlType SQL type assigned to the named global element overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Example The purchaseOrder element will have an annotation similar to xdb:SQLType="PO_SQLTYPE" and the shipTo element has one similar to xdb:SQLType="VARCHAR" . DECLARE xml_schema xmltype; BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.setSQLType (xml_schema, 'purchaseOrder', 'PO_SQLTYPE'); UPDATE annotation_tab SET out = xml_schema; END; / DECLARE xml_schema xmltype;BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.setSQLType (xml_schema, 'element','purchaseOrder', 'element' ,'shipTo', 'VARCHAR'); UPDATE annotation_tab SET out = xml_schema;END; /