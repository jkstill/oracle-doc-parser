---
id: 19c__DBA_OBJECT_SIZE
name: DBA_OBJECT_SIZE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_OBJECT_SIZE.html
---

# DBA_OBJECT_SIZE

DBA_OBJECT_SIZE lists the sizes, in bytes, of various PL/SQL objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(18) | Type of the object: TYPE, TYPE BODY, TABLE, VIEW, SYNONYM, SEQUENCE, PROCEDURE, FUNCTION, PACKAGE, PACKAGE BODY, JAVA SOURCE, JAVA CLASS or JAVA RESOURCE |
| SOURCE_SIZE | NUMBER | Size of the source in bytes. Must be in memory during compilation, or dynamic recompilation. |
| PARSED_SIZE | NUMBER | Size of the parsed form of the object, in bytes. Must be in memory when an object is being compiled that references this object. |
| CODE_SIZE | NUMBER | Code size, in bytes. Must be in memory when this object is executing. |
| ERROR_SIZE | NUMBER | Size of error messages, in bytes. In memory during the compilation of the object when there are compilation errors. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_OBJECT_SIZE lists the size of PL/SQL objects owned by the current user. See Also: " USER_OBJECT_SIZE " See Also: " USER_OBJECT_SIZE "