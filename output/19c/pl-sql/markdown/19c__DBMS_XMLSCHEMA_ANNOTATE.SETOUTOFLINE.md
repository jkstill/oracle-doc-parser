---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE
name: DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE

This procedure sets the SQLInline attribute to FALSE , that is, it sets xdb:SQLInLine=FALSE .

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE (
   xmlschema          IN OUT  XMLType,  
   elementName        IN      VARCHAR2, 
   elementType        IN      VARCHAR2, 
   defaultTableName   IN      VARCHAR2, 
   overwrite          IN      BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLType | IN OUT | The XML schema to be annotated. |
| elementName | VARCHAR2 | IN | The element name |
| elementType | VARCHAR2 | IN | The element type |
| defaultTable Name |  |  | The name of the default table. |
| globalObject |  |  | The global object (global complex type or global element) |
| globalObjectName |  |  | The name of the global object |
| localElementName |  |  | The name of a local element that descends from the global element. |
| reference |  |  | A reference to a global element |
| overwrite | BOOLEAN | IN | A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . |

## Usage Notes

This forces XDB to store the corresponding elements in the XML document out-of-line as rows in a separate XMLType table. XDB stores references to each row of the XMLType table in a link table that is maintained by the main table This procedure can improve performance in some situations if the out-of-line table acts as the driver for the query. Storing elements in an out-of-line table also reduces the numbers of columns in the base table, thus avoiding '1000 column limit' errors during XML schema registration, when some elements have complex types with many elements. Also See: Oracle XML DB Developer's Guide There are three overloads. Also See: Oracle XML DB Developer's Guide Syntax Sets the SQLInline attribute to FALSE , forcing out-of-line storage for the named element. DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE ( xmlschema IN OUT XMLType, elementName IN VARCHAR2, elementType IN VARCHAR2, defaultTableName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Sets the SQLInline attribute to FALSE , forcing out-of-line storage for the element specified by its local and global name. DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE ( xmlschema IN OUT XMLType, globalObject IN VARCHAR2, globalObjectName IN VARCHAR2, localElementName IN VARCHAR2, defaultTableName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Sets the SQLInline attribute to FALSE to force out-of-line storage and sets the default table name for all references to a particular global element. DBMS_XMLSCHEMA_ANNOTATE.SETOUTOFLINE ( xmlschema IN OUT XMLType, reference IN VARCHAR2, defaultTableName IN VARCHAR2, overwrite IN BOOLEAN DEFAULT TRUE); Parameters Table 211-22 SETOUTOFLINE Procedure Parameters Parameter Description xmlschema The XML schema to be annotated. elementName The element name elementType The element type defaultTable Name The name of the default table. globalObject The global object (global complex type or global element) globalObjectName The name of the global object localElementName The name of a local element that descends from the global element. reference A reference to a global element overwrite A boolean that indicates whether or not the procedure overwrites element attributes. The default is TRUE . Usage Notes After XML schema registration and before loading XML instance data, use DBMS_XMLSTORAGE_MANAGE.SCOPEXMLREFERENCES() to make these references scope to the out-of-line table only. This ensures better query performance later on.