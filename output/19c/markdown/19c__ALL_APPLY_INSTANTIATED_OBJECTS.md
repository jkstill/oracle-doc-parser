---
id: 19c__ALL_APPLY_INSTANTIATED_OBJECTS
name: ALL_APPLY_INSTANTIATED_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_APPLY_INSTANTIATED_OBJECTS.html
---

# ALL_APPLY_INSTANTIATED_OBJECTS

ALL_APPLY_INSTANTIATED_OBJECTS displays information about objects accessible to the current user for which an instantiation SCN has been set.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SOURCE_DATABASE | VARCHAR2(128) | Name of the database where the object originated |
| SOURCE_OBJECT_OWNER | VARCHAR2(128) | Owner of the object at the source database |
| SOURCE_OBJECT_NAME | VARCHAR2(128) | Name of the object at the source database |
| SOURCE_OBJECT_TYPE | VARCHAR2(11) | Type of the object at the source database |
| INSTANTIATION_SCN | NUMBER | Instantiation SCN for the object. Only changes committed after this SCN are applied by an apply process. |
| IGNORE_SCN | NUMBER | SCN below which the instantiation SCN cannot be set. This value corresponds to the SCN value at the source database at the time when the object was prepared for instantiation. |
| APPLY_DATABASE_LINK | VARCHAR2(128) | Database link to which changes are applied. If null, then changes are applied to the local database. |
| SOURCE_ROOT_NAME | VARCHAR2(128) | The global name of the source root database |

## Usage Notes

Related View DBA_APPLY_INSTANTIATED_OBJECTS displays information about objects for which an instantiation SCN has been set. See Also: " DBA_APPLY_INSTANTIATED_OBJECTS " See Also: " DBA_APPLY_INSTANTIATED_OBJECTS "