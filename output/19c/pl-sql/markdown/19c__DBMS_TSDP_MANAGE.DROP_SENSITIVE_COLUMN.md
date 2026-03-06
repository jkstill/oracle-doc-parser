---
id: 19c__DBMS_TSDP_MANAGE.DROP_SENSITIVE_COLUMN
name: DBMS_TSDP_MANAGE.DROP_SENSITIVE_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_MANAGE
tags: [dbms_tsdp_manage]
source_file: DBMS_TSDP_MANAGE.html
---

# DBMS_TSDP_MANAGE.DROP_SENSITIVE_COLUMN

This procedure removes columns from the sensitive column list.

## Syntax

```sql
DBMS_TSDP_MANAGE.DROP_SENSITIVE_COLUMN (
   schema_name        IN VARCHAR2 DEFAULT '%',
   table_name         IN VARCAHR2 DEFAULT '%',
   column_name        IN VARCAHR2 DEFAULT '%');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Schema to which the column belongs |
| table_name | VARCAHR2 | IN | Table containing the column |
| column_name | VARCAHR2 | IN | Sensitive column name |

## Usage Notes

Syntax DBMS_TSDP_MANAGE.DROP_SENSITIVE_COLUMN ( schema_name IN VARCHAR2 DEFAULT '%', table_name IN VARCAHR2 DEFAULT '%', column_name IN VARCAHR2 DEFAULT '%'); Parameters Table 181-5 DROP_SENSITIVE_COLUMN Procedure Parameters Parameter Description schema_name Schema to which the column belongs table_name Table containing the column column_name Sensitive column name Examples Remove column SAL in SCOTT.EMP from the sensitive column list: DBMS_TSDP_MANAGE.DROP_SENSITIVE_COLUMN ( schema_name => 'SCOTT', table_name => 'EMP', column_name => 'SAL');