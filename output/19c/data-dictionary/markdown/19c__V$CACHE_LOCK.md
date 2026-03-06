---
id: 19c__V$CACHE_LOCK
name: V$CACHE_LOCK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-CACHE_LOCK.html
---

# V$CACHE_LOCK

V$CACHE_LOCK is deprecated. The information that was provided in this view is now provided in the V$INSTANCE_CACHE_TRANSFER and V$SEGMENT_STATISTICS views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| STATUS | VARCHAR2(10) |  |
| XNC | NUMBER |  |
| FORCED_READS | NUMBER |  |
| FORCED_WRITES | NUMBER |  |
| NAME | VARCHAR2(128) |  |
| KIND | VARCHAR2(15) |  |
| OWNER# | NUMBER |  |
| LOCK_ELEMENT_ADDR | RAW(4 | 8) |  |
| LOCK_ELEMENT_NAME | NUMBER |  |
| INDX | NUMBER |  |
| CLASS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content