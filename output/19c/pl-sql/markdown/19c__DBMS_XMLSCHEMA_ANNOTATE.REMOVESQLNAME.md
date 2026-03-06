---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLNAME
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLNAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLNAME

This procedure removes a SQLNAME from a global element.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLNAME (
   xmlschema          IN OUT  XMLType,
   globalObject       IN      VARCHAR2, 
   globalObjectName   IN      VARCHAR2,
   localObject        IN      VARCHAR2, 
   localObjectName    IN      VARCHAR2, 
   sqlName            IN      VARCHAR2, 
   overwrite          IN      BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | XML schema to be annotated |
| globalObject | VARCHAR2 | IN | Global object (global complex type or global element) |
| globalObjectName | VARCHAR2 | IN | Name of the global object |
| localObject | VARCHAR2 | IN | Object descended from the global object |
| localObjectName | VARCHAR2 | IN | Name of the local object |
| sqlName | VARCHAR2 | IN | Name of the SQL attribute that corresponds to the element defined in the XML schema |
| overwrite | BOOLEAN | IN | Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVESQLNAME ( xmlschema IN OUT XMLType, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localObject IN VARCHAR2, localObjectName IN VARCHAR2, sqlName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-15 REMOVESQLNAME Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalObject Global object (global complex type or global element) globalObjectName Name of the global object localObject Object descended from the global object localObjectName Name of the local object sqlName Name of the SQL attribute that corresponds to the element defined in the XML schema overwrite Boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Example The shipTo element will have an annotation similar to xdb:SQLName="SHIPTO_SQLNAME" . DECLARE xml_schema XMLTYPE; BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.SETSQLNAME (xml_schema, 'element', 'purchaseOrder', 'element', 'shipTo', 'SHIPTO_SQLNAME'); UPDATE annotation_tab SET out = xml_schema; END; /