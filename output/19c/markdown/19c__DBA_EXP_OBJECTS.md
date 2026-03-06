---
id: 19c__DBA_EXP_OBJECTS
name: DBA_EXP_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_EXP_OBJECTS.html
---

# DBA_EXP_OBJECTS

DBA_EXP_OBJECTS describes objects that have been incrementally exported.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of exported object |
| OBJECT_NAME | VARCHAR2(128) | Name of exported object |
| OBJECT_TYPE | VARCHAR2(13) | Type of exported object |
| CUMULATIVE | DATE | Timestamp of last cumulative export |
| INCREMENTAL | DATE | Timestamp of last incremental export |
| EXPORT_VERSION | NUMBER(3) | The ID of the export session |