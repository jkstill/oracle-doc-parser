---
id: 19c__ALL_APPLY_INSTANTIATED_SCHEMAS
name: ALL_APPLY_INSTANTIATED_SCHEMAS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_INSTANTIATED_SCHEMAS.html
---

# ALL_APPLY_INSTANTIATED_SCHEMAS

ALL_APPLY_INSTANTIATED_SCHEMAS displays information about schemas accessible to the current user for which an instantiation SCN has been set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_DATABASE | VARCHAR2(128) | Name of the database where the schema originated |
| SOURCE_SCHEMA | VARCHAR2(128) | Name of the schema at the source database |
| INSTANTIATION_SCN | NUMBER | Instantiation SCN for the schema. Only changes committed after this SCN are applied by an apply process. |
| APPLY_DATABASE_LINK | VARCHAR2(128) | Database link to which changes are applied. If null, then changes are applied to the local database. |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_APPLY_INSTANTIATED_SCHEMAS displays information about schemas for which an instantiation SCN has been set. See Also: " DBA_APPLY_INSTANTIATED_SCHEMAS " See Also: " DBA_APPLY_INSTANTIATED_SCHEMAS "