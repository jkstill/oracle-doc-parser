---
id: 19c__V$RESULT_CACHE_OBJECTS
name: V$RESULT_CACHE_OBJECTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [dynamic_performance]
source_file: V-RESULT_CACHE_OBJECTS.html
---

# V$RESULT_CACHE_OBJECTS

V$RESULT_CACHE_OBJECTS displays all the objects (both cached results and dependencies) and their attributes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| TYPE | VARCHAR2(10) |  |
| STATUS | VARCHAR2(9) |  |
| BUCKET_NO | NUMBER |  |
| HASH | NUMBER |  |
| NAME | VARCHAR2(387) |  |
| NAMESPACE | VARCHAR2(10) |  |
| CREATION_TIMESTAMP | DATE |  |
| CREATOR_UID | NUMBER |  |
| DEPEND_COUNT | NUMBER |  |
| BLOCK_COUNT | NUMBER |  |
| SCN | NUMBER |  |
| COLUMN_COUNT | NUMBER |  |
| PIN_COUNT | NUMBER |  |
| SCAN_COUNT | NUMBER |  |
| ROW_COUNT | NUMBER |  |
| ROW_SIZE_MAX | NUMBER |  |
| ROW_SIZE_MIN | NUMBER |  |
| ROW_SIZE_AVG | NUMBER |  |
| BUILD_TIME | NUMBER |  |
| LRU_NUMBER | NUMBER |  |
| OBJECT_NO | NUMBER |  |
| INVALIDATIONS | NUMBER |  |
| SPACE_OVERHEAD | NUMBER |  |
| SPACE_UNUSED | NUMBER |  |
| CACHE_ID | VARCHAR2(387) |  |
| CACHE_KEY | VARCHAR2(387) |  |
| CHECKSUM | NUMBER |  |
| EDITION_ID | NUMBER |  |
| DB_LINK | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |