---
id: 19c__DBMS_SQLDIAG.PACK_STGTAB_SQLPATCH
name: DBMS_SQLDIAG.PACK_STGTAB_SQLPATCH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.PACK_STGTAB_SQLPATCH

This procedure packs SQL patches into the staging table created by a call to the CREATE_STGTAB_SQLPATCH Procedure.

## Syntax

```sql
DBMS_SQLDIAG.PACK_STGTAB_SQLPATCH (
   patch_name            IN  VARCHAR2 := '%',
   patch_category        IN  VARCHAR2 := 'DEFAULT',
   staging_table_name    IN  VARCHAR2,
   staging_schema_owner  IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patch_name | VARCHAR2 | IN | Name of patch to pack (% wildcards acceptable, case-sensitive) |
| patch_category | VARCHAR2 | IN | Category to which to pack patches (% wildcards acceptable, case-insensitive) |
| staging_table_name | VARCHAR2 | IN | (Mandatory) Name of the table to use (case-sensitive) |
| staging_schema_owner | VARCHAR2 | IN | Schema where the table resides, or NULL for current schema (case-sensitive) |

## Usage Notes

Syntax DBMS_SQLDIAG.PACK_STGTAB_SQLPATCH ( patch_name IN VARCHAR2 := '%', patch_category IN VARCHAR2 := 'DEFAULT', staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL); Parameters Table 165-29 PACK_STGTAB_SQLPATCH Procedure Parameters Parameter Description patch_name Name of patch to pack (% wildcards acceptable, case-sensitive) patch_category Category to which to pack patches (% wildcards acceptable, case-insensitive) staging_table_name (Mandatory) Name of the table to use (case-sensitive) staging_schema_owner Schema where the table resides, or NULL for current schema (case-sensitive) Usage Notes Requires: ADMINISTER SQL PLAN MANAGEMENT OBJECT privilege and INSERT privilege on the staging table By default, we move all SQL patches in category DEFAULT . Note that the subprogram issues a COMMIT after packing each SQL patch, so if an error is raised in mid-execution, some patches may be in the staging table.