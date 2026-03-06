---
id: 19c__ALL_CONTEXT
name: ALL_CONTEXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CONTEXT.html
---

# ALL_CONTEXT

DBA_CONTEXT describes all context namespaces defined in the database, regardless whether any attributes have been specified for them using the DBMS_SESSION.SET_CONTEXT procedure.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(128) | Name of the context namespace |
| SCHEMA | VARCHAR2(128) | Schema name of the designated package that can set attributes using this namespace |
| PACKAGE | VARCHAR2(128) | Package name of the designated package that can set attributes using this namespace |

## Usage Notes

Related View See Also: " DBA_CONTEXT " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SESSION.SET_CONTEXT procedure See Also: " DBA_CONTEXT " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SESSION.SET_CONTEXT procedure