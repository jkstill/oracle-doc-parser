---
id: 19c__ALL_CUBE_NAMED_BUILD_SPECS
name: ALL_CUBE_NAMED_BUILD_SPECS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CUBE_NAMED_BUILD_SPECS.html
---

# ALL_CUBE_NAMED_BUILD_SPECS

ALL_CUBE_NAMED_BUILD_SPECS describes the OLAP cube named build specifications in the database that are accessible by the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the OLAP named build specification |
| CUBE_NAME | VARCHAR2(128) | Name of the OLAP cube |
| NAMED_BUILD_SPEC | CLOB | Name of the OLAP cube named build specification |

## Usage Notes

Related Views DBA_CUBE_NAMED_BUILD_SPECS describes the OLAP cube named build specifications in the database. USER_CUBE_NAMED_BUILD_SPECS describes the OLAP cube named build specifications in the database that are owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_NAMED_BUILD_SPECS " " USER_CUBE_NAMED_BUILD_SPECS " See Also: " DBA_CUBE_NAMED_BUILD_SPECS " " USER_CUBE_NAMED_BUILD_SPECS "