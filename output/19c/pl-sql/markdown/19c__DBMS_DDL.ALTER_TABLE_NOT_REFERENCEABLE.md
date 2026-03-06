---
id: 19c__DBMS_DDL.ALTER_TABLE_NOT_REFERENCEABLE
name: DBMS_DDL.ALTER_TABLE_NOT_REFERENCEABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.ALTER_TABLE_NOT_REFERENCEABLE

This procedure alters the given object table table_schema.table_name so it becomes not the default referenceable table for the schema affected_schema .

## Syntax

```sql
ALTER TABLE [<table_schema>.]<table_name> NOT REFERENCEABLE FOR <affected_schema>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name |  |  | Name of the table to be altered. Cannot be a synonym. Must not be NULL . Case sensitive. |
| table_schema |  |  | Name of the schema owning the table to be altered. If NULL then the current schema is used. Case sensitive. |
| affected_schema |  |  | Name of the schema affected by this alteration. If NULL then the current schema is used. Case sensitive. |

## Usage Notes

This is equivalent to SQL: ALTER TABLE [<table_schema>.]<table_name> NOT REFERENCEABLE FOR <affected_schema> which is currently not supported or available as a DDL statement. Syntax DBMS_DDL.ALTER_TABLE_NOT_REFERENCEABLE ( table_name IN VARCHAR2, table_schema IN DEFAULT NULL, affected_schema IN DEFAULT NULL); Parameters Table 56-4 ALTER_TABLE_NOT_REFERENCEABLE Procedure Parameters Parameter Description table_name Name of the table to be altered. Cannot be a synonym. Must not be NULL . Case sensitive. table_schema Name of the schema owning the table to be altered. If NULL then the current schema is used. Case sensitive. affected_schema Name of the schema affected by this alteration. If NULL then the current schema is used. Case sensitive. Usage Notes This procedure simply reverts for the affected schema to the default table referenceable for PUBLIC ; that is., it simply undoes the previous ALTER_TABLE_REFERENCEABLE call for this specific schema. The affected schema must a particular schema (cannot be PUBLIC ). The user that executes this procedure must own the table (that is, the schema is the same as the user), and the affected schema must be the same as the user. If the user executing this procedure has ALTER ANY TABLE and SELECT ANY TABLE and DROP ANY TABLE privileges, the user doesn't have to own the table and the affected schema can be any valid schema.