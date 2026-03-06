---
id: 19c__V$FALSE_PING
name: V$FALSE_PING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-FALSE_PING.html
---

# V$FALSE_PING

V$FALSE_PING is deprecated. The information that was provided in this view is now provided in the V$INSTANCE_CACHE_TRANSFER and V$SEGMENT_STATISTICS views.

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
| PARTITION_NAME | VARCHAR2(128) |  |
| KIND | VARCHAR2(15) |  |
| OWNER# | NUMBER |  |
| LOCK_ELEMENT_ADDR | RAW(4 | 8) |  |
| LOCK_ELEMENT_NAME | NUMBER |  |
| CLASS# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$INSTANCE_CACHE_TRANSFER " " V$SEGMENT_STATISTICS " See Also: " V$INSTANCE_CACHE_TRANSFER " " V$SEGMENT_STATISTICS "