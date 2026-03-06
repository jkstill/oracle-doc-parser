---
id: 19c__ALL_PLSQL_OBJECT_SETTINGS
name: ALL_PLSQL_OBJECT_SETTINGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [all]
source_file: ALL_PLSQL_OBJECT_SETTINGS.html
---

# ALL_PLSQL_OBJECT_SETTINGS

ALL_PLSQL_OBJECT_SETTINGS displays information about the compiler settings for the stored objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(12) | Type of the object: PROCEDURE FUNCTION PACKAGE PACKAGE BODY TRIGGER TYPE TYPE BODY |
| PLSQL_OPTIMIZE_LEVEL | NUMBER | Optimization level that was used to compile the object |
| PLSQL_CODE_TYPE | VARCHAR2(4000) | Compilation mode for the object |
| PLSQL_DEBUG | VARCHAR2(4000) | Indicates whether the object was compiled with debug information or not |
| PLSQL_WARNINGS | VARCHAR2(4000) | Compiler warning settings that were used to compile the object |
| NLS_LENGTH_SEMANTICS | VARCHAR2(4000) | NLS length semantics that were used to compile the object |
| PLSQL_CCFLAGS | VARCHAR2(4000) | Conditional compilation flag settings that were used to compile the object |
| PLSCOPE_SETTINGS | VARCHAR2(4000) | Settings for using PL/Scope |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_PLSQL_OBJECT_SETTINGS displays information about the compiler settings for all stored objects in the database. USER_PLSQL_OBJECT_SETTINGS displays information about the compiler settings for the stored objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_PLSQL_OBJECT_SETTINGS " " USER_PLSQL_OBJECT_SETTINGS " See Also: " DBA_PLSQL_OBJECT_SETTINGS " " USER_PLSQL_OBJECT_SETTINGS "