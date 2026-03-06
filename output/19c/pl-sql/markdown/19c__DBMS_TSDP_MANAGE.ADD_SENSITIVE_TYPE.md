---
id: 19c__DBMS_TSDP_MANAGE.ADD_SENSITIVE_TYPE
name: DBMS_TSDP_MANAGE.ADD_SENSITIVE_TYPE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.ADD_SENSITIVE_TYPE

This procedure creates and adds a sensitive column type to the list sensitive column types in the database.

## Syntax

```sql
DBMS_TSDP_MANAGE.ADD_SENSITIVE_TYPE (
   sensitive_type     IN  VARCHAR2,
   user_comment       IN  VARCAHR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sensitive_type | VARCHAR2 | IN | Name of the sensitive column type |
| user_comment | VARCAHR2 | IN | User comment regarding the sensitive column |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.ADD_SENSITIVE_TYPE ( sensitive_type IN VARCHAR2, user_comment IN VARCAHR2 DEFAULT NULL); Parameters Table 181-4 ADD_SENSITIVE_TYPE Procedure Parameters Parameter Description sensitive_type Name of the sensitive column type user_comment User comment regarding the sensitive column Examples Add a sensitive column type called SALARY_TYPE that is intended to be associated with columns containing salary data: DBMS_TSDP_MANAGE.ADD_SENSITIVE_TYPE ( sensitive_type => 'SALARY_TYPE', user_comment => 'Salary data');