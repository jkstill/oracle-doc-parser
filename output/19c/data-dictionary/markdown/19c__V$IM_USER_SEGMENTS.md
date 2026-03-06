---
id: 19c__V$IM_USER_SEGMENTS
name: V$IM_USER_SEGMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-IM_USER_SEGMENTS.html
---

# V$IM_USER_SEGMENTS

V$IM_USER_SEGMENTS presents information about the in-memory segments for the current user in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEGMENT_NAME | VARCHAR2(128) |  |
| PARTITION_NAME | VARCHAR2(128) |  |
| SEGMENT_TYPE | VARCHAR2(18) |  |
| TABLESPACE_NAME | VARCHAR2(30) |  |
| INMEMORY_SIZE | NUMBER |  |
| BYTES | NUMBER |  |
| BYTES_NOT_POPULATED | NUMBER |  |
| POPULATE_STATUS | VARCHAR2(13) |  |
| INMEMORY_PRIORITY | VARCHAR2(8) |  |
| INMEMORY_DISTRIBUTE | VARCHAR2(15) |  |
| INMEMORY_DUPLICATE | VARCHAR2(13) |  |
| INMEMORY_COMPRESSION | VARCHAR2(17) |  |
| INMEMORY_SERVICE | VARCHAR2(12) |  |
| INMEMORY_SERVICE_NAME | VARCHAR2(129) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Only segments that have an in-memory representation are displayed. If a segment is marked for the In-Memory Column Store (IM column store) but is not populated, no corresponding row for that segment is displayed in this view. See Also: " INMEMORY_CLAUSE_DEFAULT " " V$IM_COLUMN_LEVEL " " V$IM_SEGMENTS " Oracle Database In-Memory Guide for an introduction to the IM column store See Also: " INMEMORY_CLAUSE_DEFAULT " " V$IM_COLUMN_LEVEL " " V$IM_SEGMENTS " Oracle Database In-Memory Guide for an introduction to the IM column store