---
id: 19c__DBMS_SQLDIAG.UNPACK_STGTAB_SQLPATCH
name: DBMS_SQLDIAG.UNPACK_STGTAB_SQLPATCH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.UNPACK_STGTAB_SQLPATCH

This procedure unpacks from the staging table populated by a call to the PACK_STGTAB_SQLPATCH Procedure. It uses the patch data stored in the staging table to create patches on this system. Users can opt to replace existing patches with patch data when they exist already. In this case, note that it is only possible to replace patches referring to the same statement if the names are the same (see the ACCEPT_SQL_PATCH Function & Procedure).

## Syntax

```sql
DBMS_SQLDIAG.UPPACK_STGTAB_SQLPATCH (
   patch_name            IN  VARCHAR2 := '%',
   patch_category        IN  VARCHAR2 := '%',
   replace               IN  BOOLEAN,
   staging_table_name    IN  VARCHAR2,
   staging_schema_owner  IN  VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| patch_name | VARCHAR2 | IN | Name of patch to unpack (% wildcards acceptable, case-sensitive) |
| patch_category | VARCHAR2 | IN | Category from which to unpack patches (% wildcards acceptable, case-insensitive) |
| replace | BOOLEAN | IN | Replace patches if they already exist. Note that patches cannot be replaced if there is one in the staging table with the same name as an active patch on different SQL. The subprogram raises an error if there an attempt to create a patch that already exists. |
| staging_table_name | VARCHAR2 | IN | (Mandatory) Name of the table to use (case-sensitive) |
| staging_schema_owner | VARCHAR2 | IN | Schema where the table resides, or NULL for current schema (case-sensitive) |

## Usage Notes

Syntax DBMS_SQLDIAG.UPPACK_STGTAB_SQLPATCH ( patch_name IN VARCHAR2 := '%', patch_category IN VARCHAR2 := '%', replace IN BOOLEAN, staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL); Parameters Table 165-36 UPPACK_STGTAB_SQLPATCH Procedure Parameters Parameter Description patch_name Name of patch to unpack (% wildcards acceptable, case-sensitive) patch_category Category from which to unpack patches (% wildcards acceptable, case-insensitive) replace Replace patches if they already exist. Note that patches cannot be replaced if there is one in the staging table with the same name as an active patch on different SQL. The subprogram raises an error if there an attempt to create a patch that already exists. staging_table_name (Mandatory) Name of the table to use (case-sensitive) staging_schema_owner Schema where the table resides, or NULL for current schema (case-sensitive) Usage Notes Requires: ADMINISTER SQL MANAGEMENT OBJECT privilege and SELECT or READ privilege on the staging table By default, all SQL patches in the staging table are moved. The function commits after successfully loading each patch. If it fails in creating an individual patch, it raises an error and does not proceed to those remaining in the staging table.