---
id: 19c__DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF
name: DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF

This procedure changes the profile data values kept in the staging table prior to performing an unpack operation.

## Syntax

```sql
DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF (
  old_profile_name      IN VARCHAR2,
  new_profile_name      IN VARCHAR2 := NULL,
  new_profile_category  IN VARCHAR2 := NULL,
  staging_table_name    IN VARCHAR2,
  staging_schema_owner  IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| old_profile_name | VARCHAR2 | IN | The name of the profile to target for a remap operation (case-sensitive) |
| new_profile_name | VARCHAR2 | IN | The new name of the profile, or NULL to remain the same (case-sensitive) |
| new_profile_category | VARCHAR2 | IN | The new category for the profile, or NULL to remain the same (case-sensitive) |
| staging_table_name | VARCHAR2 | IN | The name of the table on which to perform the remap operation (case-sensitive). Required. |
| staging_schema_owner | VARCHAR2 | IN | The schema where the table resides, or NULL for current schema (case-sensitive) |

## Usage Notes

You can use this procedure to change the category of a profile. You can also use it to change the name of a profile if one already exists on the system with the same name. See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.REMAP_STGTAB_SQLPROF ( old_profile_name IN VARCHAR2, new_profile_name IN VARCHAR2 := NULL, new_profile_category IN VARCHAR2 := NULL, staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL); Parameters Table 169-28 REMAP_STGTAB_SQLPROF Procedure Parameters Parameter Description old_profile_name The name of the profile to target for a remap operation (case-sensitive) new_profile_name The new name of the profile, or NULL to remain the same (case-sensitive) new_profile_category The new category for the profile, or NULL to remain the same (case-sensitive) staging_table_name The name of the table on which to perform the remap operation (case-sensitive). Required. staging_schema_owner The schema where the table resides, or NULL for current schema (case-sensitive) Security Model This procedure requires the UPDATE privilege on the staging table.