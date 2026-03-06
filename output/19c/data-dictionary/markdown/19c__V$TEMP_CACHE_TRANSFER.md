---
id: 19c__V$TEMP_CACHE_TRANSFER
name: V$TEMP_CACHE_TRANSFER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-TEMP_CACHE_TRANSFER.html
---

# V$TEMP_CACHE_TRANSFER

V$TEMP_CACHE_TRANSFER is deprecated. The information that was provided in this view is now provided in the V$INSTANCE_CACHE_TRANSFER and V$SEGMENT_STATISTICS views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_NUMBER | NUMBER |  |
| X_2_NULL | NUMBER |  |
| X_2_NULL_FORCED_WRITE | NUMBER |  |
| X_2_NULL_FORCED_STALE | NUMBER |  |
| X_2_S | NUMBER |  |
| X_2_S_FORCED_WRITE | NUMBER |  |
| S_2_NULL | NUMBER |  |
| S_2_NULL_FORCED_STALE | NUMBER |  |
| RBR | NUMBER |  |
| RBR_FORCED_WRITE | NUMBER |  |
| NULL_2_X | NUMBER |  |
| S_2_X | NUMBER |  |
| NULL_2_S | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$INSTANCE_CACHE_TRANSFER " " V$SEGMENT_STATISTICS " See Also: " V$INSTANCE_CACHE_TRANSFER " " V$SEGMENT_STATISTICS "