---
id: 19c__DBA_GLOBAL_CONTEXT
name: DBA_GLOBAL_CONTEXT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_GLOBAL_CONTEXT.html
---

# DBA_GLOBAL_CONTEXT

DBA_GLOBAL_CONTEXT displays the definition (name, schema, and package) of all global contexts created in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(128) | Name of the context namespace |
| SCHEMA | VARCHAR2(128) | Schema of the package that administers the globally accessible context |
| PACKAGE | VARCHAR2(128) | Package that administers the globally accessible context |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view is a subset of DBA_CONTEXT , which describes all contexts, including global contexts. See Also: " DBA_CONTEXT " Oracle Database Security Guide for more information about using global application contexts Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SESSION.SET_CONTEXT procedure See Also: " DBA_CONTEXT " Oracle Database Security Guide for more information about using global application contexts Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SESSION.SET_CONTEXT procedure