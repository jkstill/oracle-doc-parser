---
id: 19c__DBMS_SQLDIAG.CREATE_STGTAB_SQLPATCH
name: DBMS_SQLDIAG.CREATE_STGTAB_SQLPATCH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.CREATE_STGTAB_SQLPATCH

This procedure creates the staging table used for transporting SQL patches from one system to another.

## Syntax

```sql
DBMS_SQLDIAG.CREATE_STGTAB_SQLPATCH (
   table_name       IN  VARCHAR2,
   schema_name      IN  VARCHAR2 := NULL,
   tablespace_name  IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | (Mandatory) Name of the table to create (case-sensitive) |
| schema_name | VARCHAR2 | IN | Schema to create the table in, or NULL for current schema (case-sensitive) |
| tablespace_name | VARCHAR2 | IN | Tablespace to store the staging table within, or NULL for current user's default tablespace (case-sensitive) |

## Usage Notes

Syntax DBMS_SQLDIAG.CREATE_STGTAB_SQLPATCH ( table_name IN VARCHAR2, schema_name IN VARCHAR2 := NULL, tablespace_name IN VARCHAR2 := NULL); Parameters Table 165-15 CREATE_STGTAB_SQLPATCH Procedure Parameters Parameter Description table_name (Mandatory) Name of the table to create (case-sensitive) schema_name Schema to create the table in, or NULL for current schema (case-sensitive) tablespace_name Tablespace to store the staging table within, or NULL for current user's default tablespace (case-sensitive)