---
id: 19c__V$SQL_PLAN
name: V$SQL_PLAN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_PLAN.html
---

# V$SQL_PLAN

V$SQL_PLAN contains the execution plan information for each child cursor loaded in the library cache.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDRESS | RAW(4 | 8) |  |
| HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| PLAN_HASH_VALUE | NUMBER |  |
| FULL_PLAN_HASH_VALUE | NUMBER |  |
| CHILD_ADDRESS | RAW(4 | 8) |  |
| CHILD_NUMBER | NUMBER |  |
| TIMESTAMP | DATE |  |
| OPERATION | VARCHAR2(120) |  |
| OPTIONS | VARCHAR2(120) |  |
| OBJECT_NODE | VARCHAR2(160) |  |
| OBJECT# | NUMBER |  |
| OBJECT_OWNER | VARCHAR2(128) |  |
| OBJECT_NAME | VARCHAR2(128) |  |
| OBJECT_ALIAS | VARCHAR2(261) |  |
| OBJECT_TYPE | VARCHAR2(80) |  |
| OPTIMIZER | VARCHAR2(80) |  |
| ID | NUMBER |  |
| PARENT_ID | NUMBER |  |
| DEPTH | NUMBER |  |
| POSITION | NUMBER |  |
| SEARCH_COLUMNS | NUMBER |  |
| COST | NUMBER |  |
| CARDINALITY | NUMBER |  |
| BYTES | NUMBER |  |
| OTHER_TAG | VARCHAR2(140) |  |
| PARTITION_START | VARCHAR2(256) |  |
| PARTITION_STOP | VARCHAR2(256) |  |
| PARTITION_ID | NUMBER |  |
| OTHER | VARCHAR2(4000) |  |
| DISTRIBUTION | VARCHAR2(80) |  |
| CPU_COST | NUMBER |  |
| IO_COST | NUMBER |  |
| TEMP_SPACE | NUMBER |  |
| ACCESS_PREDICATES | VARCHAR2(4000) |  |
| FILTER_PREDICATES | VARCHAR2(4000) |  |
| PROJECTION | VARCHAR2(4000) |  |
| TIME | NUMBER |  |
| QBLOCK_NAME | VARCHAR2(128) |  |
| REMARKS | VARCHAR2(4000) |  |
| OTHER_XML | CLOB |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content