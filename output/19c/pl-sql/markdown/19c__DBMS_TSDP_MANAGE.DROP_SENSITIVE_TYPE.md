---
id: 19c__DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE
name: DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE

This procedure drops a sensitive column type from the list sensitive column types in the database.

## Syntax

```sql
DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE (
   sensitive_type     IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sensitive_type | VARCHAR2) | IN | Name of the sensitive column type to be dropped |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE ( sensitive_type IN VARCHAR2); Parameters Table 181-6 DROP_SENSITIVE_TYPE Procedure Parameters Parameter Description sensitive_type Name of the sensitive column type to be dropped Examples To drop SALARY_TYPE : DBMS_TSDP_MANAGE.DROP_SENSITIVE_TYPE ( sensitive_type => 'SALARY_TYPE');