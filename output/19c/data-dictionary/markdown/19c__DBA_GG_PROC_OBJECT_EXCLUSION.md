---
id: 19c__DBA_GG_PROC_OBJECT_EXCLUSION
name: DBA_GG_PROC_OBJECT_EXCLUSION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_GG_PROC_OBJECT_EXCLUSION.html
---

# DBA_GG_PROC_OBJECT_EXCLUSION

DBA_GG_PROC_OBJECT_EXCLUSION provides details about all tables that should be filtered when operating on given objects.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PACKAGE_OWNER | VARCHAR2(384) | Procedure package owner |
| PACKAGE_NAME | VARCHAR2(384) | Procedure package name |
| OBJECT_OWNER | VARCHAR2(384) | Object owner to filter for the given procedure |
| OBJECT_NAME | VARCHAR2(384) | Object name to filter for the given procedure |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content