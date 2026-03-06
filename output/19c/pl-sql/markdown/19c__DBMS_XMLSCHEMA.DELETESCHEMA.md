---
id: 19c__DBMS_XMLSCHEMA.DELETESCHEMA
name: DBMS_XMLSCHEMA.DELETESCHEMA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XMLSCHEMA
tags: [dbms_xmlschema]
source_file: DBMS_XMLSCHEMA.html
---

# DBMS_XMLSCHEMA.DELETESCHEMA

This procedure deletes the XML Schema specified by the URL.

## Syntax

```sql
DBMS_XMLSCHEMA.DELETESCHEMA(
   schemaurl      IN  VARCHAR2,
   delete_option  IN  PLS_INTEGER := DELETE_RESTRICT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schemaurl | VARCHAR2 | IN | URL identifying the schema to be deleted |
| delete_option | PLS_INTEGER | IN | Delete options: DELETE_RESTRICT - Schema deletion fails if there are any tables or schemas that depend on this schema DELETE_INVALIDATE - Schema deletion does not fail if there are any dependencies. Instead, it simply invalidates all dependent objects. DELETE_CASCADE - Schema deletion will also drop all default SQL types and default tables. However the deletion fails if there are any stored instances conforming to this schema. DELETE_CASCADE_FORCE - Similar to DELETE_CASCADE except that it does not check for any stored instances conforming to this schema. Also, it ignores any errors. |

## Usage Notes

Syntax DBMS_XMLSCHEMA.DELETESCHEMA( schemaurl IN VARCHAR2, delete_option IN PLS_INTEGER := DELETE_RESTRICT); See Also: "XMLSCHEMA Storage and Query: Basic" chapter of the Oracle XML DB Developer's Guide See Also: "XMLSCHEMA Storage and Query: Basic" chapter of the Oracle XML DB Developer's Guide Parameters Table 210-8 DELETESCHEMA Procedure Parameters Parameter Description schemaurl URL identifying the schema to be deleted delete_option Delete options: DELETE_RESTRICT - Schema deletion fails if there are any tables or schemas that depend on this schema DELETE_INVALIDATE - Schema deletion does not fail if there are any dependencies. Instead, it simply invalidates all dependent objects. DELETE_CASCADE - Schema deletion will also drop all default SQL types and default tables. However the deletion fails if there are any stored instances conforming to this schema. DELETE_CASCADE_FORCE - Similar to DELETE_CASCADE except that it does not check for any stored instances conforming to this schema. Also, it ignores any errors. Exceptions Table 210-9 DELETESCHEMA Procedure Exceptions Exception Description ORA-31001 Invalid resource handle or path name