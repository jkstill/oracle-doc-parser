---
id: 19c__ALL_HIERARCHIES
name: ALL_HIERARCHIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIERARCHIES.html
---

# ALL_HIERARCHIES

ALL_HIERARCHIES describes the hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| DIMENSION_OWNER | VARCHAR2(128) | Owner of the attribute dimension used by the hierarchy |
| DIMENSION_NAME | VARCHAR2(128) | Name of the attribute dimension used by the hierarchy |
| PARENT_ATTR | VARCHAR2 | The value of this column is always NULL |
| COMPILE_STATE | VARCHAR2(7) | Compile status of the hierarchy: VALID INVALID |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_HIERARCHIES describes all hierarchies in the database. USER_HIERARCHIES describes the hierarchies owned by the current user. This view does not display the OWNER column. See Also: " DBA_HIERARCHIES " " USER_HIERARCHIES " See Also: " DBA_HIERARCHIES " " USER_HIERARCHIES "