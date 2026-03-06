---
id: 19c__DBMS_XDBZ.ENABLE_HIERARCHY
name: DBMS_XDBZ.ENABLE_HIERARCHY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBZ
tags: [dbms_xdbz]
source_file: DBMS_XDBZ.html
---

# DBMS_XDBZ.ENABLE_HIERARCHY

This procedure enables repository support for a particular XMLType table or view. This allows the use of a uniform ACL-based security model across all documents in the repository.

## Syntax

```sql
DBMS_XDBZ.ENABLE_HIERARCHY(
   object_schema   IN   VARCHAR2,
   object_name     IN   VARCHAR2,
   hierarchy_type  IN   PLS_INTEGER := DBMS_XDBZ.ENABLE_CONTENTS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema name of the XMLType table or view |
| object_name | VARCHAR2 | IN | Name of the XMLType table or view |
| hierarchy_type | PLS_INTEGER | IN | How to enable the hierarchy. ENABLE_CONTENTS - enable hierarchy for contents, that is, this table will store contents of resources in the repository ENABLE_RESMETADATA - enable hierarchy for resource metadata, that is, this table will store schema based custom metadata for resources If this subprogram is called on a table, another call will have no effect. Note that you cannot enable hierarchy for both contents and resource metadata. |

## Usage Notes

See Also: Oracle XML DB Developer's Guide for more information about See Also: Oracle XML DB Developer's Guide for more information about Syntax DBMS_XDBZ.ENABLE_HIERARCHY( object_schema IN VARCHAR2, object_name IN VARCHAR2, hierarchy_type IN PLS_INTEGER := DBMS_XDBZ.ENABLE_CONTENTS); Parameters Table 202-6 ENABLE_HIERARCHY Procedure Parameters Parameter Description object_schema Schema name of the XMLType table or view object_name Name of the XMLType table or view hierarchy_type How to enable the hierarchy. ENABLE_CONTENTS - enable hierarchy for contents, that is, this table will store contents of resources in the repository ENABLE_RESMETADATA - enable hierarchy for resource metadata, that is, this table will store schema based custom metadata for resources If this subprogram is called on a table, another call will have no effect. Note that you cannot enable hierarchy for both contents and resource metadata.