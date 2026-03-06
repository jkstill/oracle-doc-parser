---
id: 19c__DBA_APPLY_VALUE_DEPENDENCIES
name: DBA_APPLY_VALUE_DEPENDENCIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_APPLY_VALUE_DEPENDENCIES.html
---

# DBA_APPLY_VALUE_DEPENDENCIES

DBA_APPLY_VALUE_DEPENDENCIES displays information about the value dependencies for all apply processes in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DEPENDENCY_NAME | VARCHAR2(128) | Name of the dependency |
| OBJECT_OWNER | VARCHAR2(128) | Owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| COLUMN_NAME | VARCHAR2(128) | Name of the column |
| COLUMN_POSITION | NUMBER | Position of the column |