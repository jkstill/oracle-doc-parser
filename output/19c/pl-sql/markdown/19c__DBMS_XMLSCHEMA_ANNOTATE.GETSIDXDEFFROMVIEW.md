---
id: 19c__DBMS_XMLSCHEMA_ANNOTATE.GETSIDXDEFFROMVIEW
name: DBMS_XMLSCHEMA_ANNOTATE.GETSIDXDEFFROMVIEW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA_ANNOTATE
tags: [dbms_xmlschema_annotate]
source_file: DBMS_XMLSCHEMA_ANNOTATE.html
---

# DBMS_XMLSCHEMA_ANNOTATE.GETSIDXDEFFROMVIEW

This function takes a XMLTABLE view definition on a xmltype column or table and it returns a CLOB which can be used as parameter to create a structured xmlindex that backs up the XMLTABLE view as relational table.

## Syntax

```sql
DBMS_XMLSCHEMA_ANNOTATE.GETSIDXDEFFROMVIEW (
   viewName   IN xmlType) 
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| viewName | xmlType) | IN | The original XML schema |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_XMLSCHEMA_ANNOTATE.GETSIDXDEFFROMVIEW ( viewName IN xmlType) RETURN CLOB; Parameters Table 211-8 GETSIDXDEFFROMVIEW Function Parameters Parameter Description viewName The original XML schema Return Values This function returns a CLOB which can be used as parameter to create a structured xmlindex that backs up the XMLTABLE view as relational table.