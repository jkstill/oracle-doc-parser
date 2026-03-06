---
id: 19c__DBMS_TSDP_PROTECT.DISABLE_PROTECTION_COLUMN
name: DBMS_TSDP_PROTECT.DISABLE_PROTECTION_COLUMN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.DISABLE_PROTECTION_COLUMN

This procedure disables protection for columns.

## Syntax

```sql
DBMS_TSDP_PROTECT.DISABLE_PROTECTION_COLUMN (
   schema_name        IN  VARCHAR2 DEFAULT '%',
   table_name         IN  VARCHAR2 DEFAULT '%',
   column_name        IN  VARCHAR2 DEFAULT '%',
   policy_name        IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schema_name | VARCHAR2 | IN | Name of the schema containing the column |
| table_name | VARCHAR2 | IN | Table containing the column |
| column_name | VARCHAR2 | IN | Column name |
| policy_name | VARCHAR2 | IN | Optional policy name. If given, only this policy is disabled. |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.DISABLE_PROTECTION_COLUMN ( schema_name IN VARCHAR2 DEFAULT '%', table_name IN VARCHAR2 DEFAULT '%', column_name IN VARCHAR2 DEFAULT '%', policy_name IN VARCHAR2 DEFAULT NULL); Parameters Table 182-6 DISABLE_PROTECTION_COLUMN Procedure Parameters Parameter Description schema_name Name of the schema containing the column table_name Table containing the column column_name Column name policy_name Optional policy name. If given, only this policy is disabled. Examples Disable TSDP policies associated with the corresponding sensitive column types for columns that reside in schema with name like %PAYROLL% , table name like EMP% , and column name like SAL% : EXEC DBMS_TSDP_PROTECT.DISABLE_PROTECTION_COLUMN ('%PAYROLL%', 'EMP%', 'SAL%');