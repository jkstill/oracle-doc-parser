---
id: 19c__DBMS_XDBZ.IS_HIERARCHY_ENABLED
name: DBMS_XDBZ.IS_HIERARCHY_ENABLED
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBZ
tags: [dbms_xdbz]
source_file: DBMS_XDBZ.html
---

# DBMS_XDBZ.IS_HIERARCHY_ENABLED

This function determines if repository support for the specified XMLType table or view is enabled.

## Syntax

```sql
DBMS_XDBZ.IS_HIERARCHY_ENABLED(
   object_schema   IN  VARCHAR2,
   object_name     IN  VARCHAR2,
   hierarchy_type  IN  PLS_INTEGER := IS_ENABLED_CONTENTS)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema name of the XMLType table or view |
| object_name | VARCHAR2 | IN | Name of the XMLType table or view |
| hierarchy_type | PLS_INTEGER | IN | Type of hierarchy to check for: IS_ENABLED_CONTENTS - if hierarchy was enabled for contents, that is, the ENABLE_HIERARCHY Procedure was called with hierarchy_type as ENABLE_CONTENTS IS_ENABLED_RESMETADATA - if hierarchy was enabled for resource metadata, that is, the ENABLE_HIERARCHY Procedure was called with hierarchy_type as ENABLE_RESMETADATA |

**Returns:** `BOOLEAN`

## Usage Notes

Syntax DBMS_XDBZ.IS_HIERARCHY_ENABLED( object_schema IN VARCHAR2, object_name IN VARCHAR2, hierarchy_type IN PLS_INTEGER := IS_ENABLED_CONTENTS) RETURN BOOLEAN; Parameters Table 202-9 IS_HIERARCHY_ENABLED Function Parameters Parameter Description object_schema Schema name of the XMLType table or view object_name Name of the XMLType table or view hierarchy_type Type of hierarchy to check for: IS_ENABLED_CONTENTS - if hierarchy was enabled for contents, that is, the ENABLE_HIERARCHY Procedure was called with hierarchy_type as ENABLE_CONTENTS IS_ENABLED_RESMETADATA - if hierarchy was enabled for resource metadata, that is, the ENABLE_HIERARCHY Procedure was called with hierarchy_type as ENABLE_RESMETADATA Return Values Returns TRUE if the given XMLTYPE table or view has the XDB Hierarchy enabled with the specified type.