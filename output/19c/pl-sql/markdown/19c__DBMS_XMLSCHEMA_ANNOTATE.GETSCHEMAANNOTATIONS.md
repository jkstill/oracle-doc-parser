---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS
name: DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS

This function creates a document containing the differences between the annotated XML schema and the original XML schema.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS (
   xmlschema IN xmlType) 
  RETURN XMLType;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| xmlschema | xmlType) | IN | The original XML schema |

**Returns:** `XMLType`

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS ( xmlschema IN xmlType) RETURN XMLType; Parameters Table 211-7 GETSCHEMAANNOTATIONS Function Parameters Parameter Description xmlschema The original XML schema Return Values This function returns the document annotations.xml as an XMLType . Usage Notes This function saves all annotations in one document, named annotations , and returns it. With this document, you can apply all annotations to a non-annotated schema, using DBMS_XMLSCHEMA_ANNOTATE. GETSCHEMAANNOTATIONS . DBMS_XMLSCHEMA_ANNOTATE.GETSCHEMAANNOTATIONS is not available on Oracle Database release 10.2 (only Oracle Database release 11. x ). See Also: SETSCHEMAANNOTATATIONS Procedure See Also: SETSCHEMAANNOTATATIONS Procedure