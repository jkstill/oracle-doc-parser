---
id: 19c__V$LOCK_ACTIVITY
name: V$LOCK_ACTIVITY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LOCK_ACTIVITY.html
---

# V$LOCK_ACTIVITY

V$LOCK_ACTIVITY is deprecated. The information that was provided in this view is now provided in the V$INSTANCE_CACHE_TRANSFER and V$SEGMENT_STATISTICS views.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FROM_VAL | CHAR(4) |  |
| TO_VAL | CHAR(1) |  |
| ACTION_VAL | CHAR(21) |  |
| COUNTER | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$INSTANCE_CACHE_TRANSFER " " V$SEGMENT_STATISTICS " See Also: " V$INSTANCE_CACHE_TRANSFER " " V$SEGMENT_STATISTICS "