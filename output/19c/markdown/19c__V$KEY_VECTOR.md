---
id: 19c__V$KEY_VECTOR
name: V$KEY_VECTOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-KEY_VECTOR.html
---

# V$KEY_VECTOR

V$KEY_VECTOR provides debugging information related to the data structures used by in-memory aggregation for current and recent queries using key vectors.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| CON_ID | NUMBER |  |
| TRANSLATE_ID | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_EXEC_START | DATE |  |
| SQL_EXEC_ID | NUMBER |  |
| PROCESS | VARCHAR2(64) |  |
| STATE | VARCHAR2(9) |  |
| TYPE | VARCHAR2(9) |  |
| WIDTH | NUMBER |  |
| KEY_DATA_TYPE | VARCHAR2(13) |  |
| JOIN_COLUMN_COUNT | NUMBER |  |
| JOIN_KEY_COUNT | NUMBER |  |
| DUP_JOIN_KEY_COUNT | NUMBER |  |
| MIN_JOIN_KEY | NUMBER |  |
| MAX_JOIN_KEY | NUMBER |  |
| GROUP_KEY_COUNT | NUMBER |  |
| FILTERED | NUMBER |  |
| PROBED | NUMBER |  |
| ACTIVE | NUMBER |  |
| DISABLED | NUMBER |  |
| MEMORY_ALLOCATED | NUMBER |  |
| JOIN_STRUCTURE_SIZE | NUMBER |  |
| FACT_OWNER | VARCHAR2(128) |  |
| FACT_NAME | VARCHAR2(128) |  |
| DIMENSION_OWNER | VARCHAR2(128) |  |
| DIMENSION_NAME | VARCHAR2(128) |  |
| CREATION_DURATION | NUMBER |  |
| PAYLOAD_COLUMN_COUNT | NUMBER |  |

## Usage Notes

See Also: Oracle Database SQL Tuning Guide for more information about in-memory aggregation See Also: Oracle Database SQL Tuning Guide for more information about in-memory aggregation