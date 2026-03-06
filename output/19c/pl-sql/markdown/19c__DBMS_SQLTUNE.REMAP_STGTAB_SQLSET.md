---
id: 19c__DBMS_SQLTUNE.REMAP_STGTAB_SQLSET
name: DBMS_SQLTUNE.REMAP_STGTAB_SQLSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLTUNE
tags: [dbms_sqltune]
source_file: DBMS_SQLTUNE.html
---

# DBMS_SQLTUNE.REMAP_STGTAB_SQLSET

This procedure changes the tuning set names and owners in the staging table so that they can be unpacked with different values.

## Syntax

```sql
DBMS_SQLTUNE.REMAP_STGTAB_SQLSET (
   old_sqlset_name        IN VARCHAR2,
   old_sqlset_owner       IN VARCHAR2 := NULL,
   new_sqlset_name        IN VARCHAR2 := NULL,
   new_sqlset_owner       IN VARCHAR2 := NULL,
   staging_table_name     IN VARCHAR2,
   staging_schema_owner   IN VARCHAR2 := NULL
   old_con_dbid           IN NUMBER   := NULL,
   new_con_dbid           IN NUMBER   := NULL);
);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| old_sqlset_name | VARCHAR2 | IN | Specifies the name of the tuning set to target for a remap operation. Wildcard characters ( % ) are not supported. |
| old_sqlset_owner | VARCHAR2 | IN | Specifies the new name of the tuning set owner to target for a remap operation. NULL for current schema owner |
| new_sqlset_name | VARCHAR2 | IN | Specifies the new name for the tuning set, or NULL to keep the same tuning set name. |
| new_sqlset_owner | VARCHAR2 | IN | Specifies the new owner for the tuning set, or NULL to keep the same owner name. |
| staging_table_name | VARCHAR2 | IN | Specifies the name of the table on which to perform the remap operation. The value is case sensitive. |
| staging_schema_owner | VARCHAR2 | IN | Specifies the name of staging table owner, or NULL for the current schema owner. The value is case sensitive. |
| old_con_dbid | NUMBER | IN | Specifies the old container DBID to be remapped to a new container DBID. Specify NULL to use the same container DBID. You must provide both old_con_dbid and new_con_dbid for the remap to succeed. |
| new_con_dbid | NUMBER | IN | Specifies the new container DBID to replace with the old container DBID. Specify NULL to use the same container DBID. You must provide both old_con_dbid and new_con_dbid for the remap to succeed. |

## Usage Notes

See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group See Also: DBMS_SQLTUNE SQL Profile Subprograms for other subprograms in this group Syntax DBMS_SQLTUNE.REMAP_STGTAB_SQLSET ( old_sqlset_name IN VARCHAR2, old_sqlset_owner IN VARCHAR2 := NULL, new_sqlset_name IN VARCHAR2 := NULL, new_sqlset_owner IN VARCHAR2 := NULL, staging_table_name IN VARCHAR2, staging_schema_owner IN VARCHAR2 := NULL old_con_dbid IN NUMBER := NULL, new_con_dbid IN NUMBER := NULL); ); Parameters The parameters are identical for the DBMS_SQLTUNE.REMAP_STGTAB_SQLSET and DBMS_SQLSET.REMAP_SQLSET procedures. Table 169-29 REMAP_STGTAB_SQLSET and REMAP_SQLSET Procedure Parameters Parameter Description old_sqlset_name Specifies the name of the tuning set to target for a remap operation. Wildcard characters ( % ) are not supported. old_sqlset_owner Specifies the new name of the tuning set owner to target for a remap operation. NULL for current schema owner new_sqlset_name Specifies the new name for the tuning set, or NULL to keep the same tuning set name. new_sqlset_owner Specifies the new owner for the tuning set, or NULL to keep the same owner name. staging_table_name Specifies the name of the table on which to perform the remap operation. The value is case sensitive. staging_schema_owner Specifies the name of staging table owner, or NULL for the current schema owner. The value is case sensitive. old_con_dbid Specifies the old container DBID to be remapped to a new container DBID. Specify NULL to use the same container DBID. You must provide both old_con_dbid and new_con_dbid for the remap to succeed. new_con_dbid Specifies the new container DBID to replace with the old container DBID. Specify NULL to use the same container DBID. You must provide both old_con_dbid and new_con_dbid for the remap to succeed. Usage Notes Call this procedure multiple times to remap more than one tuning set name or owner. This procedure only handles one tuning set per call.