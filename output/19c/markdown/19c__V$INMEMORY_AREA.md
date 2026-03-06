---
id: 19c__V$INMEMORY_AREA
name: V$INMEMORY_AREA
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-INMEMORY_AREA.html
---

# V$INMEMORY_AREA

V$INMEMORY_AREA contains information on the space allocation inside the In-Memory area.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POOL | VARCHAR2(26) |  |
| ALLOC_BYTES | NUMBER |  |
| USED_BYTES | NUMBER |  |
| POPULATE_STATUS | VARCHAR2(26) |  |
| CON_ID | NUMBER |  |

## Usage Notes

The In-Memory area is sub-divided into two pools: a 1MB pool used to store the actual column formatted data populated into memory, and a 64K pool used to store metadata about the objects that are populated into the In-Memory Column Store (IM column store). The amount of available memory in each pool is visible in the V$INMEMORY_AREA view. The relative size of the two pools is determined by internal heuristics. The majority of the In-Memory area memory is allocated to the 1MB pool. See Also: " INMEMORY_CLAUSE_DEFAULT " " V$IM_COLUMN_LEVEL " " V$IM_SEGMENTS " " V$IM_USER_SEGMENTS " Oracle Database In-Memory Guide for an introduction to the IM column store See Also: " INMEMORY_CLAUSE_DEFAULT " " V$IM_COLUMN_LEVEL " " V$IM_SEGMENTS " " V$IM_USER_SEGMENTS " Oracle Database In-Memory Guide for an introduction to the IM column store