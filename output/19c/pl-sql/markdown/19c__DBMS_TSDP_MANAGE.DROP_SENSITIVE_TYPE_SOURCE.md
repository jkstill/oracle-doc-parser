---
id: 19c__DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE_SOURCE
name: DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE_SOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE_SOURCE

This procedure drops sensitive column types corresponding to a source from the list sensitive column types in the database.

## Syntax

```sql
DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE_SOURCE (
   source      IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| source | VARCHAR2) | IN | Name of the source |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE_SOURCE ( source IN VARCHAR2); Parameters Table 181-7 DROP_SENSITIVE_TYPE_SOURCE Procedure Parameters Parameter Description source Name of the source Examples To drop all sensitive column types corresponding to an Application Data Model (ADM) from an Oracle Enterprise Manager Cloud Control instance, ADM_DEMO : DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE_SOURCE ( source => 'ADM_DEMO');