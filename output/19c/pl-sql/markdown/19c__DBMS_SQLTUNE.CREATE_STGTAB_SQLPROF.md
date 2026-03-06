---
id: 19c__DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF
name: DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF

This procedure creates the staging table used for copying SQL profiles from one system to another.

## Syntax

```sql
DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF (
   table_name            IN VARCHAR2,
   schema_name           IN VARCHAR2 := NULL,
   tablespace_name       IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | The name of the table to create (case-insensitive unless double quoted). |
| schema_name | VARCHAR2 | IN | The schema to create the table in, or NULL for the current schema (case-insensitive unless double quoted). |
| tablespace_name | VARCHAR2 | IN | The tablespace to store the staging table within, or NULL for the default tablespace of the current user (case-insensitive unless double quoted). |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.CREATE_STGTAB_SQLPROF ( table_name IN VARCHAR2, schema_name IN VARCHAR2 := NULL, tablespace_name IN VARCHAR2 := NULL); Parameters Table 169-16 CREATE_STGTAB_SQLPROF Procedure Parameters Parameter Description table_name The name of the table to create (case-insensitive unless double quoted). schema_name The schema to create the table in, or NULL for the current schema (case-insensitive unless double quoted). tablespace_name The tablespace to store the staging table within, or NULL for the default tablespace of the current user (case-insensitive unless double quoted). Usage Notes Call this procedure once before issuing a call to the PACK_STGTAB_SQLPROF Procedure . To put different SQL profiles in different staging tables, you can call this procedure multiple times. This is a DDL operation, so it does not occur within a transaction.