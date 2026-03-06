---
id: 19c__DBMS_SQLTUNE.PACK_STGTAB_SQLSET
name: DBMS_SQLTUNE.PACK_STGTAB_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.PACK_STGTAB_SQLSET

This procedure copies one or more SQL tuning sets from their location in the SYS schema to a staging table created by the CREATE_STGTAB_SQLSET procedure.

## Syntax

```sql
DBMS_SQLTUNE.PACK_STGTAB_SQLSET (
   sqlset_name          IN VARCHAR2,
   sqlset_owner         IN VARCHAR2 := NULL,
   staging_table_name   IN VARCHAR2,
   staging_schema_owner IN VARCHAR2 := NULL,
   db_version           IN NUMBER   := NULL);
```

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.PACK_STGTAB_SQLSET ( sqlset_name IN VARCHAR2, sqlset_owner IN VARCHAR2 := NULL, staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL, db_version IN NUMBER := NULL); Examples Put all SQL tuning sets on the database in the staging table: BEGIN DBMS_SQLTUNE.PACK_STGTAB_SQLSET( sqlset_name => '%' , sqlset_owner => '%' , staging_table_name => 'STGTAB_SQLSET'); END; Put only those SQL tuning sets owned by the current user in the staging table: BEGIN DBMS_SQLTUNE.PACK_STGTAB_SQLSET( sqlset_name => '%' , staging_table_name => 'STGTAB_SQLSET'); END; Pack a specific SQL tuning set: BEGIN DBMS_SQLTUNE.PACK_STGTAB_SQLSET( sqlset_name => 'my_workload' , staging_table_name => 'STGTAB_SQLSET'); END; Pack a second SQL tuning set: BEGIN DBMS_SQLTUNE.PACK_STGTAB_SQLSET( sqlset_name => 'workload_subset' , staging_table_name => 'STGTAB_SQLSET'); END; Pack the STS my_workload_subset into a staging table stgtab_sqlset created for Oracle Database 11 g Release 1 (11.2): BEGIN DBMS_SQLTUNE.PACK_STGTAB_SQLSET( sqlset_name => 'workload_subset' , staging_table_name => 'STGTAB_SQLSET' , db_version => DBMS_SQLTUNE.STS_STGTAB_11_2_VERSION); END;