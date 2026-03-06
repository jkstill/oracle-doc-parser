---
id: 19c__ALL_APPLY_INSTANTIATED_GLOBAL
name: ALL_APPLY_INSTANTIATED_GLOBAL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_APPLY_INSTANTIATED_GLOBAL.html
---

# ALL_APPLY_INSTANTIATED_GLOBAL

ALL_APPLY_INSTANTIATED_GLOBAL displays information for the current user about databases for which an instantiation SCN has been set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_DATABASE | VARCHAR2(128) | Name of the database that was instantiated |
| INSTANTIATION_SCN | NUMBER | Instantiation SCN for the database. Only changes committed after this SCN are applied by an apply process. |
| APPLY_DATABASE_LINK | VARCHAR2(128) | Database link to which changes are applied. If null, then changes are applied to the local database. |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database |

## Usage Notes

Related View DBA_APPLY_INSTANTIATED_GLOBAL displays information about databases for which an instantiation SCN has been set. See Also: " DBA_APPLY_INSTANTIATED_GLOBAL " See Also: " DBA_APPLY_INSTANTIATED_GLOBAL "