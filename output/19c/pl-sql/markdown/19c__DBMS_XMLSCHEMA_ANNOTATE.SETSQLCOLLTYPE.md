---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETSQLCOLLTYPE
name: DBMS_XMLSCHEMA_ANNOTATE.SETSQLCOLLTYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETSQLCOLLTYPE

This procedure assigns a SQL type name for a collection. A collection is a global or local element with maxOccurs>1 .

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETSQLCOLLTYPE (
   xmlschema          IN OUT   XMLTYPE, 
   elementName        IN       VARCHAR2, 
   sqlCollType        IN       VARCHAR2, 
   overwrite          IN       BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN OUT | The XML schema to be annotated |
| elementName | VARCHAR2 | IN | The element name |
| sqlCollType | VARCHAR2 | IN | The SQL collection type |
| globalObject |  |  | The global object (global complex type or global element) |
| globalObjectName |  |  | The name of the global object |
| localElementName |  |  | The name of a local element that descends from the global element |
| overwrite | BOOLEAN | IN | A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

Using this procedure, XDB creates SQLType s with the user-defined names provided. There are two overloads. The first sets the name of the SQL collection type corresponding to an XML element and the second to an XML element inside the specified complex type. Syntax DBMS_XMLSCHEMA_ANNOTATE.SETSQLCOLLTYPE ( xmlschema IN OUT XMLTYPE, elementName IN VARCHAR2, sqlCollType IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); DBMS_XMLSCHEMA_ANNOTATE.SETSQLCOLLTYPE ( xmlschema IN OUT XMLType, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localElementName IN VARCHAR2, sqlCollType IN VARCHAR2, overwrite IN BOOLEAN default TRUE ); Parameters Table 211-24 SETSQLCOLLTYPE Procedure Parameters Parameter Description xmlschema The XML schema to be annotated elementName The element name sqlCollType The SQL collection type globalObject The global object (global complex type or global element) globalObjectName The name of the global object localElementName The name of a local element that descends from the global element overwrite A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Example The item element will have an annotation similar to xdb:SQLCollType="ITEM_SQL_COL_TYPE" . declare xml_schema xmltype; begin SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.setSQLCollType (xml_schema, 'item', 'ITEM_SQL_COL_TYPE',TRUE); UPDATE annotation_tab SET out = xml_schema; end;