---
id: 19c__DBMS_SQLDIAG.DROP_SQL_PATCH
name: DBMS_SQLDIAG.DROP_SQL_PATCH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.DROP_SQL_PATCH

This procedure drops the named SQL patch from the database.

## Syntax

```sql
DBMS_SQLDIAG.DROP_SQL_PATCH (
   name     IN  VARCHAR2,   ignore   IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of patch to be dropped. The name is case sensitive. |
| ignore | BOOLEAN | IN | Ignore errors due to object not existing. |

## Usage Notes

Syntax DBMS_SQLDIAG.DROP_SQL_PATCH ( name IN VARCHAR2, ignore IN BOOLEAN := FALSE); Parameters Table 165-17 DROP_SQL_PATCH Function & Procedure Parameters Parameter Description name Name of patch to be dropped. The name is case sensitive. ignore Ignore errors due to object not existing. Usage Notes Requires DROP ANY SQL PATCH privilege