---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.PRINTWARNINGS
name: DBMS_XMLSCHEMA_ANNOTATE.PRINTWARNINGS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.PRINTWARNINGS

This procedure lets a user raise or suppress a warning if an annotation maps to zero nodes in the XML schema.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.PRINTWARNINGS (
   value       IN   BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| val |  |  | For the NO MATCHING ELEMENTS FOUND error message to be raised val must be set to TRUE . In cases in which user wishes to suppress this warning, set to FALSE . |

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.PRINTWARNINGS ( value IN BOOLEAN DEFAULT TRUE); Parameters Table 211-9 PRINTWARNINGS Procedure Parameters Parameter Description val For the NO MATCHING ELEMENTS FOUND error message to be raised val must be set to TRUE . In cases in which user wishes to suppress this warning, set to FALSE . Usage Notes If an annotation maps to more than one node in the XML schema, this raise the error ANNOTATION MAPS TO MULTIPLE ELEMENTS . In this case no annotation is performed, and the user must correct the parameters to the procedure call to refer to a unique node in the XML schema.