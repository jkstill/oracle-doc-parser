---
id: 19c__DBMS_SQLTUNE.CREATE_STGTAB_SQLSET
name: DBMS_SQLTUNE.CREATE_STGTAB_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.CREATE_STGTAB_SQLSET

This procedure creates a staging table through which SQL tuning sets are imported and exported.

## Syntax

```sql
DBMS_SQLTUNE.CREATE_STGTAB_SQLSET (
   table_name           IN VARCHAR2,
   schema_name          IN VARCHAR2 := NULL,
   tablespace_name      IN VARCHAR2 := NULL,
   db_version           IN NUMBER   := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| table_name | VARCHAR2 | IN | Specifies the of the table to create. The name is case sensitive. |
| schema_name | VARCHAR2 | IN | Defines the schema in which to create the table, or NULL for the current schema. The name is case sensitive. |
| tablespace_name | VARCHAR2 | IN | Specifies the tablespace in which to store the staging table, or NULL for the default tablespace of the current user. The name is case sensitive. |
| db_version | NUMBER | IN | Specifies the database version that determines the format of the staging table. You can also create an older database version staging table to export an STS to an older database version. Use one of the following values: NULL (default) — Specifies the current database version. STS_STGTAB_10_2_VERSION — Specifies the 10.2 database version. STS_STGTAB_11_1_VERSION — Specifies the 11.1 database version. STS_STGTAB_11_2_VERSION — Specifies the 11.2 database version. STS_STGTAB_12_1_VERSION — Specifies the 12.1 database version. STS_STGTAB_12_2_VERSION — Specifies the 12.2 database version. |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.CREATE_STGTAB_SQLSET ( table_name IN VARCHAR2, schema_name IN VARCHAR2 := NULL, tablespace_name IN VARCHAR2 := NULL, db_version IN NUMBER := NULL); Parameters Table 169-17 CREATE_STGTAB_SQLSET and CREATE_STGTAB Procedure Parameters Parameter Description table_name Specifies the of the table to create. The name is case sensitive. schema_name Defines the schema in which to create the table, or NULL for the current schema. The name is case sensitive. tablespace_name Specifies the tablespace in which to store the staging table, or NULL for the default tablespace of the current user. The name is case sensitive. db_version Specifies the database version that determines the format of the staging table. You can also create an older database version staging table to export an STS to an older database version. Use one of the following values: NULL (default) — Specifies the current database version. STS_STGTAB_10_2_VERSION — Specifies the 10.2 database version. STS_STGTAB_11_1_VERSION — Specifies the 11.1 database version. STS_STGTAB_11_2_VERSION — Specifies the 11.2 database version. STS_STGTAB_12_1_VERSION — Specifies the 12.1 database version. STS_STGTAB_12_2_VERSION — Specifies the 12.2 database version. Security Model You must have CREATE TABLE permissions in the specified schema and tablespace.