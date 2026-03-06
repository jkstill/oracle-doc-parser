---
id: 19c__DBMS_SPD.CREATE_STGTAB_DIRECTIVE
name: DBMS_SPD.CREATE_STGTAB_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPD
tags: [dbms_spd]
source_file: DBMS_SPD.html
---

# DBMS_SPD.CREATE_STGTAB_DIRECTIVE

This procedure creates a staging table into which to pack (export) SQL plan directives.

## Syntax

```sql
DBMS_SPD.CREATE_STGTAB_DIRECTIVE (
   table_name         IN VARCHAR2,
   table_owner        IN VARCHAR2  := USER,
   tablespace_name    IN VARCHAR2  := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Name of staging table |
| table_owner | VARCHAR2 | IN | Name of schema owner of staging table. Default is current schema. |
| tablespace_name | VARCHAR2 | IN | Name of tablespace. Default NULL means create staging table in the default tablespace: |

## Usage Notes

Syntax DBMS_SPD.CREATE_STGTAB_DIRECTIVE ( table_name IN VARCHAR2, table_owner IN VARCHAR2 := USER, tablespace_name IN VARCHAR2 := NULL); Parameters Table 160-3 CREATE_STGTAB_DIRECTIVE Procedure Parameters Parameter Description table_name Name of staging table table_owner Name of schema owner of staging table. Default is current schema. tablespace_name Name of tablespace. Default NULL means create staging table in the default tablespace: Exceptions ORA-38171 INSUFFICIENT_PRIVILEGE : The user does not have proper privilege to perform the operation. ORA-28104 INVALID_INPUT : The input value is not valid. ORA-44001 INVALID_SCHEMA : The input schema does not exist. ORA-13159 TABLE_ALREADY_EXISTS : The specified table already exists. ORA-29304 TABLESPACE_MISSING : The specified tablespace does not exist. Usage Notes The ADMINISTER SQL MANAGEMENT OBJECT privilege is required to execute this procedure.