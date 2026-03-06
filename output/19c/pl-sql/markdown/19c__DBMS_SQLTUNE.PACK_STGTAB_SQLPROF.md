---
id: 19c__DBMS_SQLTUNE.PACK_STGTAB_SQLPROF
name: DBMS_SQLTUNE.PACK_STGTAB_SQLPROF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.PACK_STGTAB_SQLPROF

This procedure copies profile data from the SYS . schema into the staging table.

## Syntax

```sql
DBMS_SQLTUNE.PACK_STGTAB_SQLPROF (
   profile_name          IN VARCHAR2 := '%',
   profile_category      IN VARCHAR2 := 'DEFAULT',
   staging_table_name    IN VARCHAR2,
   staging_schema_owner  IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | The name of the profile to pack (% wildcards acceptable, case-sensitive) |
| profile_category | VARCHAR2 | IN | The category to pack profiles from (% wildcards acceptable, case-sensitive) |
| staging_table_name | VARCHAR2 | IN | The name of the table to use (case-insensitive unless double quoted). Required. |
| staging_schema_owner | VARCHAR2 | IN | The schema where the table resides, or NULL for current schema (case-insensitive unless double quoted) |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.PACK_STGTAB_SQLPROF ( profile_name IN VARCHAR2 := '%', profile_category IN VARCHAR2 := 'DEFAULT', staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL); Parameters Table 169-27 PACK_STGTAB_SQLPROF Procedure Parameters Parameter Description profile_name The name of the profile to pack (% wildcards acceptable, case-sensitive) profile_category The category to pack profiles from (% wildcards acceptable, case-sensitive) staging_table_name The name of the table to use (case-insensitive unless double quoted). Required. staging_schema_owner The schema where the table resides, or NULL for current schema (case-insensitive unless double quoted) Security Model This procedures requires ADMINISTER SQL MANAGEMENT OBJECT privilege and INSERT privilege on the staging table.