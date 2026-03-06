---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION
name: DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION

This procedure prevents the creation of a table for the top-level element by adding a default table attribute with an empty value to the element. The first overload applies to a specified top-level element and the second applies to all top-level elements. The procedure always overwrites. This is equivalent to using the schema annotation xdb:defaultTable="" for the top-level element or elements.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION (
   xmlschema         IN OUT XMLType,  
   globalElementName IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | XML schema to be annotated |
| globalElementName | VARCHAR2) | IN | Name of the global element in the schema |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION ( xmlschema IN OUT XMLType, globalElementName IN VARCHAR2); DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION ( xmlschema IN OUT XMLType); Parameters Table 211-3 DISABLEDEFAULTTABLECREATION Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalElementName Name of the global element in the schema Example The purchaseOrder element will have an annotation similar to xdb:defaultTable="" . DECLARE xml_schema XMLTYPE; BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.DISABLEDEFAULTTABLECREATION(xml_schema, 'purchaseOrder'); UPDATE annotation_tab SET out = xml_schema; END; /