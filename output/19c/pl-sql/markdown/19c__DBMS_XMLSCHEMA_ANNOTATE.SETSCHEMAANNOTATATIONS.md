---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATATIONS
name: DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATATIONS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATATIONS

This procedure takes the annotated differences resulting from a call to DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS and patches them into the provided XML schema.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATIONS (
   xmlschema     IN OUT xmlType,
   annotations   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | xmlType | IN OUT | An XML schema to be patched. |
| annotations | VARCHAR2) | IN | The differences document produced by calling DBMS_XMLSCHEMA_ANNOTATE. GETSCHEMAANNOTATIONS on the original XML schema and an annotated XML schema. |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATIONS ( xmlschema IN OUT xmlType, annotations IN VARCHAR2); Parameters Table 211-23 SETSCHEMAANNOTATIONS Procedure Parameters Parameter Description xmlschema An XML schema to be patched. annotations The differences document produced by calling DBMS_XMLSCHEMA_ANNOTATE. GETSCHEMAANNOTATIONS on the original XML schema and an annotated XML schema. Usage Notes DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATATIONS is not available on Oracle Database release 10.2 (only Oracle Database release 11. x ). See Also: GETSCHEMAANNOTATIONS Function See Also: GETSCHEMAANNOTATIONS Function Example The following example illustrates DBMS_XMLSCHEMA_ANNOTATE.SETSCHEMAANNOTATIONS shown here and GETSCHEMAANNOTATIONS Function . -- test getannotations and apply them declare xml_schema xmltype; xml_schema2 xmltype; annotations xmltype; begin select out into xml_schema from annotation_tab; -- get the annotations from the schema annotations := DBMS_XMLSCHEMA_ANNOTATE.getSchemaAnnotations (xml_schema); -- apply the annotations to the schema select inp into xml_schema2 from annotation_tab; DBMS_XMLSCHEMA_ANNOTATE.setSchemaAnnotations(xml_schema2, annotations); update annotation_tab t set t.out = xml_schema2; end; /