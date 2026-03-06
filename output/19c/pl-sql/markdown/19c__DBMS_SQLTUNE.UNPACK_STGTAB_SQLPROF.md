---
id: 19c__DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF
name: DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF

This procedure copies profile data stored in the staging table to create profiles on the system.

## Syntax

```sql
DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF (
   profile_name          IN VARCHAR2 := '%',
   profile_category      IN VARCHAR2 := 'DEFAULT',
   replace               IN BOOLEAN,
   staging_table_name    IN VARCHAR2,
   staging_schema_owner  IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| profile_name | VARCHAR2 | IN | The name of the profile to unpack ( % wildcards acceptable, case-sensitive) |
| profile_category | VARCHAR2 | IN | The category from which to unpack profiles ( % wildcards acceptable, case-sensitive) |
| replace | BOOLEAN | IN | The option to replace profiles if they already exist. Note that profiles cannot be replaced if one in the staging table has the same name as an active profile in a different SQL statement. If FALSE , this function raises errors if you try to create a profile that already exists |
| staging_table_name | VARCHAR2 | IN | The name of the table on which to perform the remap operation (case-insensitive unless double quoted). Required. |
| staging_schema_owner | VARCHAR2 | IN | The schema where the table resides, or NULL for current schema (case-insensitive unless double quoted) |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.UNPACK_STGTAB_SQLPROF ( profile_name IN VARCHAR2 := '%', profile_category IN VARCHAR2 := 'DEFAULT', replace IN BOOLEAN, staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL); Parameters Table 169-48 UNPACK_STGTAB_SQLPROF Procedure Parameters Parameter Description profile_name The name of the profile to unpack ( % wildcards acceptable, case-sensitive) profile_category The category from which to unpack profiles ( % wildcards acceptable, case-sensitive) replace The option to replace profiles if they already exist. Note that profiles cannot be replaced if one in the staging table has the same name as an active profile in a different SQL statement. If FALSE , this function raises errors if you try to create a profile that already exists staging_table_name The name of the table on which to perform the remap operation (case-insensitive unless double quoted). Required. staging_schema_owner The schema where the table resides, or NULL for current schema (case-insensitive unless double quoted) Usage Notes Using this procedure requires the CREATE ANY SQL PROFILE privilege and the SELECT privilege on staging table.