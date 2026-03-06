---
id: 19c__DBMS_XMLSCHEMA.COMPILESCHEMA
name: DBMS_XMLSCHEMA.COMPILESCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA.COMPILESCHEMA

This procedure can be used to re-compile an already registered XML schema. This is useful for bringing a schema in an invalid state to a valid state. Can result in a ORA-31001 exception: invalid resource handle or path name.

## Syntax

```sql
DBMS_XMLSCHEMA.COMPILESCHEMA(
   schemaurl IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaurl | VARCHAR2) | IN | URL identifying the schema |

## Usage Notes

Syntax DBMS_XMLSCHEMA.COMPILESCHEMA( schemaurl IN VARCHAR2); Parameters Table 210-6 COMPILESCHEMA Procedure Parameters Parameter Description schemaurl URL identifying the schema