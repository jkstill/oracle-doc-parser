---
id: 19c__DBA_ADVISOR_OBJECT_TYPES
name: DBA_ADVISOR_OBJECT_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dba]
source_file: DBA_ADVISOR_OBJECT_TYPES.html
---

# DBA_ADVISOR_OBJECT_TYPES

DBA_ADVISOR_OBJECT_TYPES displays information about the object types used by all advisors in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_TYPE_ID | NUMBER | Type identifier |
| OBJECT_TYPE | VARCHAR2(64) | Type name |

## Usage Notes

In addition to the regular database object types (such as TABLE and INDEX ), the following types are defined: SYSTEM I/O SGA PGA SHARED POOL BUFFER CACHE LIBRARY CACHE PROCESS SESSION ENQUEUE LATCH ROLLBACK SEGMENT FILE PARAMETER CURSOR SQL SQL WORKLOAD