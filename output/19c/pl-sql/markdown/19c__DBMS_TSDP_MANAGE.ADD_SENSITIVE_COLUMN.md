---
id: 19c__DBMS_TSDP_MANAGE.ADD_SENSITIVE_COLUMN
name: DBMS_TSDP_MANAGE.ADD_SENSITIVE_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.ADD_SENSITIVE_COLUMN

This procedure adds a column to the sensitive column list.

## Syntax

```sql
DBMS_TSDP_MANAGE.ADD_SENSITIVE_COLUMN (
   schema_name        IN VARCHAR2,
   table_name         IN VARCHAR2,
   column_name        IN VARCHAR2,
   sensitive_type     IN VARCHAR2,
   user_comment       IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema to which the column belongs |
| table_name | VARCHAR2 | IN | Table containing the column |
| column_name | VARCHAR2 | IN | Sensitive column name |
| sensitive_type | VARCHAR2 | IN | Identifier of the sensitive column type |
| user_comment | VARCHAR2 | IN | User comment regarding the sensitive column |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.ADD_SENSITIVE_COLUMN ( schema_name IN VARCHAR2, table_name IN VARCHAR2, column_name IN VARCHAR2, sensitive_type IN VARCHAR2, user_comment IN VARCHAR2 DEFAULT NULL); Parameters Table 181-2 ADD_SENSITIVE_COLUMN Procedure Parameters Parameter Description schema_name Schema to which the column belongs table_name Table containing the column column_name Sensitive column name sensitive_type Identifier of the sensitive column type user_comment User comment regarding the sensitive column Examples Add a column SAL in SCOTT.EMP : DBMS_TSDP_MANAGE.ADD_SENSITIVE_COLUMN ( schema_name => 'SCOTT', table_name => 'EMP', column_name => 'SAL', sensitive_type => 'SALARY_TYPE', user_comment => 'Salary column');