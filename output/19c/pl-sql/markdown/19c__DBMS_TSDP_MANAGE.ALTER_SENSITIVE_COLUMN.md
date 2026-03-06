---
id: 19c__DBMS_TSDP_MANAGE.ALTER_SENSITIVE_COLUMN
name: DBMS_TSDP_MANAGE.ALTER_SENSITIVE_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.ALTER_SENSITIVE_COLUMN

This procedure alters the Sensitive Type and/or the Comment of a Column in the sensitive column list.

## Syntax

```sql
DBMS_TSDP_MANAGE.ALTER_SENSITIVE_COLUMN (
   schema_name        IN VARCHAR2,
   table_name         IN VARCAHR2,
   column_name        IN VARCAHR2,
   sensitive_type     IN VARCAHR2,
   user_comment       IN VARCAHR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema to which the column belongs |
| table_name | VARCAHR2 | IN | Table containing the column |
| column_name | VARCAHR2 | IN | Sensitive column name |
| sensitive_type | VARCAHR2 | IN | Identifier of the sensitive column type |
| user_comment | VARCAHR2 | IN | User comment regarding the sensitive column |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.ALTER_SENSITIVE_COLUMN ( schema_name IN VARCHAR2, table_name IN VARCAHR2, column_name IN VARCAHR2, sensitive_type IN VARCAHR2, user_comment IN VARCAHR2 DEFAULT NULL); Parameters Table 181-3 ALTER_SENSITIVE_COLUMN Procedure Parameters Parameter Description schema_name Schema to which the column belongs table_name Table containing the column column_name Sensitive column name sensitive_type Identifier of the sensitive column type user_comment User comment regarding the sensitive column Examples Alter the column SAL in SCOTT.EMP that is listed in the sensitive column list: DBMS_TSDP_MANAGE.ALTER_SENSITIVE_COLUMN ( schema_name => 'SCOTT', table_name => 'EMP', column_name => 'SAL', sensitive_type => 'FINANCE_Type', user_comment => 'Finance Type. Earlier categorized as Salary Type');