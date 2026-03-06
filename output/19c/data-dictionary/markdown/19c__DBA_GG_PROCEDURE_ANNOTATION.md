---
id: 19c__DBA_GG_PROCEDURE_ANNOTATION
name: DBA_GG_PROCEDURE_ANNOTATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_GG_PROCEDURE_ANNOTATION.html
---

# DBA_GG_PROCEDURE_ANNOTATION

DBA_GG_PROCEDURE_ANNOTATION annotates the position of Owner and Object arguments in procedure calls.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PACKAGE_OWNER | VARCHAR2(384) | Procedure package owner |
| PACKAGE_NAME | VARCHAR2(384) | Procedure package name |
| PROCEDURE_NAME | VARCHAR2(384) | Procedure name |
| OBJECT_OWNER_ARGPOS | NUMBER | Object owner name position in argument list, -1 if not present |
| OBJECT_ARGPOS | NUMBER | Object name position in argument list, -1 if not present |
| MIN_DB_VERSION | VARCHAR2(100) | Minimum database version for the procedure |
| MAX_DB_VERSION | VARCHAR2(100) | Maximum database version for the procedure |
| MIN_REDO_COMPAT_LEVEL | VARCHAR2(100) | Minimum redo compatibility for the procedure |
| MAX_REDO_COMPAT_LEVEL | VARCHAR2(100) | Maximum redo compatibility for the procedure |
| FLAGS | NUMBER | Additional information about procedure arguments |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content