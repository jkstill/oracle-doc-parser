---
id: 19c__DBMS_DDL.ALTER_TABLE_REFERENCEABLE
name: DBMS_DDL.ALTER_TABLE_REFERENCEABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DDL
tags: [dbms_ddl]
source_file: DBMS_DDL.html
---

# DBMS_DDL.ALTER_TABLE_REFERENCEABLE

This procedure alters the given object table table_schema.table_name so it becomes the referenceable table for the given schema affected_schema .

## Syntax

```sql
ALTER TABLE [<table_schema>.]<table_name>  REFERENCEABLE FOR <affected_schema>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name |  |  | Name of the table to be altered. Cannot be a synonym. Must not be NULL . Case sensitive. |
| table_schema |  |  | Name of the schema owning the table to be altered. If NULL then the current schema is used. Case sensitive. |
| affected_schema |  |  | Name of the schema affected by this alteration. If NULL then the current schema is used. Case sensitive. |

## Usage Notes

This is equivalent to SQL: ALTER TABLE [<table_schema>.]<table_name> REFERENCEABLE FOR <affected_schema> which is currently not supported or available as a DDL statement. Syntax DBMS_DDL.ALTER_TABLE_REFERENCEABLE table_name IN VARCHAR2, table_schema IN DEFAULT NULL, affected_schema IN DEFAULT NULL); Parameters Table 56-5 ALTER_TABLE_REFERENCEABLE Procedure Parameters Parameter Description table_name Name of the table to be altered. Cannot be a synonym. Must not be NULL . Case sensitive. table_schema Name of the schema owning the table to be altered. If NULL then the current schema is used. Case sensitive. affected_schema Name of the schema affected by this alteration. If NULL then the current schema is used. Case sensitive. Usage Notes When you create an object table, it automatically becomes referenceable, unless you use the OID AS clause when creating the table. The OID AS clause makes it possible for you to create an object table and to assign to the new table the same EOID as another object table of the same type. After you create a new table using the OID AS clause, you end up with two object table with the same EOID ; the new table is not referenceable, the original one is. All references that used to point to the objects in the original table still reference the same objects in the same original table. If you execute this procedure on the new table, it makes the new table the referenceable table replacing the original one; thus, those references now point to the objects in the new table instead of the original table.