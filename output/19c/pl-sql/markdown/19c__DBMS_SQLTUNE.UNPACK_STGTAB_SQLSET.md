---
id: 19c__DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET
name: DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET

This procedure copies one or more SQL tuning sets from their location in the staging table into the SQL tuning sets schema, making them proper SQL tuning sets.

## Syntax

```sql
DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET (
   sqlset_name          IN VARCHAR2 := '%',
   sqlset_owner         IN VARCHAR2 := NULL,
   replace              IN BOOLEAN,
   staging_table_name   IN VARCHAR2,
   staging_schema_owner IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sqlset_name | VARCHAR2 | IN | Specifies the name of the tuning set to unpack (not null). Wildcard characters ( % ) are supported to unpack multiple tuning sets in a single call. For example, specify % to unpack all tuning sets from the staging table. |
| sqlset_owner | VARCHAR2 | IN | Specifies the name of tuning set owner, or NULL for the current schema owner. Wildcard characters ( % ) are supported. |
| replace | BOOLEAN | IN | Specifies whether to replace an existing SQL tuning set. If FALSE , then this procedure raises errors when you try to create a tuning set that already exists. |
| staging_table_name | VARCHAR2 | IN | Specifies the name of the staging table, moved after a call to the DBMS_SQLTUNE.PACK_STGTAB_SQLSET or DBMS_SQLSET.PACK_STGTAB procedure (case-sensitive). |
| staging_schema_owner | VARCHAR2 | IN | Specifies the name of staging table owner, or NULL for the current schema owner (case-sensitive). |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Tuning Set Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET ( sqlset_name IN VARCHAR2 := '%', sqlset_owner IN VARCHAR2 := NULL, replace IN BOOLEAN, staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL); Parameters The parameters are identical for DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET and DBMS_SQLSET.UNPACK_STGTAB . Table 169-49 UNPACK_STGTAB_SQLSET and UNPACK_STGTAB Procedure Parameters Parameter Description sqlset_name Specifies the name of the tuning set to unpack (not null). Wildcard characters ( % ) are supported to unpack multiple tuning sets in a single call. For example, specify % to unpack all tuning sets from the staging table. sqlset_owner Specifies the name of tuning set owner, or NULL for the current schema owner. Wildcard characters ( % ) are supported. replace Specifies whether to replace an existing SQL tuning set. If FALSE , then this procedure raises errors when you try to create a tuning set that already exists. staging_table_name Specifies the name of the staging table, moved after a call to the DBMS_SQLTUNE.PACK_STGTAB_SQLSET or DBMS_SQLSET.PACK_STGTAB procedure (case-sensitive). staging_schema_owner Specifies the name of staging table owner, or NULL for the current schema owner (case-sensitive). Examples -- unpack all STS in the staging table EXEC DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET(sqlset_name => '%', - sqlset_owner => '%', - replace => FALSE, - staging_table_name => 'STGTAB_SQLSET'); -- errors can arise during STS unpack when a STS in the staging table has the -- same name/owner as STS on the system. In this case, users should call -- remap_stgtab_sqlset to patch the staging table and with which to call unpack -- Replace set to TRUE. EXEC DBMS_SQLTUNE.UNPACK_STGTAB_SQLSET(sqlset_name => '%', - sqlset_owner => '%', - replace => TRUE, - staging_table_name => 'STGTAB_SQLSET');