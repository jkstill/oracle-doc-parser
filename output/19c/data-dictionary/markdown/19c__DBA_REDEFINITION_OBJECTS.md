---
id: 19c__DBA_REDEFINITION_OBJECTS
name: DBA_REDEFINITION_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_REDEFINITION_OBJECTS.html
---

# DBA_REDEFINITION_OBJECTS

DBA_REDEFINITION_OBJECTS is an online redefinition view. It displays the objects involved in the current redefinitions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_TYPE | VARCHAR2(12) | Type of the redefinition object: TABLE INDEX CONSTRAINT TRIGGER NESTED TABLE PARTITION MV LOG |
| OBJECT_OWNER | VARCHAR2(4000) | Owner of the redefinition object |
| OBJECT_NAME | VARCHAR2(128) | Name of the redefinition object |
| BASE_TABLE_OWNER | VARCHAR2(128) | Owner of the base table of the redefinition object |
| BASE_TABLE_NAME | VARCHAR2(128) | Name of the base table of the redefinition object |
| INTERIM_OBJECT_OWNER | VARCHAR2(4000) | Owner of the corresponding interim redefinition object |
| INTERIM_OBJECT_NAME | VARCHAR2(128) | Name of the corresponding interim redefinition object |
| EDITION_NAME | VARCHAR2(128) | Reserved for future use |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Administrator’s Guide for more information about online redefinition See Also: Oracle Database Administrator’s Guide for more information about online redefinition