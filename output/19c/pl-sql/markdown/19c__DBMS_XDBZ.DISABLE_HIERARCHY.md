---
id: 19c__DBMS_XDBZ.DISABLE_HIERARCHY
name: DBMS_XDBZ.DISABLE_HIERARCHY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBZ
tags: [dbms_xdbz]
source_file: DBMS_XDBZ.html
---

# DBMS_XDBZ.DISABLE_HIERARCHY

This procedure disables repository support for a particular XMLType table or view.

## Syntax

```sql
DBMS_XDBZ.DISABLE_HIERARCHY(
   object_schema IN VARCHAR2,
   object_name   IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| object_schema | VARCHAR2 | IN | Schema name of the XMLType table or view |
| object_name | VARCHAR2) | IN | Name of the XMLType table or view |

## Usage Notes

Syntax DBMS_XDBZ.DISABLE_HIERARCHY( object_schema IN VARCHAR2, object_name IN VARCHAR2); Parameters Table 202-5 DISABLE_HIERARCHY Procedure Parameters Parameter Description object_schema Schema name of the XMLType table or view object_name Name of the XMLType table or view