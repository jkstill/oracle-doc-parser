---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.REMOVEDEFAULTTABLE
name: DBMS_XMLSCHEMA_ANNOTATE.REMOVEDEFAULTTABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.REMOVEDEFAULTTABLE

This procedure removes any default table attribute given for the element.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.REMOVEDEFAULTTABLE (
   xmlschema          IN OUT XMLTYPE, 
   globalElementName  IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | XMLTYPE | IN OUT | XML schema to be annotated |
| globalElementName | VARCHAR2) | IN | Name of the global element in the schema |

## Usage Notes

After calling this procedure, the system generates table names. This procedure always overwrites. Syntax DBMS_XMLSCHEMA_ANNOTATE.REMOVEDEFAULTTABLE ( xmlschema IN OUT XMLTYPE, globalElementName IN VARCHAR2); Parameters Table 211-11 REMOVEDEFAULTTABLE Procedure Parameters Parameter Description xmlschema XML schema to be annotated globalElementName Name of the global element in the schema Example Annotations can be verified anytime using "select out from annotation_tab" . --The purchaseOrder element will have no annotation for defaultTable. DECLARE xml_schema XMLTYPE; BEGIN SELECT out INTO xml_schema FROM annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.REMOVEDEFAULTTABLE(xml_schema, 'purchaseOrder'); UPDATE annotation_tab SET out = xml_schema; END; /