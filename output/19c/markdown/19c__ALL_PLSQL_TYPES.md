---
id: 19c__ALL_PLSQL_TYPES
name: ALL_PLSQL_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_PLSQL_TYPES.html
---

# ALL_PLSQL_TYPES

ALL_PLSQL_TYPES describes the PL/SQL types accessible to the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the type |
| TYPE_NAME | VARCHAR2(136) | Name of the type |
| PACKAGE_NAME | VARCHAR2(128) | Name of the package containing the type |
| TYPE_OID | RAW(16) | Object identifier (OID) of the type |
| TYPECODE | VARCHAR2(58) | Typecode of the type |
| ATTRIBUTES | NUMBER | Number of attributes in the type |
| CONTAINS_PLSQL | VARCHAR2(3) | Indicates whether the type contains PL/SQL-specific data types ( YES ) or not ( NO ) |

## Usage Notes

Related Views DBA_PLSQL_TYPES describes all the PL/SQL types in the database. USER_PLSQL_TYPES describes the user's own PL/SQL types. This view does not display the OWNER column. See Also: " DBA_PLSQL_TYPES " " USER_PLSQL_TYPES " See Also: " DBA_PLSQL_TYPES " " USER_PLSQL_TYPES "