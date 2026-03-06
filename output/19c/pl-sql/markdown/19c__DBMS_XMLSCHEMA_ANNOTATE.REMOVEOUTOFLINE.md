---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE

This procedure removes any existing SQLInline attributes to prevent out-of-line storage.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE (
   xmlschema           IN OUT  XMLType, 
   elementName         IN      VARCHAR2, 
   elementType         IN      VARCHAR2, 
   overwrite           IN      BOOLEAN default TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | The XML schema to be annotated |
| elementName | VARCHAR2 | IN | The element name |
| elementType | VARCHAR2 | IN | The element type |
| globalObject |  |  | The global object (global complex type or global element) |
| globalObjectName |  |  | The name of the global object |
| localElementName |  |  | The name of a local element that descends from the global element |
| reference |  |  | A reference to a global element |
| overwrite | BOOLEAN | IN | A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

There are three overloads. Syntax Removes the SQLInline attribute for the named element. DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE ( xmlschema IN OUT XMLType, elementName IN VARCHAR2, elementType IN VARCHAR2, overwrite IN BOOLEAN default TRUE); Removes the SQLInline attribute for the object specified by its global object and local element names. DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE ( xmlschema IN OUT XMLType, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localElementName IN VARCHAR2); Removes the SQLInline attribute for the referenced global element. DBMS_XMLSCHEMA_ANNOTATE.REMOVEOUTOFLINE ( xmlschema IN OUT XMLType, reference IN VARCHAR2); Parameters Table 211-13 REMOVEOUTOFLINE Procedure Parameters Parameter Description xmlschema The XML schema to be annotated elementName The element name elementType The element type globalObject The global object (global complex type or global element) globalObjectName The name of the global object localElementName The name of a local element that descends from the global element reference A reference to a global element overwrite A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Usage Notes This procedure reverses SETOUTOFLINE Procedure .