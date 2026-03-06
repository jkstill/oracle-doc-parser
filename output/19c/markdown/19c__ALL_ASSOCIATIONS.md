---
id: 19c__ALL_ASSOCIATIONS
name: ALL_ASSOCIATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ASSOCIATIONS.html
---

# ALL_ASSOCIATIONS

ALL_ASSOCIATIONS describes user-defined statistics associated with objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object for which the association is being defined |
| OBJECT_NAME | VARCHAR2(128) | Name of the object for which the association is being defined |
| COLUMN_NAME | VARCHAR2(128) | Column name in the object for which the association is being defined |
| OBJECT_TYPE | VARCHAR2(9) | Kind of object with which statistics are being associated: column, type, package or function, indextype, or domain index. |
| STATSTYPE_SCHEMA | VARCHAR2(128) | Owner of the statistics type |
| STATSTYPE_NAME | VARCHAR2(128) | Name of statistics type that contains the cost, selectivity or statistics functions |
| DEF_SELECTIVITY | NUMBER | Default selectivity of the object, if any |
| DEF_CPU_COST | NUMBER | Default CPU cost of the object, if any |
| DEF_IO_COST | NUMBER | Default I/O cost of the object, if any |
| DEF_NET_COST | NUMBER | Default networking cost of the object, if any |
| INTERFACE_VERSION | NUMBER | Identifies the version number of the ODCIStats interface. Value is 1 for statistics type implementing Oracle8 i 8.1; 0 for types implementing Oracle9 i 9.0.0. |
| MAINTENANCE_TYPE | VARCHAR2(14) | Specifies whether the object is system-managed or user-managed |

## Usage Notes

Related Views DBA_ASSOCIATIONS describes all user-defined statistics in the database. USER_ASSOCIATIONS describes user-defined statistics associated with objects owned by the current user. See Also: " DBA_ASSOCIATIONS " " USER_ASSOCIATIONS " See Also: " DBA_ASSOCIATIONS " " USER_ASSOCIATIONS "