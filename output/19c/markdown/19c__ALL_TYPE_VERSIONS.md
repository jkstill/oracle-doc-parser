---
id: 19c__ALL_TYPE_VERSIONS
name: ALL_TYPE_VERSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_TYPE_VERSIONS.html
---

# ALL_TYPE_VERSIONS

ALL_TYPE_VERSIONS describes the versions of the object types accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(128) | Name of the type |
| VERSION# | NUMBER | Internal version number of the type |
| TYPECODE | VARCHAR2(128) | Typecode of the type |
| STATUS | VARCHAR2(7) | Status of the type: N/A VALID INVALID |
| LINE | NUMBER | Line number of the type's spec |
| TEXT | VARCHAR2(4000) | Text of the type's spec |
| HASHCODE | RAW(17) | Hashcode of the type |

## Usage Notes

Related Views DBA_TYPE_VERSIONS describes the versions of all object types in the database. USER_TYPE_VERSIONS describes the versions of the object types owned by the current user. This view does not display the OWNER column. See Also: " DBA_TYPE_VERSIONS " " USER_TYPE_VERSIONS " See Also: " DBA_TYPE_VERSIONS " " USER_TYPE_VERSIONS "